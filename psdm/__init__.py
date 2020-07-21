from flask import Flask
from psdm.fit_router import fit_app
from psdm.fetch import download_repo_files


def create_app():
    app = Flask(__name__)

    # Register routers
    app.register_blueprint(fit_app)

    @app.before_first_request
    def initialize():
        download_repo_files()

    return app
