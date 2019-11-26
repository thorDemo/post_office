# -*- coding:utf-8 -*-
from flask import Flask, request, jsonify, Response
from mylib.smtp_socket import SMTPSocket
import os
import json


# Flask对象
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


def response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/post/office/', methods=['POST'])
def post_email():
    if request.method == 'POST':
        data = request.form
        sender = data['sender']
        receivers = data['receivers']
        message = data['message']
        service = SMTPSocket()
        status, code, msg = service.send_mail(sender, receivers, message)
        result = {
            'code': code,
            'msg': msg
        }
        return jsonify(result)
    else:
        content = json.dumps({"error_code": "1001"})
        resp = response_headers(content)
        return resp


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )