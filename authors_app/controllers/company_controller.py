from flask import Blueprint, Request, jsonify
from authors_app.company import Company

company = Blueprint('auth', __name__, url_prefix='api/v1/company')  

@auth.route('/register', methods=['POST'])

def register():
    name = request.json['name']
    description = request.json['description']
    user_id = request.json['user_id']
    origin = request.json['origin']
    user_id= request.json['user_id']
    

    if not name:
        return jsonify({'error': "Name is required"})
    if not description:
        return jsonify({'error': 'Description is required'})
    if not origin:
        return jsonify({'error': 'Origin date is required'})



# creating a new company
    new_company = Company(name=name, description=description, origin=origin)