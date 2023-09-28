data = [
    ["Jaké napětí běžně vyrábí fotovoltaické panely?", "24V / 12V", "60V / 120V", 1],
    ["Lze pěstovat pod FVE panely rostliny?", "Ano", "Ne", 1],
    ["K čemu slouží měnič u FVE?", "Převádění DC z FVE do AC síťového napětí", "Přehrávání AC/DC", 1],
    ["Mohou se instalovat v CHKO všechny FV panely?", "Ano", "Ne", 2],
    ["Kolik energie průměrně v čr vyrobí jeden FV panel?", "300kWh - 600kWh", "250kWh - 400kWh", 2],
    ["Vyrábí FVE více, když je chlazená?", "Ano", "Ne", 1],
    ["O kolik se v zimě sníží účinnost FVE?", "50%", "20%", 2],
    ["Můžeš se v CHKO používat stříbrná FVE?", "Ano", "Ne", 2],
]

def getInfoSolar(qNumber):
    i = 0
    for line in data:
        if(i == qNumber):
            return line
        i += 1

def getLenSolar():
    return(len(data))
