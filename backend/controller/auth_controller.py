from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from service.auth_service import AuthService, ACCESS_TOKEN_EXPIRE_MINUTES
from database import get_db
from model.user import UserCreate, Token, UserResponse

from typing import List
from model.servico import ServicoResponse
from service.servico_service import ServicoService

router = APIRouter()

@router.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    
    if auth_service.get_user(user.email):
        raise HTTPException(status_code=400, detail="Email já registrado")
    
    db_user = auth_service.create_user(user.name, user.email, user.password)
    
    access_token = auth_service.create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    user = auth_service.authenticate_user(form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = auth_service.create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"} 

@router.get("/status-servicos", response_model=List[ServicoResponse])
def listar_status_servicos(db: Session = Depends(get_db)):
    servico_service = ServicoService(db)
    return servico_service.listar_servicos()