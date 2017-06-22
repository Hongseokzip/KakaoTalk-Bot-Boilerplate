# -*- coding: utf-8 -*-

from flask import Flask

from kakao_bot import kakao_bot

app = Flask(__name__)
app.register_blueprint(kakao_bot, url_prefix="/iface")  # if url_prefix, set url_prefix parameter

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
