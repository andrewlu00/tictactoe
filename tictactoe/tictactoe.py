from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp


app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():

	if "board" not in session:
		session["board"] = [{None, None, None}, {None, None, None}, {None, None, None}]
		session["turn"] = "X"

	return render_template("game.html", game = session["board"], turn=session["turn"])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
	session["board"][row][col] = session["turn"]
	if windetect():
		return render_template("result.html", player=session["turn"])
	else:
		session["turn"] = switch(session["turn"])
		return redirect(url_for("index"))

def windetect():
	for i in range(3):
		if session["board"][i] == {"X", "X", "X"} or session["board"][i] == {"O", "O", "O"}:
			return true
	if session["board"][0][0] == session["board"][1][0] == session["board"][2][0] and session["board"][0][0]:
		return true
	if session["board"][0][1] == session["board"][1][1] == session["board"][2][1] and session["board"][0][1]:
		return true
	if session["board"][0][2] == session["board"][1][2] == session["board"][2][2] and session["board"][0][2]:
		return true
	if session["board"][0][0] == session["board"][1][1] == session["board"][2][2] and session["board"][0][0]:
		return true
	if session["board"][0][2] == session["board"][1][1] == session["board"][2][0] and session["board"][1][1]:
		return true
	return false


def switch(a):
	if a == "X":
		return "O"
	else:
		return "X"
	
