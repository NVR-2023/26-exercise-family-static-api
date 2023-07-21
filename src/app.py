"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""

import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
from random import randint

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure("Jackson")

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# GET all family members

@app.route('/getallmembers', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    if not members:
        return jsonify({"message": "No family members found"}), 404
    return jsonify(members), 200


# GET specific family member by ID

@app.route('/getmember/<int:id>', methods=['GET'])
def get_member(id):
    member = jackson_family.get_member(id)
    if member is None:
        return jsonify({"message": "Member not found"}), 404
    return jsonify(member), 200


# POST new family member

@app.route('/addmember', methods=['POST'])
def add_member():
    member_data = request.get_json()
    if member_data is None:
        return jsonify({"message": "Void request"}), 400

    response = jackson_family.add_member(member_data)
    if not response:
        return jsonify({"message": "Could not add member"}), 400
    return jsonify({"message": "New member added successfully"}), 200


# DELETE a family member by ID

@app.route('/deletemember/<int:id>', methods=['DELETE'])
def delete_member(id):
    response = jackson_family.delete_member(id)
    if not response:
        return jsonify({"message": "Member not found"}), 404
    return jsonify({"message": "Member successfully deleted"}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
