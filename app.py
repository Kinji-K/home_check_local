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

@app.route("/sleep")
def sleep():
    drive = DriveUpload("sleep.txt")
    drive.FileUpload()
    return "sleep"

@app.route("/wakeup")
def wakeup():
    drive = DriveUpload("sleep.txt")
    drive.FileDelete()
    return "wake_up"

@app.route("/get")
def get_status():
    drive = DriveUpload("out.txt")
    status = drive.CheckOut()
    return str(status)

@app.route("/sleep_check")
def get_sleep_status():
    drive = DriveUpload("sleep.txt")
    status = drive.CheckOut()
    return str(status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5555)