from CRUD import CRUDInterface
from models.model_db import db, BaseModel

db.connect()
db.create_tables(BaseModel.__subclasses__())
crud = CRUDInterface()

if __name__ == "__main__":
    crud()
