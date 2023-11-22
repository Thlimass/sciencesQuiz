# import datetime
#
# from sqlalchemy import DateTime, func
#
# from quiz_db import db
#
#
# class Category(db.Model):
#     __tablename__ = 'category'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
#     created_at = db.Column(DateTime(timezone=True), server_default=func.now())
#     updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())
#
#     class Meta:
#         database = db
#
#     def json(self):
#         return {'id': self.id, 'name': self.username, 'created_at': self.created_at, 'updated_at': self.created_at}
