#importing libraries
from urllib import request
from flask import render_template, request

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired
import jadernaEnergie
import pole
import reka as rk
import les as ls
import doly as dl
import bioOdpad as bios
import vodniElektrarna as vodA
import solarniElaktrarna as so
import vet as vt
import Skoda as skod

#setuping dlask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'weby'

body = [0,0,0,0,0,0,0,0,0,0] #variable for holding points
#webside 
@app.route("/", methods=["GET","POST"])
def home():
    return render_template("h2.html") 

@app.route("/about.html", methods=["GET","POST"])
def abought():
    return render_template("about.html")

@app.route("/achievements.html", methods=["GET","POST"])
def achievements():
    poh = [0,0,0,0] #checking if someone got all questions right
    if(body[0] == 8 and body[4] == 8 and body[5] == 8 and body[8] == 8 and body[9] == 8):
        poh[2] = 1
    if(body[1] == 8 and body[2] == 8 and body[3] == 8 and body[7] == 8):
        poh[1] = 1
    if(body[6] == 8):
        poh[0] = 1
    if(poh[0] == 1 and poh[1] == 1 and poh[2] == 1):
        poh[3] = 1
    return render_template("achievements.html", poh = poh)

@app.route("/settings.html", methods=["GET","POST"])
def settings():
    return render_template("settings.html")

@app.route("/game.html", methods=["GET","POST"])
def newGame():
    #body[0] = 8
    #body[1] = 8
    #body[2] = 8
    #body[3] = 8
    #body[4] = 8
    #body[5] = 8
    #body[6] = 8
    #body[7] = 8
    #body[8] = 8
    #body[9] = 8
    #check if is not win
    if(body[0] == 8 and body[1] == 8 and body[2] == 8 and body[3] == 8 and body[4] == 8 and body[5] == 8 and body[6] == 8 and body[7] == 8 and body[8] == 8 and body[9] == 8):
        return render_template("konec.html")
    questions = []
    i = 0
    for point in body: #if some question has 8/8 points, then it will not show it on the screen
        if(int(point) != 8):
            questions.append(i)
        else:
            questions.append(-1)
        i += 1
            
        
    return render_template("game.html", body = questions)
#rendering questions
@app.route("/jad.html", methods=["GET","POST"])
def jad():
    return render_template("jad.html", points = body[0])

@app.route("/pole.html", methods=["GET","POST"])
def pol():
    return render_template("pole.html", points = body[1])

@app.route("/bio.html", methods=["GET","POST"])
def bio():
    return render_template("bio.html", points = body[4])

@app.route("/skoda.html", methods=["GET","POST"])
def idk():
    return render_template("skoda.html", points = body[6])

@app.route("/les.html", methods=["GET","POST"])
def les():
    return render_template("les.html", points = body[3])

@app.route("/reka.html", methods=["GET","POST"])
def reka():
    return render_template("reka.html", points = body[7])

@app.route("/slun.html", methods=["GET","POST"])
def slun():
    return render_template("slun.html", points = body[5])

@app.route("/uh.html", methods=["GET","POST"])
def uh():
    return render_template("uh.html", points = body[2])

@app.route("/vet.html", methods=["GET","POST"])
def vet():
    return render_template("vet.html", points = body[9])

@app.route("/vod.html", methods=["GET","POST"])
def vod():
    return render_template("vod.html", points = body[8])

#quizz checkers
@app.route("/jadG.html", methods=["GET","POST"]) 
def jadG():
    if request.method == "POST": #if button is set
        #it gets points and questions
        points = request.form.get("points")
        questions = request.form.get("questions")
        if(points == None or questions == None):
            return render_template("jadG.html", points = 0)

        otazka = jadernaEnergie.getInfoJadro(int(questions)) #gets a question, 2 answers and wich is correct
        
        if(otazka[3] == 1 and request.form.get("a")): #checking correct answers
            points = 1 + int(points)
        elif(otazka[3] == 2 and request.form.get("b")):
            points = 1 + int(points)
        
        if int(questions) +1 >= jadernaEnergie.getLenJadro(): #if we get to last question it will return us back
            body[0] = points
            return render_template("jad.html", points = points)

        
        questions = 1 + int(questions) #incrementing question number
        otazka = jadernaEnergie.getInfoJadro(int(questions)) #get info

        return render_template("jadG.html", points = points, questions = questions, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2] )
    #first question
    otazka = jadernaEnergie.getInfoJadro(0)
    return render_template("jadG.html", points = 0, questions = 0, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2])

