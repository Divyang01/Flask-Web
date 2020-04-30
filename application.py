from flask import Flask, render_template, request, session
from flask_session import Session

import datetime

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

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

	if session.get('notes') is None:
		session["notes"] = []	
	if request.method == 'POST':	
		name = request.form.get('name')

		note = request.form.get('note')
		session["notes"].append(note)
		return render_template("hello.html",name=name,notes=session["notes"])	

@app.route("/<string:name>")
def hi(name):
	return f"Hello,{name}!"