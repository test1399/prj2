from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import sys
	
app = Flask(__name__)
app.config['SECRET_KEY'] = "dfbtnbcdsdferbngfsade"
socketio = SocketIO(app)
channels = ["sample"]
messages = []

@app.route("/")
def index():
	return render_template("index.html")

@socketio.on("create channel")
def create(data):
	channel = data['channel']
	if channel not in channels:
		channels.append( channel )
		emit("channel added", {"channel": channel }, broadcast=True )

@socketio.on("load")
def load():
	print("get aaaaaaaaaaaaaaaaaaaaaaaaaaa", file=sys.stderr)
	emit("load channels", channels, broadcast=True )
	emit("load panel", messages, broadcast=True)

@socketio.on("send msg")
def sendMsg(data):
	msg = data['msg']
	messages.append(msg)
	emit("update panel", {"msg":msg}, broadcast=True)


