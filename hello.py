from flask import Flask, render_template

app = Flask("MyApp")

#import random
@app.route("/idoexist")
def idoexist():
    return "I do exist now!"


@app.route("/fionnewpage")
def mypage():
    return "this is my new page"

app.run(debug=True)
