from flask import abort, Flask, jsonify, request
from Drive import DriveUpload
import requests
import json
import os

app = Flask(__name__)

@app.route("/")
def go_test():
    return "hello"

@app.route("/out")
def go_out():
    drive = DriveUpload("out.txt")
    drive.FileUpload()
    return "hello"

@app.route("/in")
def go_in():
    drive = DriveUpload("out.txt")
    drive.FileDelete()
    return "hello"

@app.route("/get")
def get_status():
    drive = DriveUpload("out.txt")
    status = drive.CheckOut()
    return str(status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5555)