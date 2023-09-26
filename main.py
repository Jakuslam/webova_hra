from urllib import request
from flask import render_template, request

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired

from getQuestions import *

print(getQuestion("countries", 3))


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'weby'


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")



#webside
@app.route("/", methods=["GET","POST"])
def home():

    points = 0 
    if request.method == "POST": #when somebody push button inicialize "POST method"
        if(request.form.get("NuclearPlant")):
            
            points = 0
            questionNumber = 0
            return render_template("main.html", points = points, questionNumber = questionNumber)
        
        if(request.form.get("NuclearPlant1")):
            print(request.form.get("points"))
            if(request.form.get("points") == None):
                points = 0
                questionNumber = 0
            else:
                points = request.form.get("points")
                questionNumber = 1 + int(request.form.get("from"))
            points = int(points) + 1
            print(points)
            return render_template("main.html", points = points, questionNumber = questionNumber )
            
        if(request.form.get("NuclearPlant2")):
            if(request.form.get("points") == None):
                points = 0
                questionNumber = 0
            else:
                points = request.form.get("points")
                questionNumber = 1 + int(request.form.get("from"))
            print(points)
            return render_template("main.html", points = points, questionNumber = questionNumber)
        

    return render_template("home.html")

    
if(__name__ == "__main__"):
    app.run(debug=True)