"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")
firstMember = {"id": jackson_family._generateId(),
               "firstname": "John",
               "lastname": jackson_family.last_name,
               "age": 33,
               "luckyNumbers": [7, 13, 22]}
Secondmember = {"id": jackson_family._generateId(),
                "firstname": "Jane",
                "lastname": jackson_family.last_name,
                "age": 35,
                "luckyNumbers": [10, 14, 3]}
ThirdMember = {"id": jackson_family._generateId(),
               "firstname": "Jimmy",
               "lastname": jackson_family.last_name,
               "age": 5,
               "luckyNumbers": [1]}
jackson_family.add_member(firstMember)
jackson_family.add_member(Secondmember)
jackson_family.add_member(ThirdMember)

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_hello():
    members = FamilyStructure.get_all_members(jackson_family)
    response_body = {
        "result": True,
        "family": members
    }
    return jsonify(response_body), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member is None:
        return "member not found", 404
    result = {
        "id": member_id,
        "result": True,
        "status": 200,
        
    }
    return jsonify(result), 200

@app.route('/member', methods=['POST'])
def add_member():

    member = request.get_json() 
  
    if member["age"] <= 0:
        return jsonify({"menssage":"wrong age"}), 404
    if member["id"] is None:
        member["id"] = jackson_family._generateId()
    memberFamily = { 
            "id" : member["id"],
            "firstname" :member["firstname"], 
            "age" : member["age"], 
            "luckyNumbers": member["luckyNumbers"]
            }
    new_member = jackson_family.add_member(memberFamily)

    return jsonify(new_member), 200    

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = jackson_family.delete_member(member_id)
    if member is None:
        return "member not found", 404
    result = {
        "id": member_id,
        "result": True,
        "status": 200,
        "mensaje": "member remove"
    }
    return jsonify(result), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
