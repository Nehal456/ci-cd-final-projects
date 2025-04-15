from flask import Blueprint, jsonify
from service.common.status import HTTPStatus

counters_blueprint = Blueprint('counters', __name__)
counters = {}  # Simple in-memory storage

@counters_blueprint.route('/')
def index():
    return jsonify({"message": "Welcome to the Counter API"}), HTTPStatus.OK

@counters_blueprint.route('/health')
def health():
    return jsonify({"status": "OK"}), HTTPStatus.OK

@counters_blueprint.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    counters[name] = 0
    return jsonify({"name": name, "counter": 0}), HTTPStatus.CREATED

@counters_blueprint.route('/counters', methods=['GET'])
def list_counters():
    return jsonify(counters), HTTPStatus.OK

@counters_blueprint.route('/counters/<name>', methods=['GET'])
def read_counter(name):
    if name not in counters:
        return jsonify({"error": "Counter not found"}), HTTPStatus.NOT_FOUND
    return jsonify({"name": name, "counter": counters[name]}), HTTPStatus.OK

@counters_blueprint.route('/counters/<name>', methods=['PUT'])
def update_counter(name):
    if name not in counters:
        return jsonify({"error": "Counter not found"}), HTTPStatus.NOT_FOUND
    counters[name] += 1
    return jsonify({"name": name, "counter": counters[name]}), HTTPStatus.OK

@counters_blueprint.route('/counters/<name>', methods=['DELETE'])
def delete_counter(name):
    if name not in counters:
        return jsonify({"error": "Counter not found"}), HTTPStatus.NOT_FOUND
    del counters[name]
    return '', HTTPStatus.NO_CONTENT
