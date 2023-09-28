data = [
    
]

def getInfoLes(qNumber):
    i = 0
    for line in data:
        if(i == qNumber):
            return line
        i += 1

def getLenLes():
    return(len(data))
