import os

from flask import Flask, render_template, request
from handslap.db import get_db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    from . import db
    db.init_app(app)

    app.config.from_mapping(
        SECRET_KEY='obviously_change_this',
        DATABASE=os.path.join(app.instance_path, 'handslap.sqlite'),
    )

    @app.route('/')
    def index():
        db = get_db()
        error = None

        result = db.execute(
            'SELECT hits from sites where url_root = ?',
            (request.url_root,)
        ) # I should validate url_root really

        site_hits = result.fetchone()
        if site_hits is None:
            site_hits = 0
            db.execute(
                'INSERT INTO sites (url_root, hits) VALUES (?, ?)',
                (request.url_root, site_hits)
            )
            db.commit()
        else:
            site_hits = site_hits['hits']

        site_hits = site_hits + 1

        db.execute(
            'UPDATE sites SET hits = (?) WHERE url_root = (?)',
            (site_hits, request.url_root))
        db.commit()

        return render_template('index.html', url=request.url_root, site_hits=site_hits)


    return app
