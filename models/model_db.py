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
    history_id = AutoField()
    created_at = DateField()
    user = ForeignKeyField(User, backref="history")
    message = TextField()

    def __str__(self):
        return "{id}.{date} - {message}".format(
            id=self.history_id,
            message=self.message,
            date=self.created_at.strftime(DATE_FORMAT),
        )


def create_models():
    db.create_tables(BaseModel.__subclasses__())
