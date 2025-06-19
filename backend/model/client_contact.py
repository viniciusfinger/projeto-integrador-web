from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean
from database import Base

from enum import Enum

class ContactStatus(str, Enum):
    waiting = "waiting"
    contacted = "contacted"
    finalized = "finalized"

class ClientContactResponse(BaseModel):
    id: int
    client_name: str
    client_number: str
    have_art: bool
    tattoo_artist_wanted: str
    status: ContactStatus
    class Config:
        orm_mode = True


class ClientContactCreate(BaseModel):
    client_name: str
    client_number: str
    have_art: bool
    tattoo_artist_wanted: str
    status: ContactStatus

class ClientContact(Base):
    __tablename__ = "client_contacts"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, nullable=False)
    client_number = Column(String, nullable=False)
    have_art = Column(Boolean, nullable=False, default=False)
    tattoo_artist_wanted = Column(String, nullable=False) 
    status = Column(String, nullable=False, default=ContactStatus.waiting)