import base64

ADMIN_PASSWORD = 'QURNSU4yNjI3Q09PTA=='


def sycol(encoded_str):
    decoded_bytes = base64.b64decode(encoded_str)
    decoded_str = decoded_bytes.decode("utf-8")
    return decoded_str


def check_admin_password(password):
    return password == sycol(ADMIN_PASSWORD)
