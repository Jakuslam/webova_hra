data = [
    ["Kolik spaloven se v čr nachází?", "4", "5", 1],
    ["Mohou se spalovat ve spalovnách plasty?", "Ano", "Ne", 1],
    ["Mohou prakticky skončit toxické látky na smetišti?", "Ne", "Ano", 2],
    ["Co se stane po zaplnění skládky", "2", "3", 1],
    ["Kolik mají dukovany bloků?", "Zahází se hlínou", "Odpad se odveze jinam", 1],
    ["Kde se recikluje většina oblečení?", "V zemi vyhození", "V zemích třetího světa (např. Indie)", 2],
    ["Mohou se dávat do komunálního odpadu baterie?", "Ano", "Ne", 2],
    ["Jaký materiál se vyhazuje do žlutých kontejnerů?", "Plast", "Papír", 1],
]

def getInfoSkladka(qNumber):
    i = 0
    for line in data:
        if(i == qNumber):
            return line
        i += 1

def getLenSkladka():
    return(len(data))
