from flask import Blueprint, jsonify, request

bp = Blueprint('api', __name__)

@bp.route('/grants', methods=['GET'])
def get_grants():
    # Placeholder logic
    return jsonify({"message": "List of grants"})

@bp.route('/grant', methods=['POST'])
def create_grant():
    data = request.json
    # Logic to save grant
    return jsonify({"message": "Grant created"}), 201
