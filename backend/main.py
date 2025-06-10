from controller import auth_controller
from fastapi import FastAPI
import uvicorn
from model.user import Base
from database import engine


Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(auth_controller.router, tags=["auth"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)