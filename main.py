from flask_login import login_user, current_user
from flask import Blueprint, request, json
import bcrypt
import re
from database import USER_DATA, save_user, get_user

main = Blueprint('main', __name__)


@main.route('/register', methods=['POST'])
def register_account():
    if request.method == 'POST':
        if request.data is not None:
            body_json = json.loads(request.data)
            if USER_DATA.find_one({'username': str(body_json['username']).lower()}) is None:
                if len(str(body_json['username'])) >= 5:
                    if re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",
                                str(body_json['password'])) is not None:
                        save_user(str(body_json['username']).lower(), str(body_json['password']).encode('utf-8'))
                        return "Registered Successfully!"
                    else:
                        return "Password must contain minimum 8 characters with at least one Uppercase, one Lowercase, one Number, and one Special Character!"
                else:
                    return "Username must contain minimum 5 characters!"
            else:
                return "Username already exists!"
        else:
            return "Please enter required the Data correctly!"


@main.route('/login', methods=['POST'])
def account_login():
    if request.method == 'POST':
        body_json = json.loads(request.data)
        user_data = get_user(str(body_json['username']).lower())
        if user_data is not None:
            if bcrypt.checkpw(str(body_json['password']).encode('utf-8'), user_data.password_hash):
                login_user(user_data)
                return f"Logged in Successfully as {current_user.get_id()} !"
            else:
                return "Wrong Password. Try Again!"
        else:
            return "Account does not exist!"
