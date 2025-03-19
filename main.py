from mcstatus import JavaServer, motd
from typing import Annotated, Literal
from fastapi import FastAPI

app = FastAPI()

@app.get("/api-2/{server}/{port}/{class2}/{class3}")
async def players(server: str, port: str, class2: str, class3: str):
    server = JavaServer.lookup(f"{server}:{port}")
    status = server.status()
    if class2 == "players":
        if class3 == "online":
            return {"response": status.players.online}
        elif class3 == "max":
            return {"response": status.players.max}

@app.get("/api-1/{server}/{port}/{class2}")
async def players(server: str, port: str, class2: str):
    server = JavaServer.lookup(f"{server}:{port}")
    status = server.status()
    if class2 == "motd":
        return {"response": status.motd}
