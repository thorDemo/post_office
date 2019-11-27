# -*- coding:utf-8 -*-
from flask import Flask, request, jsonify, Response
from mylib.smtp_socket import SMTPSocket
from mylib.real_ip import real_ip
from mylib.code_logging import Logger
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
        code, msg = service.send_mail(sender, receivers, message)
        result = {
            'code': code,
            'msg': msg
        }
        logging = Logger('send_email.log').get_log()
        logging.info(f'{receivers} {code} {msg}')
        return jsonify(result)
    else:
        content = json.dumps({"error_code": "1001"})
        resp = response_headers(content)
        return resp


if __name__ == '__main__':
    app.run(
        host=real_ip(),
        port=5000,
        debug=True
    )
