from urllib import request
from flask import render_template, request

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired

from getQuestions import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'weby'

#webside
@app.route("/", methods=["GET","POST"])
def home():

    return render_template("h2.html")

if(__name__ == "__main__"):
    app.run(debug=True)