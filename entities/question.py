# entities/question.py

from peewee import Model, SqliteDatabase, IntegerField, TextField, DateTimeField, ForeignKeyField
from entities.category import Category
import datetime

db = SqliteDatabase('db/quiz_db.sqlite')


class Question(Model):
    question_id = IntegerField(primary_key=True)
    category = ForeignKeyField(Category, backref='questions')
    incorrect_answers = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    update_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
