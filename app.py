from flask import Flask, render_template,request,redirect,url_for
from pymongo import MongoClient as mongoDB
import os

app = Flask(__name__)
title = "Team-Management"
heading = "Team-Management App"

#client = MongoClient("mongodb://127.0.0.1:27017")
client = mongoDB(os.environ['host-0f-mongo'], 27017)
db = client.mymongodb
mycol = db.todo

@app.route("/")
@app.route("/list")
def lists ():
	return render_template('index.html', a1 = "active", mycol = mycol.find(), t = title, h = heading)

@app.route("/action1", methods=['POST'])
def action1 ():
	mycol.insert({ "name" : request.values.get("name"), "email" : request.values.get("email"), "date" : request.values.get("date"), "pr" : request.values.get("pr")})
	return redirect("/list")

@app.route("/action2", methods=['POST'])
def action2 ():
	data = {"email" : request.values.get("email")}
	new_data = {'$set' : {"name" : request.values.get("name"), "email" : request.values.get("email"), "date" : request.values.get("date"), "pr" : request.values.get("pr")}}
	mycol.update(data, new_data)
	return redirect("/list")

@app.route("/action3", methods=['POST'])
def action3 ():
	email = request.values.get("email")
	mycol.delete_one({"email" : email})
	return redirect("/list")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
