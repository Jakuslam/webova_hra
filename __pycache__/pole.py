data = [
    ["Jak by se měly orat brázdy?", "Horizontálně ku svahem", "Kolmo ke svahu", 1],
    ["Jaká značka je vyhlášená konstruováním traktorů?", "Tatra", "Zetor", 2],
    ["Kdy se seje ozim", "V zimě", "Na podzim", 2],
    ["Umí lidský metabolizmus zpracovat krmnou kukuřici", "Ano", "Ne", 1],
    ["Co nebo kdo je to Remízek?", "Úsek louky mezi poly", "Ministr zemědělství", 1],
    ["Jaká je nejpěstovanější plodina v čr?", "Řepka olejka", "Mák", 1],
    ["Co je mrva?", "Lejna zvířat, která se používají na hnojení", "Typ obylniny pěstovaný v nepříznivých podmínkách", 2],
    ["Jak dlouho roste více letka", "2 roky", "více jak 2 roky", 2],
]

def getInfoPole(qNumber):
    i = 0
    for line in data:
        if(i == qNumber):
            return line
        i += 1

def getLenPole():
    return(len(data))