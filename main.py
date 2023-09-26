from urllib import request
from flask import render_template, request

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'weby'


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")





#webside
@app.route("/", methods=["GET","POST"])
def home():

    if request.method == "POST": #when somebody push button inicialize "POST method"
        if(request.form.get("NuclearPlant")):
            return render_template("main.html")
        
        
    return render_template("home.html")

    
if(__name__ == "__main__"):
    app.run(debug=True)