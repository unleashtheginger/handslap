import os

from flask import Flask, request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'handslap.sqlite'),
    )

    @app.route('/')
    def index():
        return f'This is {request.url_root} '


    return app
