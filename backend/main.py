import sqlite3
import json
import random
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from datetime import datetime
from typing import List

app = FastAPI()

# --- INICIALIZACIÓN DE BASE DE DATOS (HU06) ---
def init_db():
    conn = sqlite3.connect("pxl_chat.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            content TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# --- GESTOR DE CONEXIONES ---
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)

manager = ConnectionManager()

@app.websocket("/ws/{client_name}")
async def websocket_endpoint(websocket: WebSocket, client_name: str):
    await manager.connect(websocket)
    
    # Cargar Historial de la Base de Datos al entrar
    conn = sqlite3.connect("pxl_chat.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, content, timestamp FROM messages ORDER BY id ASC LIMIT 50")
    for row in cursor.fetchall():
        await websocket.send_json({
            "user": row[0], 
            "msg": row[1], 
            "time": row[2], 
            "type": "chat"
        })
    conn.close()

    # Notificación de entrada (Limpia)
    join_time = datetime.now().strftime("%H:%M")
    await manager.broadcast({
        "user": "", 
        "msg": f"📢 {client_name} se ha unido al chat", 
        "time": join_time, 
        "type": "sys"
    })

    try:
        while True:
            # Recibir mensaje del cliente
            data = await websocket.receive_text()
            current_time = datetime.now().strftime("%H:%M")
            
            # Guardar en Base de Datos (Persistencia)
            conn = sqlite3.connect("pxl_chat.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO messages (username, content, timestamp) VALUES (?, ?, ?)",
                           (client_name, data, current_time))
            conn.commit()
            conn.close()

            # Enviar a todos
            await manager.broadcast({
                "user": client_name, 
                "msg": data, 
                "time": current_time, 
                "type": "chat"
            })
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        exit_time = datetime.now().strftime("%H:%M")
        await manager.broadcast({
            "user": "", 
            "msg": f"🚪 {client_name} ha salido", 
            "time": exit_time, 
            "type": "sys"
        })