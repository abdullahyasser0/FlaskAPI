from flask import Flask, request,jsonify

TOKEN = "mytoken12"

def authenticate_token():
    token = request.headers.get("Authorization")
    if not token or token !=f"Bearer {TOKEN}":
        return jsonify({"error ": "Unothorized "}),401    