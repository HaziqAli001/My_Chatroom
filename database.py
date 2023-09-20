import bcrypt
from pymongo import MongoClient
from user import User

client = MongoClient('mongodb://localhost:27017')
database = client['Chat_Application']
USER_DATA = database['UserData']
CHATROOM_DATA = database['ChatroomData']
MESSAGE_DATA = database['MessageData']


def save_user(username, password_bytes):
    salt = bcrypt.gensalt()
    user_data = {'_id': len(list(USER_DATA.find({}))) + 1,
                 'username': username,
                 'password_hash': bcrypt.hashpw(password_bytes, salt)}
    USER_DATA.insert_one(user_data)


def get_user(username):
    user_data = USER_DATA.find_one({'username': str(username).lower()})
    return User(user_data['_id'], user_data['username'], user_data['password_hash']) if user_data else None
