data = [
    ["Jaký je hlavní zdroj suroviny pro výrobu bioplynu v bioplynových stanicích?", "Organický materiál", "Ropa", 1],
    ["Jaký je hlavní proces, kterým bioplynové stanice zpracovávají organický odpad?", " Fermentace", "Spalování", 1],
    ["K čemu slouží anaerobní fermentace v procesu výroby bioplynu?", "Ke zvýšení obsahu kyslíku", "K rozkladu organických materiálů", 2],
    ["Jaký druh bioplynu je nejběžněji využíván pro výrobu elektřiny a tepla v bioplynových stanicích?", "Biometan", "Biowatergas", 1],
    ["Jaká je hlavní využití bioplynu v zemědělství?", "Zemědělské stroje a vybavení", "Hnojivo", 1],
    ["Co se stane s odpadem po dokončení procesu anaerobní fermentace v bioplynových stanicích?", "Skládkování", "Vytvoření hnojiva", 2],
    ["Jaký je hlavní výstupní produkt v procesu anaerobní fermentace?", "Bioplyn", "Elektrická energie", 1],
    ["Jaké jsou hlavní výhody spalování bioplynu?", "Nižší výrobní náklady", "Efektivní využití organického odpadu", 2],
]

def getInfoSkladka(qNumber):
    i = 0
    for line in data:
        if(i == qNumber):
            return line
        i += 1

def getLenSkladka():
    return(len(data))
