from flask import Blueprint, request, jsonify
from authors_app.models import user
from authors_app.extensions import db, bcrypt

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

@auth.route('/register', methods=['POST'])
def register():
    try:
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        email = request.json['email'] 
        contact = request.json['contact']
        password = request.json['password']
        biography = request.json['biography']
        user_type = request.json['user_type']

        # hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        if not first_name:
            return jsonify({"error": "Your first name is required"})
        if not last_name:
            return jsonify({"error": "Your last name is required"})
        if not email:
            return jsonify({"error": "Your email is required"})
        if not contact:
            return jsonify({"error": "Your contact is required"})
        if len(password) < 8:  # Changed the condition to check for less than 8 characters
            return jsonify({"error": "Your password should have at least 8 characters"})
        if user_type == 'author' and not biography:
            return jsonify({"error": "Your biography is required"})
        if not user_type:
            return jsonify({"error": "Your user_type is required"})

        # Check for existing email and contact
        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already exists'})
        if User.query.filter_by(contact=contact).first():
            return jsonify({'error': 'Contact already exists'})

        new_user = User(
            last_name=last_name,
            first_name=first_name,
            email=email,
            password=hashed_password,
            contact=contact,
            user_type=user_type
        )

        db.session.add(new_user)
        db.session.commit()

        username = f"{new_user.first_name} {new_user.last_name}"

        return jsonify({
            'message': f'{username} has been successfully created as an {new_user.user_type}',
            'user': {
                'first_name': new_user.first_name,
                'last_name': new_user.last_name,
                'email': new_user.email,
                'contact': new_user.contact,
                'type': new_user.user_type,
                'created_at': new_user.created_at
            }
        })
    except Exception as e:
        db.session.rollback()
    return jsonify({'error': str(e)})

