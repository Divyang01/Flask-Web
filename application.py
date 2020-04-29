from flask import Flask, render_template, request

import datetime

app = Flask(__name__)

@app.route("/")
def index():
	now = datetime.datetime.now()
	new_year = now.day == 1 and now.month == 1
	#new_year = True
	#headline = "hello world"
	lists = ["alice","bob","charlies","devid"]
	return render_template("index.html",new_year = new_year,list = lists)

@app.route("/second")
def second():
	return render_template("second.html")

@app.route("/hello",methods=["GET","POST"])
def hello():
	if request.method == "GET":
		return "Please submit the form instead."
	else:	
		name = request.form.get('name')
		return render_template("hello.html",name=name)	

@app.route("/<string:name>")
def hi(name):
	return f"Hello,{name}!"