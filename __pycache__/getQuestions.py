import csv

def getQuestion(questionSet, numberOfQuestion):
    numberOfQuestion += 1
    with open("Questions/" + questionSet + ".csv", 'r') as file:
        exitRow = []
        csvreader = csv.reader(file)
        i = 0
         
        for row in csvreader:
            if i == numberOfQuestion:
                exitRow = row
            i +=1
        return exitRow

header = ['Question', 'Answ1', 'Answ2', 'rightAnsv']

