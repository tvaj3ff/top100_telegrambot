from typing import Dict, List, TypeVar
from peewee import ModelSelect
from models.model_db import db, BaseModel

T = TypeVar("T")


def _store_date(db: db, model: T, *data: List[Dict]) -> None:
    with db.atomic():
        model.insert_many(*data).excute()


def _retrieve_data(db: db, model: T, *columns: BaseModel) -> ModelSelect:
    with db.atomic():
        response = model.select(*columns)

    return response


class CRUDInterface:
    @staticmethod
    def create():
        return _store_date

    @staticmethod
    def retrieve():
        return _retrieve_data


if __name__ == "__main__":
    _store_date()
    _retrieve_data()
    CRUDInterface()
