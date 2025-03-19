from mcstatus import JavaServer, motd
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
    elif class2 == "version":
        if class3 == "name":
            return {"response": status.version.name}
        elif class3 == "protocol":
            return {"response": status.version.protocol}


@app.get("/api-1/{server}/{port}/{class2}")
async def players(server: str, port: str, class2: str):
    server = JavaServer.lookup(f"{server}:{port}")
    status = server.status()
    if class2 == "motd":
        return {"response": status.motd}
    elif class2 == "raw":
        return {"response": status.raw}
    elif class2 == "enforces-secure-chat":
        return {"response": status.enforces_secure_chat}
