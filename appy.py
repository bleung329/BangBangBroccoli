'''
Queenie Xiang
&
Brian Leung
08_login
PD 7 SoftDev

'''
from flask import Flask, session, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

#Where you login.
@app.route("/")
def landing():
	return redirect(url_for('login'))

@app.route("/login")
def login(message = ""):

    #If user hits the submit button to logout.
	if "submit" in request.args and request.args["submit"] == "Logout":
    #Reset username and redirect to the welcome logging-in page
		session["username"] = ""
		flash("You logged out")

        #If user is logged in, redirect to the logged-in page
	if "username" in session and session["username"] == "user!":
		return redirect(url_for('logged', username = "user!"))

        #Resets username and password
	username = ""
	password = ""
        #Grabs the username and password inputs from the text boxes in the welcome page
	if "user" in request.args and "passo" in request.args:
		username = request.args["user"].lower()
		password = request.args["passo"]

	if username != "":
		if  username == "user!":
			if password == "password":
        			#If all the login credentials are correct, return the logged-in page
				return redirect(url_for('logged', username = "user!"))
			else:
				flash("Bad password!")
		else:
			flash("Bad username!")
			
	return render_template("loginpage.html")


@app.route("/logged")
def logged(username = ""):
	#print "loud and clear"
	if "username" in request.args:
		username = request.args["username"]
	if username=="":
		return redirect(url_for('login'))
	else:
        	session["username"] = "user!"
		return render_template("ushallpass.html", username = username)

if __name__ == "__main__":
    app.debug = True
    app.run()
