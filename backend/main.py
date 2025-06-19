from controller import auth_controller, client_contact_controller
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from model.user import Base as UserBase
from model.client_contact import ClientContact
from database import engine, Base

# Criar todas as tabelas
Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

app.include_router(auth_controller.router, tags=["auth"])
app.include_router(client_contact_controller.router, tags=["client-contacts"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)