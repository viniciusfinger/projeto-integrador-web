from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class ClientContact(Base):
    __tablename__ = "client_contacts"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, nullable=False)
    client_number = Column(String, nullable=False)
    have_art = Column(Boolean, nullable=False, default=False)
    tattoo_artist_wanted = Column(String, nullable=False) 