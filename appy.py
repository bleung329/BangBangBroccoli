from flask import Flask, session, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

#Where you login.
@app.route("/")
def landing():
	return redirect(url_for('login'))

@app.route("/login")
def login(message = ""):

	if "submit" in request.args:
		if request.args["submit"] == "Logout":
			session["username"] = ""
			print "fired!"
			return redirect(url_for('login', message = "You logged out."))
	if "username" in session:
		if session["username"] == "user!":
			return redirect(url_for('logged', username = "user!"))
	username = ""
	password = ""

	if "user" in request.args and "passo" in request.args:
		username = request.args["user"].lower()
		password = request.args["passo"]

	if username != "":		
		if username == "user!":
			if password == "password":
				return redirect(url_for('logged', username = "user!"))
			else:
				return redirect(url_for('login', message = "Bad password!"))
		else:
			return redirect(url_for('login', message = "Bad username!"))

	if "message" in request.args:
		print "other message: " +request.args["message"]
		message = request.args["message"]

	return render_template("loginpage.html", message = message)

	render_template()
@app.route("/logged")
def logged(username = ""):
	print "loud and clear"
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