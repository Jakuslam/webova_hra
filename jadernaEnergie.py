data = [
    ["Jak funguje jaderná elektrárna?", "Funguje na principu jaderného štěpení", "Funguje na principu makroexplozí jaderných bomb", 1],
    ["Potřebuje jaderná elektrárna chlazení?", "Ano, využívá k tomu chladící věže", "Ne, neuvolňuje se žádné teplo", 1],
    ["Kolik procent Energie v Čr je vyráběno pomocí jaderných elektráren?", "14,5%", "36,7%", 2],
    ["Kolik je jaderných elektráren v Čr?", "2", "3", 1],
    ["Kolik mají dukovany bloků?", "4", "6", 1],
    ["Jaká jaderná elektrárna selhala kvůli lidské chybě?", "Fukušima", "Černobyl", 2],
    ["Vlastní ČEZ dukovany?", "Ano", "Ne", 1],
    ["Z kolika dílů se skládají jaderné elektrárny?", "3", "1", 1],
]

def getInfoJadro(qNumber):
    i = 0
    for line in data:
        if(i == qNumber):
            return line
        i += 1

def getLenJadro():
    return(len(data))

