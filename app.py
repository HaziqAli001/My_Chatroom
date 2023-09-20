import requests
from flask_socketio import SocketIO

from flask import Flask
from database import get_user
from main import main as main_blueprint
from auth import auth as auth_blueprint
from flask_login import LoginManager


login_manager = LoginManager()
app = Flask(__name__)
login_manager.init_app(app)
socketio = SocketIO(app)
socketio.init_app(app)
login_manager.login_view = 'main.account_login'
app.secret_key = 'my secret key'

app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)


@login_manager.user_loader
def load_user(username):
    return get_user(username)


@socketio.on('message')
def message(data):
    text = data['text']
    room_id = data['room_id']
    response = requests.post(f'http://127.0.0.1:5000/chat/rooms/{room_id}/messages', data={'text': text})
    return response.json()


if __name__ == '__main__':
    app.run()
    socketio.run(app)
