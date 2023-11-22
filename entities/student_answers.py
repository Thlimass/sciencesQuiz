# import datetime
# import json
# from peewee import Model, IntegerField, TextField, DateTimeField, ForeignKeyField
# from entities.student import Student
# from entities.category import Category
# from entities.round import Round
# from quiz_db import db
#
#
# class StudentAnswers(Model):
#     student_answer_id = IntegerField(primary_key=True)
#     student = ForeignKeyField(Student, backref='questions')
#     category = ForeignKeyField(Category, backref='questions')
#     round_id = ForeignKeyField(Round, backref='questions')
#     answers_correct = TextField()  # Armazenar múltiplas respostas corretas em formato JSON
#     created_at = DateTimeField(default=datetime.datetime.now)
#     updated_at = DateTimeField(default=datetime.datetime.now)
#
#     def set_answers_correct(self, answers):
#         self.answers_correct = json.dumps(answers)
#
#     def get_answers_correct(self):
#         return json.loads(self.answers_correct)
#
#     class Meta:
#         database = db
