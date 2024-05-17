from typing import Dict, List, TypeVar, Any
from peewee import ModelSelect
from models.model_db import db, BaseModel


def store_date(db: db, model: Any, *data: List[Dict]) -> None:
    with db.atomic():
        model.insert_many(*data).excute()


def retrieve_data(db: db,  model: Any, *columns: BaseModel) -> ModelSelect:
    with db.atomic():
        response = model.select(*columns)

    return response
