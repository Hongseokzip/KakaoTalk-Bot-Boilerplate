# -*- coding: utf-8 -*-

from flask_restful import Resource


# Chat room leave API
class Chatroom(Resource):
    def delete(self, user_key):
        print "Friend (%s) leave chat room" % user_key
        return {'code': 0, 'message': 'SUCCESS'}, 200
