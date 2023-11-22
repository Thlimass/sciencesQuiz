import json
from peewee import Model, CharField, TextField, ForeignKeyField, DateTimeField
from entities.category import Category
import datetime
from quiz_db import db


class Question(Model):
    category = ForeignKeyField(Category, backref='questions')
    question_text = TextField()
    correct_answer = CharField()
    incorrect_answers = TextField()  # Armazenado como uma string JSON
    created_at = DateTimeField(default=datetime.datetime.now)
    update_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

    def to_dict(self):
        return {
            'category': self.category.name,
            'question': self.question_text,
            'correct_answer': self.correct_answer,
            'incorrect_answers': json.loads(self.incorrect_answers)
        }
