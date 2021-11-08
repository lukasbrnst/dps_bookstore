from flask_sqlalchemy import SQLAlchemy
import sys
sys.path.append(__file__+"/..") 
from backend.db_tables import metadata

db = SQLAlchemy(metadata=metadata, session_options={"expire_on_commit": False})
