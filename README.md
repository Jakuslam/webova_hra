Popis:

Tento projekt by měla být zábavná vzdělávací hra na téma ekologie s příměsí automobilizmu. V našem pojetí jsme z toho vytvořili 2D interaktivní point-click naučnou hru,
která má potenciál zabavit nejmeční, ale naučit něco i dospělé.

Pravidla:

Při rozkliknutí tlačítka "Hra" je člověk převeden na stránku, kde se nachází 10 sad otézek po 8 otázkách, které jsou rozděleny do 3 okruhů. 
Energie (žlutá), ekologie (zelená), o automobilce Škoda (modrá). Pokud člověk dokončí sadu otázek a zodpoví vše správně, tak tato sada zmizí. 
Za správné zodpovězení všech otázek v okruhu člověk dostane achievement a při správném zodpovězení všech otázek se hráči zobrazí výtězná obrazovka.

Jak funguje kód:

Primární soubor __init__.py načítá hráči stránky pomocí knihovny Flask. Pokud se hráč proklikne na quizz, tak se načte soubor "jadG.html" a pošlou se do něj otázky, které se načtou z importovaných python souborů (v každém je jedna sada otázek). Program počítá na kolikáté otázce a podle toho přiřazuje další a vyhodnocuje správnost odpovědi. Při dokončení kvízu se výsledné body zapíší do listu "body[9]", kde každé pole má přiřazenou sadu otázek. Pokaždé při načtení hlavní mapy se vyhodnocuje, zda je na všech místech tohoto listu 8 bodů, pokud tomu tak je, tak se spustí vítězná obrazovka.
