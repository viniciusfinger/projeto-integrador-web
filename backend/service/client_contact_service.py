from typing import List
from sqlalchemy.orm import Session
from model.client_contact import ClientContact, ClientContactCreate, ClientContactResponse, ContactStatus


class ClientContactService:
    def __init__(self, db: Session):
        self.db = db

    def create_client_contact(self, client_contact: ClientContactCreate) -> ClientContact:
        db_client_contact = ClientContact(
            client_name=client_contact.client_name,
            client_number=client_contact.client_number,
            have_art=client_contact.have_art,
            tattoo_artist_wanted=client_contact.tattoo_artist_wanted,
            status=client_contact.status
        )
        self.db.add(db_client_contact)
        self.db.commit()
        self.db.refresh(db_client_contact)
        return db_client_contact

    def find_all_client_contacts(self) -> List[ClientContact]:
        return self.db.query(ClientContact).all()

    def get_client_contact_by_id(self, contact_id: int) -> ClientContact:
        return self.db.query(ClientContact).filter(ClientContact.id == contact_id).first()

    def change_contact_status(self, contact_id: int) -> ClientContact:
        client_contact = self.get_client_contact_by_id(contact_id)
        
        if not client_contact:
            raise ValueError("Contato do cliente não encontrado")
        
        if client_contact.status == ContactStatus.waiting:
            client_contact.status = ContactStatus.contacted
        elif client_contact.status == ContactStatus.contacted:
            client_contact.status = ContactStatus.finalized
        elif client_contact.status == ContactStatus.finalized:
            client_contact.status = ContactStatus.waiting
        
        self.db.commit()
        self.db.refresh(client_contact)
        return client_contact 