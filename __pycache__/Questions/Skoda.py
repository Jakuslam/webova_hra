data = [
data = [
    ["Který model Škoda je nabízen v elektrické verzi s nulovými emisemi CO2?", "Méně než 10 %", "Více než 30 %", 2],
    ["Jak se nazývá program Škoda pro snižování ekologického dopadu výroby a logistiky?", "GreenLine", "GreenFuture", 2],
    ["Jaký je cíl snížení emisí CO2 v portfoliu vozidel Škoda do roku 2025?", "O 30%", "O 5%", 1],
    ["Jakým způsobem Škoda podporuje recyklaci baterií z elektrických vozidel?", "Opakovaným využitím a recyklací", "Skládkováním", 1],
    ["Jaký je název programu Škoda pro zlepšení energetické efektivity výrobních zařízení?", "EcoMode", "Green Factory", 2],
    ["Jaká je strategie Škoda vůči elektromobilitě do budoucna?", "Nadále se zaměřovat na tradiční spalovací motory", "Rozšířit nabídku elektromobilů a hybridních vozů", 2],
    ["Jaký je účel používání zelených střech na výrobních halách Škoda?", "Snížení tepelného zatížení budov", "Zlepšení aerodynamiky vozů", 1],
    ["Jaký je průměrný emisní výkon vozidel Škoda v rámci evropských emisních norem?", "Pod normou Euro 6d-TEMP", "Pod normou Euro 3", 1],
]

def getInfoLes(qNumber):
    i = 0
    for line in data:
        if(i == qNumber):
            return line
        i += 1

def getLenLes():
    return(len(data))
