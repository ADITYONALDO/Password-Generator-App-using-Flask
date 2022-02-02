from flask import Flask, render_template, request
from random import randrange
from flask_mail import Mail, Message

app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] = ""			# please enter the e-mail id in oreder to send the password ( enter another email id, do not enter the e-mail id where you will receive the passowrd) 
app.config["MAIL_PASSWORD"] = ""			# enter the passowrd for the e-mail id entered above
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False

mail = Mail(app)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/gen", methods = ["POST"])
def gen():
	em = request.form["em"]
	le = int(request.form["length"])
	pw = ""
	text = "abcdefghijklmnopqrstuvwxyz"
	if request.form.get("uc"):
		text = text + text.upper()
	if request.form.get("di"):
		text = text + "0123456789"

	for i in range(le):
		pw = pw + text[randrange(len(text))]

	msg = Message("PG App has something for you" , sender = "", recipients = [em])				# use the same e-mail used in "MAIL_USERNAME" in sender
	msg.body = "Your Passowrd is " + str(pw)
	mail.send(msg)
	return render_template("home.html", msg = pw)

if __name__ == "__main__":
	app.run(debug = True, use_reloader = True)
