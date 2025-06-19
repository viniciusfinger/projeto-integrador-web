from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from service.client_contact_service import ClientContactService
from database import get_db
from model.client_contact import ClientContactResponse

router = APIRouter()

@router.get("/client-contacts", response_model=List[ClientContactResponse])
def find_all_client_contacts(db: Session = Depends(get_db)):
    client_contact_service = ClientContactService(db)
    
    try:
        contacts = client_contact_service.find_all_client_contacts()
        return contacts
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar contatos dos clientes: {str(e)}")

@router.put("/client-contacts/{contact_id}/status", response_model=ClientContactResponse)
def change_contact_status(contact_id: int, db: Session = Depends(get_db)):
    client_contact_service = ClientContactService(db)
    
    try:
        updated_contact = client_contact_service.change_contact_status(contact_id)
        return updated_contact
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao alterar status do contato: {str(e)}")

