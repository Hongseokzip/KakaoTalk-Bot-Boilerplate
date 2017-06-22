# -*- coding: utf-8 -*-

from flask_restful import Resource


# Initialize API
class Keyboard(Resource):
    def get(self):
        return {'type': 'text'}
