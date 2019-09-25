from flask import Flask
from flask import send_file
import json
app = Flask(__name__)
CURRENT_VERSION = 2
newest_version_dir = 'newest/newest.bin'
@app.route('/update/<version>')
def update(version:int):
    if (int(version) < CURRENT_VERSION):
        return '1'
    else:
        return '0'

@app.route("/update/get")
def get_update():
    return send_file("newest.bin")

@app.route("/")
def index():
    return "Changelog:"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
