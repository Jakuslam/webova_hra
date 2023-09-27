data = [
    ["Co je hlubinná těžba?", "těžení ve štolách", "těžení na povrchu", 1],
    ["Jak se nazívají hromady vykopaná zeminy?", "Hlušina", "Tišina", 1],
    ["Jak se nazívá proces znovuobnovení přirody po těžbě?", "rekonstrukce", "revitalizace", 2],
    ["Je možno těžbou narušit prameny pitné vody?", "Ne", "Ano", 2],
    ["Je možné posuniout kostel kvůli těžbe?", "Ano", "Ne", 1],
    ["O kolik byl tento kostel posunut?", "5m", "50m", 2],
    ["Jaké uhlí je straší?", "Hnědé", "Černé", 2],
    ["Z jaké doby bochází černé uhlí?", "siliKon", "karbon", 2],
]

def getInfoDoly(qNumber):
    i = 0
    for line in data:
        if(i == qNumber):
            return line
        i += 1

def getLenDoly():
    return(len(data))
