from sqlalchemy import Column, Integer, String
from app.api_v1 import db
class User(db.Model):
    __tablename__='user'

    id=Column(db.Integer,primary_key=True)
    name=Column(db.String(255))
    age=Column(db.Integer)
    password=Column(db.String(80))

    def __init__(self,id,name,age,password):
        self.id=id
        self.name=name
        self.age=age
        self.password=password

    def __repr__(self):
        return '' %self.name





