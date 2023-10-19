from posixpath import abspath
import dotenv 
import os 
from pathlib import Path 

# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

class Settings():
    database: str = os.environ['DATABASE'] 
    hostname: str = os.environ['HOSTNAME']
    db_username: str = os.environ['DB_USERNAME']
    password: str = os.environ['PASSWORD']
    port_id: str = os.environ['PORT']

settings = Settings()
print(settings.database)
print(dotenv_file)
