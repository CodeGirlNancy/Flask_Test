# from authors_app import db
from authors_app.extensions import db
from datetime import datetime


class Company(db.Model):
 __tablename__="Companies"
 id =db.Column(db.Integer,primary_key=True)
 name=db.Column(db.String(50),nullable=False,unique=True)
 description=db.Column(db.String(100),nullable=False)
 user_id =db.Column(db.Integer, db.ForeignKey("users.id"))
 #user=db.relationship('User',backref='companies') 