from flask import Flask, request,jsonify, Blueprint
from middleware.auth import authenticate_token


todos_bp = Blueprint("modelslist",__name__)

modelslist = []


@todos_bp.before_request
def before_request():
    return authenticate_token()


@todos_bp.route("/",methods=["GET"])
def get_todos():
    return jsonify(modelslist)


@todos_bp.route("/",methods=["POST"])
def create_todo():
    list = {
        "id": len(modelslist)+1,
        "model" : request.json.get("model"),
        "available" : request.json.get("available",False),
    }
    modelslist.append(list)
    return jsonify(list),201


@todos_bp.route("/<int:id>",methods=["PUT"])
def update_todo(id):
    car = next((t for t in modelslist if t.get("id")==id),None)
    if car is None:
        return jsonify({"error" : "car not fount"}),404
    car["model"] = request.json.get("model", car["model"])
    car["available"] = request.json.get("available", car["available"])
    return jsonify(car)


@todos_bp.route("/<int:id>",methods=["DELETE"])
def delete_todo(id):
    global modelslist
    car = next((t for t in modelslist if t.get("id") == id), None)
    if car is None:
        return jsonify({"error": "Model not found"}), 404
    
    modelslist = [t for t in modelslist if t.get("id") != id]
    return '', 204


@todos_bp.route("/<int:id>",methods=["GET"])
def get_by_id(id):
    car = next((c for c in modelslist if c.get("id")==id),None)
    if car:
        return jsonify(car)
    return jsonify({"error" : "Not found "}),404



