data = [
data = [
    ["Jaká je hlavní složka fotovoltaických panelů pro přeměnu sluneční energie na elektřinu?", "Křemík", "Ocel", 1],
    ["Jaký typ slunečního záření je nejvíce využíván fotovoltaickými elektrárnami?", "Sluneční záření v podobě tepla", "Sluneční záření v podobě fotónů", 2],
    ["Jak se nazývá proces, kterým fotovoltaické panely generují elektrickou energii?", "Fotosyntéza", "Fotovoltaický jev", 2],
    ["Jaký je hlavní typ invertorů používaných v fotovoltaických elektrárnách?", "Bateriové invertory", "Střídače", 2],
    ["Jakým způsobem lze ukládat přebytečnou elektřinu vyrobenou ve fotovoltaických elektrárnách?", "Vodíkové palivové články", "Baterie", 2],
    ["Jaký je hlavní důvod, proč jsou fotovoltaické elektrárny považovány za ekologicky šetrné?", "Snížení spotřeby fosilních paliv", "Výroba emisí skleníkových plynů", 1],
    ["Kde na světě se nachází největší fotovoltaická elektrárna podle instalovaného výkonu?", "Čína", "USA", 1],
    ["Jaká je průměrná životnost fotovoltaických panelů?", "25 let", "10 let", 1],
]

def getInfoLes(qNumber):
    i = 0
    for line in data:
        if(i == qNumber):
            return line
        i += 1

def getLenLes():
    return(len(data))
