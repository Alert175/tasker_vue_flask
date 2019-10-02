from flask import Flask, url_for, request, jsonify, render_template
import pymongo
from pymongo import MongoClient


# init databases
client = MongoClient("localhost", 27017)
db = client["example"]


app = Flask(__name__,
			static_url_path="/public",
			static_folder="./public",
			template_folder="./public")


# main request
@app.route('/', methods=["GET"])
def get_index():
	return render_template("index.html")


# get file for vue-build
@app.route('/<path:path>', methods=["GET"])
def get_file(path):
	return app.send_static_file(path)


# run application
if __name__ == '__main__':
	app.run(debug=True)
