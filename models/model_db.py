from peewee import (
    AutoField,
    CharField,
    TextField,
    DateField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase,
)

from config_data.config import DATE_FORMAT, DB_PATH


db = SqliteDatabase(DB_PATH)


class BaseModel(Model):

    class Meta:
        database = db


class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    username = CharField()
    first_name = CharField()
    last_name = CharField(null=True)


class History(BaseModel):
    history_id = AutoField(primary_key=True)
    created_at = DateField()
    user_id = ForeignKeyField(User, backref="history")
    message = TextField()

    def __str__(self):
        return "{id}.{created_at} -- {message}".format(
            id=self.history_id,
            created_at=self.created_at,
            message=self.message,
        )


def create_models():
    db.create_tables(BaseModel.__subclasses__())
