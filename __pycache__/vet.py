data = [
    ["Jak funguje větrná elektrárna?", "Pádla rozhýbávají atomy vzduchu, které svým pohybem vytváří elektrickou energii", "Rotace větrného rotoru pohání generátor a generuje elektrickou energii", 2],
    ["Jaké jsou různé druhy větrných elektráren?", "vnitrozemské, podvodní, vesmírné", "přímořské, vnitrozemské a umístěné na moři", 2],
    ["Kde se nachází nejvíce větrných elektráren na světě?", "Německo", "Čína", 2],
    ["Jaký typ energie je většinou potřeba pro startování větrné turbíny?", "Elektrická energie", "Mechanická energie", 1],
    ["Jaký typ turbíny je častěji používán ve větrných elektrárnách?", "Vertikální", "Horizontální", 2],
    ["Jaký je hlavní výhodou větrných elektráren ve vztahu k životnímu prostředí?", "Emisní zátěž v podobě skleníkových plynů", "Snížení potřeby vody pro chlazení", 1],
    ["Jaké jsou hlavní výzvy spojené s větrnými elektrárnami?", "Kolize s ptáky a netopýry", "Nedostatek dostatečného větru", 1],
    ["Jaký je průměrný životnost větrné turbíny?", "10-15 let", "20-25 let", 2],
]

def getInfo(qNumber):
    i = 0
    for line in data:
        if(i == qNumber):
            return line
        i += 1

def getLen():
    return(len(data))
