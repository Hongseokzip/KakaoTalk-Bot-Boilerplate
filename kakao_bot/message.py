# -*- coding: utf-8 -*-

from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()

parser.add_argument('user_key')
parser.add_argument('type')
parser.add_argument('content')


def do_something(data):
    return 'https://lh3.googleusercontent.com/qKP2GDGUt83LnugU2ddVaPvE8L9uiJv-DP6G-ACkUsbX10cBWqTKxOJNcteQtnDTWE-Nnqc' \
           'KFxpdezxFcnmlr8o0ivlb6jbuc9D0satAYgcHMeaVcDEkEg_dwVH_etxmoSeImVM0Aprwq-fyP18Q8yz0RydkNY6izDai-_y6dbSwoifb' \
           'zBxJl53nIPNA2gKQFuFPXMYXb7KF6xWEMiQLO1YVT3QRbKqFIjnHwSBcm2uIwR2OOLL7Q7ZsE7U7UfNpNrlKMsZWbs3X0Zwe-le6Z04yq' \
           'Td5BFvUN7HOQtoI_GYxRKkh8Vs950pNzHvH2l_SlULVkeTvresxDgbkIb1vOuUs8S-6XXJUOJ18b-cgRlW4yujQixDD-bLQlDCwr-MQ6v' \
           'ma5cIaQp4AwrjsGdspncVkm9tssiLsT_nn4_akcr93joDuMlnVV9Rg_zUErNO6nuetq2wgyWPNolp66oUs5qPL8VUabxjnGaZpj5_I0wF' \
           'eXIOAnsLL3OH2bQizS9zd4dmYYGkMYojeJQQhBb1XMhvfgvrCzIN2VJVtXAyFlBVIx5QT3XBG0NjYdQjw8tAie0Mto3fEuHvzJB97tUIg' \
           'aFgKib4uLTIyb3NAOr4Ep8jZcLjD7NeR3Dg7BRfZ1fimSfBwU2V5MRwaHCaLAtX4fxCIbq--xihyRZ1wbQbbmQ=w1140-h1518-no'


# Auto Reply Message API
class Message(Resource):
    def post(self):
        args = parser.parse_args()
        resp = {
            'message': {
                'photo': {
                    'url': do_something(args['content']),
                    "width": 480,
                    "height": 640
                }
            }
        }
        print resp
        return resp, 200
