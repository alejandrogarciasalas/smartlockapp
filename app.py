import bandwidth
from flask import Flask, render_template

u-user = ''
t-token = ''
s-secret = ''

messaging_api = bandwidth.client('messaging', u-user, t-token, s-secret)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route("/unlock/")
def unlock():
	message_id = messaging_api.send_message(
	  from_ = '+15104377024',
	  to    = '+163316',
	  text  = 'S4RJQJ')
	print(message_id)
	message_id = messaging_api.send_message(
	  from_ = '+15104377024',
	  to    = '+163316',
	  text  = '1')
	print(message_id)
	return "unlock"
