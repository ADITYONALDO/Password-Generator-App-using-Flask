from flask import Flask, render_template, request
from random import randrange
from flask_mail import Mail, Message

app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] = "tester.adityaa@gmail.com"
app.config["MAIL_PASSWORD"] = "tester@123"
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

	msg = Message("PG App has something for you" , sender = "tester.adityaa@gmail.com", recipients = [em])
	msg.body = "Your Passowrd is " + str(pw)
	mail.send(msg)
	return render_template("home.html", msg = pw)

if __name__ == "__main__":
	app.run(debug = True, use_reloader = True)