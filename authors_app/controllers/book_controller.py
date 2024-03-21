# from flask import Blueprint, Request, jsonify
# from authors_app.book import Book

# book = Blueprint('book', __name__, url_prefix='api/v1/book')  

# @auth.route('/register', methods=['POST'])

# def register():
#     title = request.json['title']
#     description = request.json['description']
#     publication_date= request.json['publication_date']
#     image = request.json['image']
#     pages = request.json['pages']
#     price= request.json['price']
#     company_id= request.json['company_id']
#     user_id= request.json['user_id']


#     if not title:
#         return jsonify({'error': "Title is required"})
#     if not description:
#         return jsonify({'error': 'Description is required'})
#     if not publication_date:
#         return jsonify({'error': 'Publication date is required'})
#     if not image:
#         return jsonify({'error': 'Your image is required'})


# # creating a new book
#     new_book = Book(title=title, description=description, publication_date=publication_date,
#                     image=image, pages=pages, price=price, company_id=company_id, user_id=user_id)


from flask import Blueprint,request,jsonify
#from app.stutus_code import HTTP_400_BAD_REQUEST,HTTP_409CONFLICT,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_201_CREATED
#import validators
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri_here'
app.config['SECRET_KEY'] = 'your_secret_key_here'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


auth = Blueprint('auth', __name__, Url_prefix='api/v1/auth')


# User registration

@auth.route('/reqister', methods=['POST'])

def reqister_user():
    
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    contact = data.get('contact')
    image= data.get('image')
    password = data.get('password')
    biography = data.get('biography', '') if type == "author" else''
    #validation for the incoming request.
    
    
    if not first_name or last_name or not contact or not password or not email:
        return jsonify({ "error": "All field are required" }),HTTP_400_BAD_REQUEST
    
    if type == 'author' and not biography:
        return jsonify({ "error": "Enter your authors biography" }),HTTP_400_BAD_REQUEST
    
    if len(password) <8:
         return jsonify({ "error": "password is too short" }),HTTP_400_BAD_REQUEST
     
    if not validators.email(email):
         return jsonify({ "error": "email is not valid" }),HTTP_400_BAD_REQUEST
     
    if user.query.filter_by(email=email).first() is not None:
        return jsonify({ "error": "email address in use" }),HTTP_409_CONFLICT
    
    if user.query.filter_by(contact=contact).first() is not None:
        return jsonify({ "error": "email address in use" }),HTTP_409_CONFLICT
    
    try:
        hashed_password = bcrypt.generate_password_hash(password)# hashing aperson
        # creating a new user
        new_user = user(first_name=first_name,last_name=last_name,password=hashed_password,email=email,contact=contact,biography=biography)
        db.session.add(new_user)
        db.session.commit()
        
        # username
        
        username = new_user.get_full_name()
        
        
        return jsonify({
            'message': username + "has been successfully created" + new_user.user_type,
            'user':{
                "id":new_user.id,
                "first_name":new_user.first_name,
                "last_name":new_user.last_name,
                "email":new_user.email,
                "contact":new_user.contact,
                "type":new_user.type,
                "biography":new_user.biography,
                "created_at":new_user.created_at,
                
            }
            
            
            
            
        }),HTTP_201_CREATED
    except Exception as e: 
        db.session.rollback()   
        return jsonify({'error':str(e)}),HTTP_500_INTERNAL_SERVER_ERROR