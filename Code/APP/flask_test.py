from flask import Flask,render_template,url_for,redirect, request
import os
from speech_rec import speech_rec
from connection_test import connectionRasp

ip_rasp = '192.168.1.145'

app = Flask(__name__)

#save order at app
app.order = False

@app.route("/")
def init():
    CR = connectionRasp()
    return render_template("index2.html")

@app.route('/echoTerm')
def echoTerm():
    print('In SomeFunction')
    return "Nothing"

@app.route('/listenOrder')
def listenOrder():
    print('Listen orders')
    sp = speech_rec()
    x = sp.get_audio_data()
    print(x)
    app.order = x
    return True

@app.route("/hand_selection",methods=["GET", "POST"])
def hand_sel():
    if request.method == 'POST':
        app.order = list(request.form.keys())[:-1]
        return render_template("select_result.html", order_str=", ".join(app.order))
    return render_template("hand_sel.html")

@app.route("/voice_selection")
def voice_sel():
    if app.order:
        return render_template("select_result.html", order_str=", ".join(app.order))
    return render_template("voice_sel.html")

@app.route("/select_result")
def select_result():
    CR.comandSSH('comanda + app.order')
    return render_template("select_result.html", order_str=", ".join(app.order))

if __name__ == "__main__":
    app.run()



