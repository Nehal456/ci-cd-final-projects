from flask import Blueprint, jsonify
from service.common.status import HTTPStatus

# Initialize blueprint
bp = Blueprint('counters', __name__, url_prefix='/api')

# Initialize counters dictionary
counters = {}

@bp.route('/')
def index():
    return jsonify({"message": "Welcome to the Counter API"}), HTTPStatus.OK

@bp.route('/health')
def health():
    return jsonify({"status": "OK"}), HTTPStatus.OK

@bp.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    counters[name] = 0
    return jsonify({"name": name, "counter": 0}), HTTPStatus.CREATED

@bp.route('/counters', methods=['GET'])
def list_counters():
    return jsonify(counters), HTTPStatus.OK

@bp.route('/counters/<name>', methods=['GET'])
def read_counter(name):
    if name not in counters:
        return jsonify({"error": "Counter not found"}), HTTPStatus.NOT_FOUND
    return jsonify({"name": name, "counter": counters[name]}), HTTPStatus.OK

@bp.route('/counters/<name>', methods=['PUT'])
def update_counter(name):
    if name not in counters:
        return jsonify({"error": "Counter not found"}), HTTPStatus.NOT_FOUND
    counters[name] += 1
    return jsonify({"name": name, "counter": counters[name]}), HTTPStatus.OK

@bp.route('/counters/<name>', methods=['DELETE'])
def delete_counter(name):
    if name not in counters:
        return jsonify({"error": "Counter not found"}), HTTPStatus.NOT_FOUND
    del counters[name]
    return '', HTTPStatus.NO_CONTENT
