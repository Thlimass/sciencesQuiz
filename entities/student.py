from peewee import Model, SqliteDatabase, CharField, IntegerField, DateTimeField
import datetime

db = SqliteDatabase('db/quiz_db.sqlite')


class Student(Model):
    student_id = IntegerField(primary_key=True)
    name = CharField()
    age = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    update_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
