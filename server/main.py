from fastapi import FastAPI
from server.routers import quests

app = FastAPI()

app.include_router(quests.router)


@app.get("/")
def home():
    return {"Greeting": "Hello, Stalker..."}
