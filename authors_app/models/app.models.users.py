#from app.extensions import db

class User(db.Model):
    # Define your User model here
    pass
from app.models.users import User
from app.extensions import db, bcrypt
