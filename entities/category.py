from peewee import Model, SqliteDatabase, IntegerField,CharField, DateTimeField
import datetime

db = SqliteDatabase('db/quiz_db.sqlite')


class Category(Model):
    category_id = IntegerField(primary_key=True)
    name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