@app.route("/poleG.html", methods=["GET","POST"])
def poleG():
    if request.method == "POST":
        points = request.form.get("points")
        questions = request.form.get("questions")
        
        if(points == None or questions == None):
            return render_template("jadG.html", points = 0)
        otazka = pole.getInfoPole(int(questions))
        
        if(otazka[3] == 1 and request.form.get("a")):
            points = 1 + int(points)
        elif(otazka[3] == 2 and request.form.get("b")):
            points = 1 + int(points)

        if int(questions) +1 >= pole.getLenPole():
            body[1] = points
            return render_template("pole.html", points = points)
        
        
        questions = 1 + int(questions)
        otazka = pole.getInfoPole(int(questions))
        
        return render_template("jadG.html", points = points, questions = questions, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2] )
    otazka = pole.getInfoPole(0)
    return render_template("jadG.html", points = 0, questions = 0, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2])


@app.route("/rekaG.html", methods=["GET","POST"])
def rekaG():
    if request.method == "POST":
        points = request.form.get("points")
        questions = request.form.get("questions")
        
        if(points == None or questions == None):
            return render_template("jadG.html", points = 0)   
        otazka = rk.getInfoReka(int(questions))   
        
        if(otazka[3] == 1 and request.form.get("a")):
            points = 1 + int(points)
        elif(otazka[3] == 2 and request.form.get("b")):
            points = 1 + int(points)

        if int(questions) +1 >= rk.getLenReka():
            body[7] = points
            return render_template("reka.html", points = points)
        
        
        questions = 1 + int(questions)
        otazka = rk.getInfoReka(int(questions))
        
        return render_template("jadG.html", points = points, questions = questions, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2] )
    otazka = rk.getInfoReka(0)
    return render_template("jadG.html", points = 0, questions = 0, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2])

@app.route("/lesG.html", methods=["GET","POST"])
def lesG():
    if request.method == "POST":
        points = request.form.get("points")
        questions = request.form.get("questions")
        
        if(points == None or questions == None):
            return render_template("jadG.html", points = 0)  

        otazka = ls.getInfoLes(int(questions))      
        
        if(otazka[3] == 1 and request.form.get("a")):
            points = 1 + int(points)
        elif(otazka[3] == 2 and request.form.get("b")):
            points = 1 + int(points)

        if int(questions) +1 >= ls.getLenLes():
            body[3] = points
            return render_template("les.html", points = points)

        
        questions = 1 + int(questions)
        otazka = ls.getInfoLes(int(questions))
        
        return render_template("jadG.html", points = points, questions = questions, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2] )
    otazka = ls.getInfoLes(0)
    return render_template("jadG.html", points = 0, questions = 0, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2])

@app.route("/uhG.html", methods=["GET","POST"])
def dolyG():
    if request.method == "POST":
        points = request.form.get("points")
        questions = request.form.get("questions")
        
        if(points == None or questions == None):
            return render_template("jadG.html", points = 0)
              
        otazka = dl.getInfoDoly(int(questions))

        if(otazka[3] == 1 and request.form.get("a")):
            points = 1 + int(points)
        elif(otazka[3] == 2 and request.form.get("b")):
            points = 1 + int(points)

        if int(questions) +1 >= dl.getLenDoly():
            body[2] = points
            return render_template("uh.html", points = points)
        
        
        questions = 1 + int(questions)
        otazka = dl.getInfoDoly(int(questions))
        
        return render_template("jadG.html", points = points, questions = questions, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2] )
    otazka = dl.getInfoDoly(0)
    return render_template("jadG.html", points = 0, questions = 0, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2])

