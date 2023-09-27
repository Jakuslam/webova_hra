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
        
        if(request.form.get("NuclearPlant1") or request.form.get("NuclearPlant2")):
            whatWasPushed = 0
            if(request.form.get("NuclearPlant1")):
                whatWasPushed = 1
                if(request.form.get("points") == None):
                    points = 0
                    questionNumber = 0
                else:
                    points = request.form.get("points")
                
            if(request.form.get("NuclearPlant2")):
                whatWasPushed = 2
                if(request.form.get("points") == None):
                    points = 0
                    questionNumber = 0
                else:
                    points = request.form.get("points")

                    
            questionNumber = int(request.form.get("from"))      
            if(questionNumber + 1 >= 10):
                return render_template("home.html")
            
            dataToQuestion = getQuestion("NuclearPlant", int(questionNumber)) 
            print(dataToQuestion)
            print(whatWasPushed)
            print(dataToQuestion[3])
            if(whatWasPushed == int(dataToQuestion[3])):
                points = int(points) + 1
                print("Hello")

            questionNumber += 1
            if(questionNumber >= 10):
                return render_template("h2.html")
            
            return render_template("main.html", points = points, questionNumber = questionNumber)
        

    return render_template("h2.html")

@app.route("/game.html", methods=["GET","POST"])

def game():
    return render_template("game.html")
if(__name__ == "__main__"):
    app.run(debug=True)