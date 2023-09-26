from urllib import request
from flask import Blueprint, render_template, request, flash
import os

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'weby'

cestaKeSlozece = r"path...." #Change variable cestaKeSložce to your patho to that folther.

e = "newMember@gmail.com"
p = "123"


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route("/", methods=["GET","POST"])
def home():

    if request.method == "POST": #při post metodě
        return render_template("main.html", text="login")
    return render_template("home.html", text="login")

    
if(__name__ == "__main__"):
    app.run(debug=True)