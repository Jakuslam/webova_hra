data = [
    ["Jak získáváme energii z vodních toků? ", "Využíváme pohybovou energii protékající vody a měníme ji na elektrickou energii.", "Vychytáváme zbytky elektrické energie z odumřelých živočichů. ", 1],
    ["Kde na vodním toku stavíme vodní elektrárny?", "Na místech kde se tvoří peřejky a voda je v těchto místech mělká ", "Zpravidla na jezech nebo ohraničených vodních dílech", 2],
    ["Jaký je hlavní způsob, jakým lidská činnost ovlivňuje ekosystémy řek?", "Lesní požáry", "Znečištění vod a regulace toku řek.", 2],
    ["Jaký druh ekologických problémů může způsobit průmyslová výroba u řek?", "Vytváření ochranných rezervací", "Znečištění vod a odběr vody pro chlazení", 2],
    ["Co znamená eutrofizace v kontextu ekologie řek?", "Přebytek živin v řekách, což vede ke zhoršení kvality vody a růstu řas.", "Snížení hladiny řeky během sucha.", 1],
    ["Jaký význam mají mokřady v ekologii řek a jak chrání řeky?", "Mokřady slouží jako filtry pro znečištění a zároveň zabraňují povodním", " Mokřady zvyšují erozi břehů řek", 1],
    ["Jaké druhy zvířat jsou ohroženy v důsledku degradace říčního prostředí?", "Několik ohrožených druhů, například lososa atlantického a vydru říční.", "Hadi a pavouci", 1],
    ["Jak mohou místní komunity přispět k ochraně ekosystémů řek?", "Ignorováním ekologických problémů řek.", "Zapojením se do dobrovolnických činností, osvětovou prací a podporou udržitelného využívání říčních zdrojů", 2],
]

def getInfoReka(qNumber):
    i = 0
    for line in data:
        if(i == qNumber):
            return line
        i += 1

def getLenReka():
    return(len(data))
