# -*- coding: utf-8 -*-

import logging

from flask import Blueprint
from flask_restful import Api

from chat_room import Chatroom
from friend import Friend
from keyboard import Keyboard
from message import Message

kakao_bot = Blueprint('kakao_bot', __name__)
api = Api(kakao_bot)

# resource map
api.add_resource(Chatroom, '/chat_room/<user_key>')
api.add_resource(Friend, '/friend', '/friend/<user_key>')
api.add_resource(Keyboard, '/keyboard')
api.add_resource(Message, '/message')


@kakao_bot.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request. %s' % str(e))
    return 'An internal error occurred.', 500
