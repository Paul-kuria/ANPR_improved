from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 

from config import Settings 

settings = Settings()
database = settings.database
ipaddress = settings.hostname
db_username = settings.db_username
password = settings.password
print(db_username)

SQLALCHEMY_DB_URL = (f"postgresql://{db_username}:{password}@{ipaddress}/{database}")
engine = create_engine(SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() 

'''SQL_Alchemy dependency'''
def get_db():
    db= SessionLocal()
    try:
        yield db 
    finally:
        db.close()