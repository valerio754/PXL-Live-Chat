import random
import sqlite3
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

# --- Configuración de Base de Datos ---
def init_db():
    conn = sqlite3.connect("pxl_chat.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            content TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

def save_message(user, content):
    conn = sqlite3.connect("pxl_chat.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (username, content) VALUES (?, ?)", (user, content))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect("pxl_chat.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, content FROM messages ORDER BY id DESC LIMIT 20")
    rows = cursor.fetchall()
    conn.close()
    return rows[::-1] # Invertir para que salgan en orden cronológico

# --- Lógica de Conexiones ---
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    user_id = random.randint(100, 999)
    username = f"Usuario_{user_id}"
    await manager.connect(websocket)
    
    # 1. Enviar historial al nuevo usuario (HU06)
    history = get_history()
    for user, content in history:
        await websocket.send_text(f"💬 {user}: {content}")

    # 2. Notificar entrada
    await manager.broadcast(f"📢 {username} se ha unido al chat")
    
    try:
        while True:
            data = await websocket.receive_text()
            save_message(username, data) # Guardar en DB
            await manager.broadcast(f"💬 {username}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"🚪 {username} ha dejado el chat")