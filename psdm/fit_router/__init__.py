from flask import Blueprint, request
from psdm.fit_router.psdm_fit import psdm_kfit

fit_app = Blueprint('fit_router', __name__)


@fit_app.route('/test')
def test():
    return {
        'args': {k: v for k, v in request.args.items()}
    }


@fit_app.route('/kfit')
def kfit():
    fit_curve = psdm_kfit(**{k: v for k, v in request.args.items()})
    params, x, y = fit_curve['params'], fit_curve['index'], fit_curve['values']
    return {
        'x': x,
        'y': y,
        'length': len(x),
        'valid': len(x) == len(y),
        'params': params,
        'msg': ''
    }
