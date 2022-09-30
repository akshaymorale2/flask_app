import uuid
import jwt
import datetime
from flask import request, jsonify, make_response, Blueprint, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Users
from functools import wraps
from .. import db

app = Blueprint('user', __name__, url_prefix='/user')


# def token_required(f):
#     @wraps(f)
#     def decorator(*args, **kwargs):
#
#         token = None
#
#         if 'x-access-tokens' in request.headers:
#             token = request.headers['x-access-tokens']
#
#         if not token:
#             return jsonify({'message': 'a valid token is missing'})
#
#         try:
#             data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
#             current_user = Users.query.filter_by(public_id=data['public_id']).first()
#         except:
#             return jsonify({'message': 'token is invalid'})
#
#         return f(current_user, *args, **kwargs)
#     return decorator


@app.route('/register', methods=['POST'])
def signup_user():
    print("in register _____________")
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = Users(
        public_id=str(uuid.uuid4()),
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=hashed_password,
        username=data['username'],
        dateOfBirth=data['dateOfBirth'],
        contactNumber=data['contactNumber'],
        gender=data['gender'],
        is_verified=True
    )
    db.session.add(new_user)
    db.session.commit()
    print("user added________________")

    return jsonify({'message': 'registeration successfully'})


# @login_manager.user_loader
# def load_user(user_id):
#     return Users.query.filter_by(id=user_id).first()


@app.route('/login', methods=['POST'])
def social_login_user():
    print(request)
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    print(username, password, data)
    # auth = request.authorization

    # if not auth or not auth.username or not auth.password:
    #     return make_response('could not verify', 401, {'Authentication': 'login required"'})

    user = Users.query.filter_by(username=username).first()
    print("user---------------", user)
    if check_password_hash(user.password, password):
        # login_user(user)
        print("user logged in-------------")

        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, current_app.config['SECRET_KEY'], "HS256")
        response_data = {
            'user': user.username,
            'id': user.id,
            'token': token
        }
        return jsonify(response_data)

    return make_response('could not verify',  401, {'Authentication': '"login required"'})


# @app.route('/getuser/<int:id>', methods=['GET'])
# def getUser(id):
#     if request.method == 'GET':
#         user = Users.query.filter_by(id=id).first()
#         print(user)
#         if user:
#             response_data = {
#                 'username': user.username,
#                 'id': user.id,
#                 'first_name': user.first_name,
#                 'last_name': user.last_name,
#                 'email': user.email,
#                 'dateOfBirth': user.dateOfBirth,
#                 'contactNo': user.contactNumber,
#                 'gender': user.gender,
#                 'profilePhoto': user.profilePhoto
#             }
#             return jsonify(**response_data, safe=False)
#         return jsonify("User not found!!!", safe=False)

#
# @app.route('/shouts/', methods=['POST'])\
# def shouts():
#
#     if request.method == 'POST':
#         shout_data = request.get_json()
#
#         new_shout = Shouts(
#             user_id=shout_data['user'],
#             textdata=shout_data['textdata'],
#             type=shout_data['type']
#         )
#
#         db.session.add(new_shout)
#         db.session.commit()
#
#         return jsonify({'message': 'Shout added successfully'})
#
#
# @app.route('/shoutsList/', methods=['GET'])
# def shoutsList():
#     if request.method == 'GET':
#         shoutsList = Shouts.query.order_by(Shouts.date_added.desc()).all()
#         # shout_records = []
#         # for shouts in shoutsList:
#         #     shout = {
#         #         'id' : shouts.id,
#         #         'dateAdded' : shouts.dateAdded
#
#         #     }
#
#         print(type(shoutsList))
#
#         print("===================================", shoutsList)
#         # user_records = []
#         # for shout in shoutsList():
#         #     for value in shout.value():
#         #         print(shout['user_id'])
#         #         users = Users.query.filter_by(id=shout['user_id'])
#         #         user = {
#         #             'username': users.username,
#         #             'id': users.id,
#         #             'first_name': users.first_name,
#         #             'last_name': users.last_name,
#         #             'email': users.email,
#         #             'dateOfBirth': users.dateOfBirth,
#         #             'contactNo': users.contactNo,
#         #             'gender': users.gender,
#         #             'profilePhoto': users.profilePhoto
#         #         }
#         #         print(user)
#         #         user_records.append(user)
#         # response = {
#         #     'shouts': shoutsList
#         # }
#         # print(response)
#         return jsonify({'shouts': {'textdata': 'Somthing is there '}})


# @app.route('/instance/media/SaveFile', methods=['GET', 'POST'])
# def SaveFile():
#
#     if request.method == 'POST':
#         file = request.files['uploadedFile']
#         file_name = file.save(os.path.join(UPLOAD_FOLDER, secure_filename(file.name)))
#         return jsonify(file_name)

# @app.route('/users', methods=['GET'])
# def get_all_users():

#     users = Users.query.all()
#     result = []
#     for user in users:
#         user_data = {}
#         user_data['public_id'] = user.public_id
#         user_data['username'] = user.username
#         user_data['password'] = user.password

#         result.append(user_data)

#     return jsonify({'users': result})



