from controller import auth_controller
from fastapi import FastAPI

app = FastAPI()

app.include_router(auth_controller.router, tags=["auth"])