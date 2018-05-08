# chips/__init__.py

from flask import Flask
import config
from cloud_storage import FileStorage

file_storage = FileStorage()


def create_app():
    app = Flask(__name__)
    app.config.update(dict(
        SECRET_KEY="asjkfhwhfwihfkajsdf1294235r4r",
        WTF_CSRF_SECRET_KEY="sadjkfhiuyhgbnvcnbcnb0385jgmdnbkdjn"
    ))

    return app
