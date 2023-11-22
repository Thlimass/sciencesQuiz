# from entities.student_answers import StudentAnswers
# import json
#
#
# class StudentAnswersRepository:
#     @staticmethod
#     def create_student_answer(student_id, category_id, round_id, answers_correct):
#         return StudentAnswers.create(
#             student_id=student_id,
#             category_id=category_id,
#             round_id=round_id,
#             answers_correct=json.dumps(answers_correct)
#         )
#
#     @staticmethod
#     def get_student_answers_by_student_id(student_id):
#         return StudentAnswers.select().where(StudentAnswers.student_id == student_id)
