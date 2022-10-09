from flask import jsonify


def base_service(controller):
    size, error = controller
    response = size if not error else {'error': error}
    status_code = 200 if size else 404 if not error else 400
    return jsonify(response), status_code


