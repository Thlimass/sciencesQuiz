# from entities.question import Question
#
# class QuestionRepository:
#     @staticmethod
#     def create_question(category_id, question_text, correct_answer, incorrect_answers):
#         return Question.create(
#             category_id=category_id,
#             question_text=question_text,
#             correct_answer=correct_answer,
#             incorrect_answers=incorrect_answers
#         )
#
#     @staticmethod
#     def get_question_by_id(question_id):
#         return Question.get_or_none(Question.id == question_id)
#
#     # Outros métodos para operações relacionadas a perguntas
