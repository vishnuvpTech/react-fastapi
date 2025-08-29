from fastapi import FastAPI
from app.user_app import routers as user_routers

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI backend!"}

app.include_router(user_routers.router)
