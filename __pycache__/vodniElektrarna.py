data = [
    ["Vodní elektrárny jsou zdrojem energie", "Obnovitelné", "Neobnovitelné", 1],
    ["Jak funguje vodní elektrárna?", "Generátor mění pohybovou energii vody na elektrickou energii", "Turbíny roztáčí vodní pára všudypřítomná na hladině", 1],
    ["Kolik procent celkové výroby elektrické energie tvoří energie z vodních elektráren?", "Přibližně 7%", "Přibližně 3%", 2],
    ["Mohou vodní elektrárny být použity pro skladování energie?", "ANO můžou být užity pro skladování", "Ne", 1],
    ["Jaké jsou nevýhody vodních elektráren?", "Potřebují vodní zdroje, vytváří nebezpečí pro vodní organismy", "Potřebují vodní zdroje, dramaticky pomáhají vysoušení krajiny", 1],
    ["Kde se nachází největší vodní elektrárna v ČR z hlediska celkového instalovaného výkonu?", "Vodní elektrárna Slapy", "Vodní elektrárna Dlouhé Stráně", 2],
    ["Jaké jsou druhy vodních elektráren?", "Jezové, derivační, chemicky upravující, přečerpávací", "Průtočné, přečerpávací, přílivové, akumulační", 2],
    ["Na jakém principu funguje přečerpávací elektrárna?", "Využívají dvou různě výškově položených vodních nádrží a akumulují energii v podobě potenciální energie vody.", "Vyčerpává vodu ze země a mění ji na vodní páru", 2],
]

def getInfoHydro(qNumber):
    i = 0
    for line in data:
        if(i == qNumber):
            return line
        i += 1

def getLenHydro():
    return(len(data))
