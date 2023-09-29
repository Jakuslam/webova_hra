data = [
    ["Je povolené rozdělávat oheň v lese?", "Pouze na určených místech", "Všude", 1],
    ["Je zakázáno lovit všechna zvířata v době páření a vyvádění mláďat?", "Ano", "Ne", 2],
    ["Je povoleno po většinu roku lovit vlky?", "Ano", "Ne", 2],
    ["Jaké je v čr tradyční složení lesů?", "Jehličnatý", "Smíšený", 2],
    ["Co je to lužní les?", "Les v němž se čas od času zaplaven vodou", "Les v němž je velké množství mýtin", 1],
    ["Je koniklec chráněná rostlina?", "Ano", "Ne", 1],
    ["Nachází se v Čr neaktivní sopky?", "Ano", "Ne", 1],
    ["Jaký je význam lesů pro životní prostředí?", "Lesy mají negativní dopad na životní prostředí tím, že zvyšují znečištění vzduchu a vodu", " Lesy přispívají k udržení kvality vzduchu, regulaci vodního cyklu, a poskytují útočiště pro mnoho druhů rostlin a živočichů", 2],
]

def getInfoLes(qNumber):
    i = 0
    for line in data:
        if(i == qNumber):
            return line
        i += 1

def getLenLes():
    return(len(data))
