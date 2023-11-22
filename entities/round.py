# from peewee import Model, TextField, DateTimeField, ForeignKeyField
# from entities.student import Student
# from entities.category import Category
# import datetime
# from quiz_db import db
#
#
# class Round(Model):
#     student = ForeignKeyField(Student, backref='questions')
#     category = ForeignKeyField(Category, backref='questions')
#     incorrect_answers = TextField()
#     created_at = DateTimeField(default=datetime.datetime.now)
#     updated_at = DateTimeField(default=datetime.datetime.now)
#
#     class Meta:
#         database = db
