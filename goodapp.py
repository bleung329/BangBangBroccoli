'''
Adam Abbas
&
Brian Leung

PD 7 Softdev
HW07
'''
#Just imports
from flask import Flask, session, render_template, request, redirect, url_for
import os

#App instantiation
app = Flask(__name__)
app.secret_key = os.urandom(32)

#Where you login.
@app.route("/")
def landing():
	
	#This part checks if you tried logging out
	try:
		if request.args["submit"] == "Logout":
			session["username"] = ""
	except:
		pass
	
	#This part checks if your browser stored your username
	if ("username" in session) and session["username"] != "":
			print "Theres something in username!"
			print session["username"]
			print url_for(logged(session["username"]))
			print "the above ran!"
			print url_for(logged())
			print redirect("http://localhost:5000"+url_for(logged()))
	
	#Else, they just give you the login page.
	else:
		return render_template("loginpage.html")

#Where all the fun login stuff happens
@app.route("/loggit")
def logged(user = ""):

	#This part checks if your user+pw is correct.
	if user == "":
		username = request.args["user"].lower()
		password = request.args["passo"]
		if username == "wada":
			if password == "Zucchini":
				session["username"] = "wada"
				return render_template("ushallpass.html", username = "wada")
			else:
				return render_template("errorpage.html", bad = "password")
		else:
			return render_template("errorpage.html", bad = "username")

	#If you already have a username, it brings you here
	else:
		return render_template("ushallpass.html", username = session["username"])

if __name__ == "__main__":
    app.debug = True
    app.run()
