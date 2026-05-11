import sqlite3, json, os, uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from datetime import datetime

app = FastAPI()

# Servir el frontend correctamente
if os.path.exists("frontend"):
    app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Bd Interna
def init_db():
    conn = sqlite3.connect("pxl_chat.db")
    conn.execute("CREATE TABLE IF NOT EXISTS messages (username TEXT, content TEXT, timestamp TEXT, date TEXT)")
    conn.commit()
    conn.close()

init_db()

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            try: await connection.send_json(message)
            except: pass

manager = ConnectionManager()

@app.websocket("/ws/{user}")
async def websocket_endpoint(websocket: WebSocket, user: str):
    await manager.connect(websocket)
    
    # Cargar historial de la conversacion
    conn = sqlite3.connect("pxl_chat.db")
    cursor = conn.execute("SELECT username, content, timestamp, date FROM messages ORDER BY rowid ASC")
    for row in cursor.fetchall():
        await websocket.send_json({"user": row[0], "msg": row[1], "time": row[2], "date": row[3], "type": "chat"})
    conn.close()

    # Mensaje de entrada al chat
    await manager.broadcast({"msg": f"📢 {user} se ha unido a la sesión", "type": "sys"})

    try:
        while True:
            data = await websocket.receive_text()
            now = datetime.now()
            t, d = now.strftime("%H:%M"), now.strftime("%Y-%m-%d")
            
            conn = sqlite3.connect("pxl_chat.db")
            conn.execute("INSERT INTO messages VALUES (?, ?, ?, ?)", (user, data, t, d))
            conn.commit()
            conn.close()

            await manager.broadcast({"user": user, "msg": data, "time": t, "date": d, "type": "chat"})
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast({"msg": f"🚪 {user} ha abandonado la sesión", "type": "sys"})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)