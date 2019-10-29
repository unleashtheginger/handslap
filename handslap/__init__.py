import os

from flask import Flask, render_template, request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'handslap.sqlite'),
    )

    @app.route('/')
    def index():
        return render_template('index.html', url=request.url_root, client_ip=request.remote_addr)
        # return f'This is {request.url_root} '


    return app
