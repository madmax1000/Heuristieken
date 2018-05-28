# Results
Hier zijn de resultaten van elk van de challenges beschreven. Ook zijn er grafieken toegevoegd om de resultaten te visualiseren. 

### Challenge a) Bepaal een sequentie van mutaties dat het genoom van D. Melanogaster in het genoom van D. Miranda verandert. Bepaal ook de grenzen van de oplossingskwaliteit en de toestandsruimte.
Voor deze challenge hebben we het Bubble Sort algoritme en het Greedy algoritme gebruikt. Zie voor een beschrijving van het Greedy algoritme de README.md file op de vorige pagina. Wij gaan er van uit dat het Bubble Sort algorimte bekend is bij de lezer. 

#### Bubble Sort
...

#### Greedy
Greedy vindt in een minimale tijd (< 1 sec) een sequentie van __14 mutaties__ die het genoom van D. Melanogaster naar die van D. Miranda verandert. Een grote verbetering ten opzichte van Bubble Sort (154 mutaties)!

### Challenge b) Vind de "kortste" sequentie van mutaties dat het genoom van D. Melanogaster in het genoom van D. Miranda verandert. Als er meerdere kortste oplossingen zijn, vergelijk ze dan met elkaar.

#### Branch and Bound
Zoals uitgelegd op de vorige pagina is het probleem met Greedy dat je niet zeker weet of de kortste sequentie mutaties gevonden is. Om daadwerkelijk de kortste sequentie mutaties te vinden gebruiken wij het exhaustive Branch and Bound algoritme, dat _gegarandeerd_ de kortste sequentie mutaties vindt.<br />
Omdat de run-time van het Branch and Bound algoritme voor grote genomen extreem lang is, hebben wij het Branch and Bound algoritme voor het Melanogaster genoom niet volledig kunnen laten draaien. De run-time van het Branch and Bound algoritme is positief gecorreleerd met het aantal breakpoints in het originele genoom. Immers, meer breakpoints genereren meer opties om uit te voeren en dus een grotere boom die meer tijd kost om te doorlopen. Zie hier een scatter-plot die deze positieve correlatie weergeeft. De tijd is weergeven in seconden.
....


In de onderstaande scatter-plot is wederom te zien hoe het aantal breakpoints in het originele genoom zich verhoudt tot het minimale aantal mutatie stappen die uitgevoerd moeten worden om het genoom op te lossen. Aangezien voor het genereren van deze plot het Branch and Bound algoritme is gebruikt, weten we zeker dat dit daadwerkelijk het _minimale_ aantal mutaties is dat uitgevoerd moest worden voor dat specifieke genoom van een bepaalde lengte. 
...

#### Random-Greedy-Branch and Bound
Voor ons derde algoritme is een zelf bedachte constructie gebruikt. We wilden het aspect dat Branch and Bound altijd zorgt voor de allerbeste oplossing behouden. Het probleem dat echter opgelost moet worden is dat de run time veel te lang is bij grote (lengte 23 +) genomen. Als oplossing hiervoor hebben we het volgende algoritme bedacht. <br />
1. Kies een _random_ mutatie uit het originele genoom (depth = 0) en voer deze uit. <br />
2. Start vervolgens met het uitvoeren van het Greedy algoritme. <br />
3. STOP met Greedy uitvoeren als het aantal breakpoints in het genoom kleiner of gelijk is aan 8 (dit is een arbitrair gekozen threshold).<br />
4. BEGIN vervolgens met het uitvoeren van het Branch and Bound algoritme totdat het genoom is opgelost. <br />
5. Start opnieuw bij stap 1. Echter nu op depth = depth + 1. Blijf deze loop uitvoeren totdat Greedy niet meer uitgevoerd wordt omdat het aantal breakpoints in het gemuteerde genoom reeds kleiner of gelijk is aan 8 (de arbitrair gekozen threshold). <br />
6. Voer stappen 1 tm 5 geheel opnieuw uit voor een vooraf bepaald aantal iteraties. Bewaar de kortse sequentie mutaties wanneer alle iteraties uitgevoerd zijn. Dit is de uiteindelijke oplossing. <br />

Met deze constructie hebben we geen last van de extreem lange run-time van het Branch and Bound algoritme, maar benutten we tegelijkertijd wél de exhausitve eigenschap van het Branch and Bound (alhoewel dit dus pas benut wordt _vanaf_ 8 of minder breakpoints). Vóór de treshold zijn we overgeleverd aan het non-exhaustive Greedy algoritme. 

#### Greedy Points
Dit algoritme is bedoelt om genoom sequenties op te lossen in een laag aantal mutatie punten. Het werkt op dezelfde manier als ons vorig Greedy algoritme, het enige verschil is dat we hier steeds de mutatie kiezen die het meeste aantal breakpoints oplost voor het minst aantal punten (in tegenstelling tot ons voorgaande Greedy algoritme die telkens de mutatie kiest die het meest aantal breakpoints oplost).

#### Random-Greedy Points
Dit is ons tweede algoritme om genoom sequenties op te lossen in een laag aantal mutatie punten. Het algoritme lijkt op het Random-Greedy-Branch and Bound algoritme, het verschil hier is dat we de Branch and Bound niet gebruiken. De reden hiervoor is dat er een lowerbound vastgesteld moet worden om Branch and Bound te gebruiken. Het vinden van een lowerbound in termen van mutatie _punten_ voor een willekeurig genoom is niet triviaal. Het algoritme ziet er als volgt uit. <br />
1. Los het genoom op met Greedy. Zet _upperbound_ gelijk aan het aantal mutatiepunten dat deze Greedy vond. <br />
2. Kies een _random_ mutatie uit het originele genoom (depth = 0) en voer deze uit. <br />
3. Start vervolgens met het uitvoeren van het Greedy algoritme totdat het genoom is opgelost. Als dit aantal mutatiepunten lager is dan _upperbound_, update dan de _upperbound_. <br />
4. Start opnieuw bij stap 1. Echter nu op depth = depth + 1 (dus nu vanáf de voorgaande random uitgevoerde mutatie!). <br />
6. Voer stappen 1 tm 5 geheel opnieuw uit voor een vooraf bepaald aantal iteraties. Bewaar de sequentie mutaties met de laagste _upperbound_ wanneer alle iteraties uitgevoerd zijn. Dit is de uiteindelijke oplossing. <br />
