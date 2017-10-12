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

#Where we store users and passwords in PLAINTEXT!!!
userpass = {"user!":"password"}

#Authenticate function!
def auth(user,passo,upass):
	'''
	stat_code -1 = bad username
	stat_code 0 = bad password
	stat_code 1 = good
	'''
	stat_code = -1
	if user in upass:
		stat_code+=1
		if passo == upass[user]:
			stat_code+=1
	return stat_code


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
		if  auth(username,password,userpass)==-1:
			flash("Bad username!")			
		if auth(username,password,userpass)==0:
			flash("Bad password!")
		if auth(username,password,userpass)==1:
			return redirect(url_for('logged', username = "user!"))

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
