import base64


def encode_header(string, email):
    s = string.encode('utf-8')
    return f'=?UTF-8?B?{str(base64.b64encode(s), encoding="utf-8")}?= <{email}>'
