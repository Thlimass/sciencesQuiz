# from entities.category import Category
#
#
# class CategoryRepository:
#     @staticmethod
#     def create_category(name):
#         return Category.create(name=name)
#
#     @staticmethod
#     def get_category_by_id(category_id):
#         return Category.get_or_none(Category.id == category_id)
#
#     @staticmethod
#     def update_category_name(category_id, new_name):
#         category = Category.get_or_none(Category.id == category_id)
#         if category:
#             category.name = new_name
#             category.save()
#             return category
#         return None
#
#     @staticmethod
#     def delete_category(category_id):
#         category = Category.get_or_none(Category.id == category_id)
#         if category:
#             category.delete_instance()
#             return True
#         return False
