from flask import jsonify


def base_service(controller):
    data, error = controller
    response = data if not error else {'error': error}
    status_code = 200 if data else 404 if not error else 400
    return jsonify(response), status_code


