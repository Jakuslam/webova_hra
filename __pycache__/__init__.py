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
from getQuestions import *



app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'weby'

#webside
@app.route("/", methods=["GET","POST"])
def home():
    return render_template("h2.html")

@app.route("/game.html", methods=["GET","POST"])
def newGame():
    return render_template("game.html")

@app.route("/jad.html", methods=["GET","POST"])
def jad():
    return render_template("jad.html")

@app.route("/pole.html", methods=["GET","POST"])
def pol():
    return render_template("pole.html")

@app.route("/bio.html", methods=["GET","POST"])
def bio():
    return render_template("bio.html")

@app.route("/idk.html", methods=["GET","POST"])
def idk():
    return render_template("idk.html")

@app.route("/les.html", methods=["GET","POST"])
def les():
    return render_template("les.html")

@app.route("/reka.html", methods=["GET","POST"])
def reka():
    return render_template("reka.html")

@app.route("/slun.html", methods=["GET","POST"])
def slun():
    return render_template("slun.html")

@app.route("/uh.html", methods=["GET","POST"])
def uh():
    return render_template("uh.html")

@app.route("/vet.html", methods=["GET","POST"])
def vet():
    return render_template("vet.html")

@app.route("/vod.html", methods=["GET","POST"])
def vod():
    return render_template("vod.html")

@app.route("/jadG.html", methods=["GET","POST"])
def jadG():
    if request.method == "POST":
        points = request.form.get("points")
        questions = request.form.get("questions")
        if(points == None or questions == None):
            return render_template("jadG.html", points = 0, questions = 0)

        otazka = jadernaEnergie.getInfoJadro(int(questions))

        if int(questions) +1 >= jadernaEnergie.getLenJadro():
            return render_template("jad.html", points = points, questions = int(questions) + 1)
        
        print(otazka)
        if(otazka[3] == 1 and request.form.get("a")):
            points = 1 + int(points)
        elif(otazka[3] == 2 and request.form.get("b")):
            points = 1 + int(points)

        if(request.form.get("b")):
            print(2)

        
        questions = 1 + int(questions)
        otazka = jadernaEnergie.getInfoJadro(int(questions))
        return render_template("jadG.html", points = points, questions = questions, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2] )
    otazka = jadernaEnergie.getInfoJadro(0)
    return render_template("jadG.html", points = 0, questions = 0, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2])

@app.route("/poleG.html", methods=["GET","POST"])
def poles():
    if request.method == "POST":
        points = request.form.get("points")
        questions = request.form.get("questions")
        
        if(points == None or questions == None):
            return render_template("jadG.html", points = 0, questions = 0)
        
        if int(questions) +1 >= pole.getLenPole():
            return render_template("pole.html", points = points, questions = int(questions) +1)
        
        otazka = pole.getInfoPole(int(questions))
        questions = 1 + int(questions)
        
        
        if(otazka[3] == 1 and request.form.get("a")):
            points = 1 + int(points)
        elif(otazka[3] == 2 and request.form.get("b")):
            points = 1 + int(points)

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
            return render_template("jadG.html", points = 0, questions = 0)
        
        if int(questions) +1 >= rk.getLenReka():
            return render_template("reka.html", points = points, questions = int(questions) +1)
        
        otazka = rk.getInfoReka(int(questions))
        questions = 1 + int(questions)
        
        
        if(otazka[3] == 1 and request.form.get("a")):
            points = 1 + int(points)
        elif(otazka[3] == 2 and request.form.get("b")):
            points = 1 + int(points)

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
            return render_template("jadG.html", points = 0, questions = 0)
        
        if int(questions) +1 >= ls.getLenReka():
            return render_template("reka.html", points = points, questions = int(questions) +1)
        
        otazka = ls.getInfoReka(int(questions))
        questions = 1 + int(questions)
        
        
        if(otazka[3] == 1 and request.form.get("a")):
            points = 1 + int(points)
        elif(otazka[3] == 2 and request.form.get("b")):
            points = 1 + int(points)

        otazka = ls.getInfoReka(int(questions))
        
        return render_template("jadG.html", points = points, questions = questions, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2] )
    otazka = ls.getInfoReka(0)
    return render_template("jadG.html", points = 0, questions = 0, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2])

@app.route("/uhG.html", methods=["GET","POST"])
def dolyG():
    if request.method == "POST":
        points = request.form.get("points")
        questions = request.form.get("questions")
        
        if(points == None or questions == None):
            return render_template("jadG.html", points = 0, questions = 0)
        
        if int(questions) +1 >= dl.getLenDoly():
            return render_template("doly.html", points = points, questions = int(questions) +1)
        
        otazka = dl.getInfoDoly(int(questions))
        questions = 1 + int(questions)
        
        
        if(otazka[3] == 1 and request.form.get("a")):
            points = 1 + int(points)
        elif(otazka[3] == 2 and request.form.get("b")):
            points = 1 + int(points)

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
            return render_template("jadG.html", points = 0, questions = 0)
        
        if int(questions) +1 >= bios.getLenSkladka():
            return render_template("bio.html", points = points, questions = int(questions) +1)
        
        otazka = bios.getInfoSkladka(int(questions))
        questions = 1 + int(questions)
        
        
        if(otazka[3] == 1 and request.form.get("a")):
            points = 1 + int(points)
        elif(otazka[3] == 2 and request.form.get("b")):
            points = 1 + int(points)

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
            return render_template("jadG.html", points = 0, questions = 0)
        
        if int(questions) +1 >= vodA.getLenHydro():
            return render_template("vod.html", points = points, questions = int(questions) +1)
        
        otazka = vodA.getInfoHydro(int(questions))
        questions = 1 + int(questions)
        
        
        if(otazka[3] == 1 and request.form.get("a")):
            points = 1 + int(points)
        elif(otazka[3] == 2 and request.form.get("b")):
            points = 1 + int(points)

        otazka = vodA.getInfoHydro(int(questions))
        
        return render_template("jadG.html", points = points, questions = questions, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2] )
    otazka = vodA.getInfoHydro(0)
    return render_template("jadG.html", points = 0, questions = 0, question = otazka[0], ansv1 = otazka[1], ansv2 = otazka[2])


if(__name__ == "__main__"):
    app.run(debug=True)