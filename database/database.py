import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]

# Create database engine
engine = create_engine(DATABASE_URL)

# Create session factory to generate sessions
Session = sessionmaker(autocommit=False, bind=engine)

def get_session():
    # Get new session
    return Session()