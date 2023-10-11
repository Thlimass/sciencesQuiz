from peewee import Model, SqliteDatabase, IntegerField, TextField, DateTimeField, ForeignKeyField
from entities.student import Student
from entities.category import Category
from entities.round import Round

db = SqliteDatabase('db/quiz_db.sqlite')


class StudentAnswer(Model):
    student_answer_id = IntegerField(primary_key=True)
    student = ForeignKeyField(Student, backref='questions')
    category = ForeignKeyField(Category, backref='questions')
    round_id = ForeignKeyField(Round, backref='questions')
    answers_correct = TextField()

    class Meta:
        database = db
