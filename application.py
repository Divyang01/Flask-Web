from flask import Flask, render_template

import datetime

app = Flask(__name__)

@app.route("/")
def index():
	now = datetime.datetime.now()
	new_year = now.day == 1 and now.month == 1
	#new_year = True
	#headline = "hello world"
	lists = ["alice","bob","charlies","devid"]
	return render_template("hello.html",new_year = new_year,list = lists)

@app.route("/second")
def second():
	return render_template("second.html")

@app.route("/<string:name>")
def hello(name):
	return f"Hello,{name}!"