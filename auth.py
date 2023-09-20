import datetime
import json
from flask import Blueprint, redirect, url_for, request
from flask_login import logout_user, login_required, current_user
from database import CHATROOM_DATA, MESSAGE_DATA


auth = Blueprint('auth', __name__)


@auth.route('/logout', methods=['POST'])
@login_required
def account_logout():
    logout_user()
    redirect(url_for('main.account_login'))
    return f" Logged out Successfully!"


@auth.route('/chat/rooms', methods=['GET'])
@login_required
def chatroom_list():
    if request.method == 'GET':
        chat_rooms = list(CHATROOM_DATA.find({}))
        if len(chat_rooms) > 0:
            return chat_rooms
        else:
            return "No Chatroom found!"


@auth.route('/chat/rooms/<int:id>', methods=['GET'])
@login_required
def chatroom_details(id):
    if request.method == 'GET':
        chatroom_detail = CHATROOM_DATA.find_one({'_id': id})
        if chatroom_detail is not None:
            if current_user.get_id() in list(chatroom_detail.get('users')):
                return chatroom_detail
            else:
                return "You are not authorized to view detail!"
        else:
            return "Chatroom does not exist!"


@auth.route('/chat/rooms/<int:id>/messages', methods=['GET'])
@login_required
def chatroom_messages(id):
    if request.method == 'GET':
        chatroom = CHATROOM_DATA.find_one({'_id': id})
        if chatroom:
            if current_user.get_id() in list(chatroom.get('users')):
                chatroom_message_list = list(MESSAGE_DATA.find({'room_id': id}).sort('created_at'))
                if len(chatroom_message_list) > 0:

                    return chatroom_message_list
                else:
                    return "No messages found!"
            else:
                return "Only room members can view messages!"
        else:
            return "Chatroom does not exist!"


@auth.route('/chat/rooms/<int:id>/messages', methods=['POST'])
@login_required
def send_message(id):
    if request.method == 'POST':
        chatroom = CHATROOM_DATA.find_one({'_id': id})
        if chatroom:
            if current_user.get_id() in list(chatroom.get('users')):
                message_text = str(json.loads(request.data)['text'])
                if len(message_text) > 0:
                    message = {'_id': len(list(MESSAGE_DATA.find({}))) + 1,
                               'text': message_text,
                               'sender_id': current_user.get_id(),
                               'room_id': id,
                               'created_at': datetime.datetime.now()}
                    MESSAGE_DATA.insert_one(message)
                    #emit('new_message', {'sender': current_user.get_id(), 'text': message_text}, room=id)

                    return "Message Sent!"
                else:
                    return "Cannot send empty message!"
            else:
                return "Only room members can send messages!"
        else:
            return "Chatroom does not exist!"





