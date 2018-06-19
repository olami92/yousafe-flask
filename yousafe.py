import sqlite3 as sql
from flask import Flask
from flask import render_template
from flask import request
from twilio import twiml
from twilio.rest import Client


app = Flask(__name__, template_folder='Template')


def retrieveUsers():
    con = sql.connect("yousafe.db")
    cur = con.cursor()
    cur.execute("SELECT *FROM userinfo WHERE password =password")
    users = cur.fetchall()
	#con.close()
    if users:
        for i in users:
            
            a = '+'
            number = str(+i[5])
            to_number = a+number
            account_sid = "AC86abac3ecb05959242a541ede81db498"
            auth_token = "21e4b50f5931f547b5726ef61c1bd542"
            twilio_number = "+14243696153 "
            body = "hi"
            client = Client(account_sid, auth_token)
            client.api.messages.create(to = to_number,
                           from_=twilio_number,
                           body=body)
    return ("Welcome"" " +i[3])

@app.route('/', methods=['POST', 'GET'])
def home():
    users = None
    if request.method=='POST':
  
     password = request.form['Code']
   	#dbHandler.insertUser(username, password)
     users = (retrieveUsers())
     #send_sms(to_number, body)
    return render_template('login.html',users=users)
    #else:
      #return render_template('index.html')



if __name__ == '__main__':
    app.run(port=5000, debug=True)
