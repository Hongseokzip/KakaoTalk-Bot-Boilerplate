# -*- coding: utf-8 -*-

from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()

parser.add_argument('user_key')


# Friend add, block API
class Friend(Resource):
    def post(self):
        args = parser.parse_args()
        print "Friend (%s) added" % args['user_key']
        return {'code': 0, 'message': 'SUCCESS'}, 200

    def delete(self, user_key):
        print "Friend (%s) deleted" % user_key
        return {'code': 0, 'message': 'SUCCESS'}, 200
