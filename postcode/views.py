import http

from flask import jsonify, request

from .logger import logger
from .models import UKPostcode


def postcode():
    postcode = request.args.get('postcode', default = '', type = str)

    logger.info(f'Validating UK Postcode: {postcode} ...')
    try:
        uk_postcode = UKPostcode(postcode)
        data = {
            "postcode": str(uk_postcode)
        }
        logger.info(f'Valid UK Postcode')
        return jsonify({'data':data, 'msg':"Valid UK Postcode"}), http.HTTPStatus.OK

    except Exception as e:
        data = {
            "error": str(e)
        }
        logger.info(f'Invalid UK Postcode')
        return jsonify({'data':data, 'msg':"Invalid UK Postcode"}), http.HTTPStatus.BAD_REQUEST

def healthcheck():
    return jsonify({"status": "OK"}), http.HTTPStatus.OK