@app.route("/bioG.html", methods=["GET","POST"])
def bioG():
    if request.method == "POST":
        points = request.form.get("points")
        questions = request.form.get("questions")
        
        if(points == None or questions == None):
            return render_template("jadG.html", points = 0)
        
        otazka = bios.getInfoSkladka(int(questions))      
        
        if(otazka[3] == 1 and request.form.get("a")):
            points = 1 + int(points)
        elif(otazka[3] == 2 and request.form.get("b")):
            points = 1 + int(points)
        
        if int(questions) +1 >= bios.getLenSkladka():
            body[4] = points
            return render_template("bio.html", points = points)

        questions = 1 + int(questions)
        otazka = bios.getInfoSkladka(int(questions))
        
        return render_template("jadG.html", points = points, questions = questions, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2] )
    otazka = bios.getInfoSkladka(0)
    return render_template("jadG.html", points = 0, questions = 0, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2])

@app.route("/vodG.html", methods=["GET","POST"])
def vodG():
    if request.method == "POST":
        points = request.form.get("points")
        questions = request.form.get("questions")
        
        if(points == None or questions == None):
            return render_template("jadG.html", points = 0)
        
        otazka = vodA.getInfoHydro(int(questions))        
        
        if(otazka[3] == 1 and request.form.get("a")):
            points = 1 + int(points)
        elif(otazka[3] == 2 and request.form.get("b")):
            points = 1 + int(points)
        
        if int(questions) +1 >= vodA.getLenHydro():
            body[8] = points
            return render_template("vod.html", points = points)

        questions = 1 + int(questions)
        otazka = vodA.getInfoHydro(int(questions))
        
        return render_template("jadG.html", points = points, questions = questions, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2] )
    otazka = vodA.getInfoHydro(0)
    return render_template("jadG.html", points = 0, questions = 0, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2])

@app.route("/skodaG.html", methods=["GET","POST"])
def Skoda():
    if request.method == "POST":
        points = request.form.get("points")
        questions = request.form.get("questions")
        
        if(points == None or questions == None):
            return render_template("jadG.html", points = 0)
        
        otazka = skod.getInfo(int(questions))        
        
        if(otazka[3] == 1 and request.form.get("a")):
            points = 1 + int(points)
        elif(otazka[3] == 2 and request.form.get("b")):
            points = 1 + int(points)

        if int(questions) +1 >= skod.getLen():
            body[6] = points
            return render_template("skoda.html", points = points)

        questions = 1 + int(questions)
        otazka = skod.getInfo(int(questions))
        
        return render_template("jadG.html", points = points, questions = questions, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2] )
    otazka = skod.getInfo(0)
    return render_template("jadG.html", points = 0, questions = 0, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2])

@app.route("/vetG.html", methods=["GET","POST"])
def vetG():
    if request.method == "POST":
        points = request.form.get("points")
        questions = request.form.get("questions")
        
        if(points == None or questions == None):
            return render_template("jadG.html", points = 0)
        
        otazka = vt.getInfo(int(questions))       
        
        if(otazka[3] == 1 and request.form.get("a")):
            points = 1 + int(points)
        elif(otazka[3] == 2 and request.form.get("b")):
            points = 1 + int(points)
        
        if int(questions) +1 >= vt.getLen():
            body[9] = points
            return render_template("vet.html", points = points)

        questions = 1 + int(questions)
        otazka = vt.getInfo(int(questions))
        
        return render_template("jadG.html", points = points, questions = questions, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2] )
    otazka = vt.getInfo(0)
    return render_template("jadG.html", points = 0, questions = 0, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2])

@app.route("/solarG.html", methods=["GET","POST"])
def solarG():
    if request.method == "POST":
        points = request.form.get("points")
        questions = request.form.get("questions")
        
        if(points == None or questions == None):
            return render_template("jadG.html", points = 0)
        
        otazka = so.getInfoSolar(int(questions))        
        
        if(otazka[3] == 1 and request.form.get("a")):
            points = 1 + int(points)
        elif(otazka[3] == 2 and request.form.get("b")):
            points = 1 + int(points)

        if int(questions) + 1>= so.getLenSolar():
            
            body[5] = points
            return render_template("vet.html", points = points)

        questions = 1 + int(questions)
        otazka = so.getInfoSolar(int(questions))
        
        return render_template("jadG.html", points = points, questions = questions, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2] )
    otazka = so.getInfoSolar(0)
    return render_template("jadG.html", points = 0, questions = 0, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2])



if(__name__ == "__main__"):
    app.run(debug=True)