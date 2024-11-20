from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy import select
from database.models import Phonebook

def insert_contact(session: Session, name: str, number: str) -> bool:
    """
        Insert a single contact into the database
        - 'name' must be a string with the max length of 20
        - 'number' must be a 9-digit string
    """
    # Validate inputs
    if not isinstance(name, str) or len(name) > 20:
        raise ValueError("Name must be a string with max length 20.")
    if not isinstance(name, str) or not number.isdigit() or len(number) != 9:
        raise ValueError("Number must be a 9-digit string.")
    
    # Check if the name already exists in the database
    contact = session.query(Phonebook).filter_by(name=name).first()
    if contact:
        return False
    
    # Add new contact to the database
    try:    
        session.add(Phonebook(name=name, number=number))
        session.commit()
        return True
    except SQLAlchemyError as e:
        session.rollback()
        raise SQLAlchemyError(f"SQLAlchemy raised exception: {e}")
    except Exception as e:
        session.rollback()
        raise SQLAlchemyError(f"Unknown error raised exception: {e}")
    finally:
        session.close()


def get_all_contacts(session: Session):
    # Get all contacts from the database
    contacts = session.execute(select(Phonebook)).scalars().all()
    
    # Return all contacts as a dictionary
    return [{"name": contact.name, "number": contact.number} for contact in contacts]