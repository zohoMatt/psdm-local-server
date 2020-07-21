from flask import Blueprint

fit_app = Blueprint('fit_router', __name__)


@fit_app.route('/test')
def test():
    return {
        'tested': True
    }
