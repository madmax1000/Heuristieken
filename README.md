# Heuristieken
## Aan de slag
### Vereisten
Het programma is geschreven in python3.

Python libraries: math, copy, random, time, matplotlib
### Run Code
Om code uit te voeren:
```python
python main.py
```
U komt vervolgens in een keuzemenu dat voor zichzelf spreekt.

Veel plezier met muteren!

## Korte beschrijving van de challenge
## Twee fruitvliegjes
De genomen van twee dieren die aan nauw aan elkaar verwant zijn, zullen meer overeenkomen dan de genomen van dieren die dit niet zijn.
Verschillen tussen genomen van nauw verwante dieren zijn er echter wel. Mutaties hebben hiervoor gezorgd.
Het kan dus gesteld worden dat wanneer er weinig mutaties zijn opgetreden tussen de genomen van twee dieren, deze dieren nauw aan elkaar verwant zijn.
Datzelfde geldt voor de fruitvliegjes Drosophila Melanogaster en Drosophila Miranda. In deze opdracht is het zaak te achterhalen welke reeks van achtereenvolgende mutaties de ene fruitvliegensoort in de andere heeft doen veranderen.

## De genomen
Het genoom van de D. Melanogaster ziet er als volgt uit:<br />
[23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]<br /><br />
Het genoom van de D. Miranda ziet er als volgt uit:<br />
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]<br /><br />
Natuurlijk bestaan genomen in het echt niet uit getallen. Dit is echter een handige abstrahering om de opdracht uit te voeren.

## Mutaties
Mutaties kunnen enkel op één manier plaatsvinden, namelijk door 'reversals'. Tijdens een reversal wordt een bepaald stukje binnen een genoom in zijn geheel omgekeerd.<br />
Zie hier een reversal:<br />
(4 5 - 3 2 1 6 - 7 9) --> (4 5 - 6 1 2 3 - 7 9) (mutatie tussen streepjes)<br /><br />
Een reversal wordt gekaraktiseerd door een indexkoppel (i, j). Hierbij is i de index van het linker gen van het stuk dat ge-reversed wordt, en j de index van het rechter gen van het stuk dat ge-reversed wordt.


## De algoritmes
#### Greedy
Het Greedy algoritme kijkt na elke mutatie welke mutatie op dat specifieke moment de hoogste 'opbrengst' levert. Opbrengst hebben wij gedefinieerd als het aantal 'breakpoints' dat verwijderd wordt. Een breakpoint is gedefinieerd als een indexkoppel (i, i + 1) waarvoor geldt: __abs(genoom[i] - genoom[i + 1]) != 1__<br />
Er kunnen op elk moment in het genoom óf 2, óf 1, óf 0 breakpoints verwijderd worden.<br />
Als er een mutatie mogelijk is waarbij er 2 breakpoints verwijderd kunnen worden, zal Greedy altijd kiezen om deze mutatie uit te voeren! Er is namelijk geen hogere opbrengst mogelijk.<br />
Als er geen 2 breakpoints verwijderd kunnen worden, zal Greedy kiezen om een mutatie uit te voeren die 1 breakpoint verwijdert. Het is belangrijk om te weten dat een mutatie die een afnemende reeks getallen creëert, geprefereerd wordt boven een mutatie die een toenemde reeks getallen creëert. We refereren hierbij naar het paper dat wij voor deze opdracht hebben gebruikt: https://www2.cs.arizona.edu/~kece/Research/papers/KS95.ps


#### Branch and Bound
Het probleem met Greedy is dat je niet zeker kan weten of de kortste sequentie mutaties gevonden is. Om daadwerkelijk de kortste sequentie mutaties te vinden gebruiken wij het Branch and Bound algoritme.<br />
Dit algoritme vindt _gegarandeerd_ de korste sequentie mutaties! Dit gaat echter ten koste aan een zeer veel langere run-time.

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
Dit algoritme is bedoelt om genomen te sorteren in een laag aantal mutatie punten. Het werkt op dezelfde manier als ons vorig Greedy algoritme, het enige verschil is dat we hier steeds de mutatie kiezen die het meeste aantal breakpoints oplost voor het minst aantal punten (in tegenstelling tot ons voorgaande Greedy algoritme die telkens de mutatie kiest die het meest aantal breakpoints oplost).

#### Random-Greedy Points
Dit is ons tweede algoritme om genoom sequenties op te lossen in een laag aantal mutatie punten. Het algoritme lijkt op het Random-Greedy-Branch and Bound algoritme, het verschil hier is dat we de Branch and Bound niet gebruiken. De reden hiervoor is dat er een lowerbound vastgesteld moet worden om Branch and Bound te gebruiken. Het vinden van een lowerbound in termen van mutatie _punten_ voor een willekeurig genoom is niet triviaal.Het algoritme ziet er als volgt uit. <br />
1. Los het genoom op met Greedy. Zet _upperbound_ gelijk aan het aantal mutatiepunten dat deze Greedy vond. <br />
2. Kies een _random_ mutatie uit het originele genoom (depth = 0) en voer deze uit. <br />
3. Start vervolgens met het uitvoeren van het Greedy algoritme totdat het genoom is opgelost. Als dit aantal mutatiepunten lager is dan _upperbound_, update dan de _upperbound_. <br />
4. Start opnieuw bij stap 1. Echter nu op depth = depth + 1 (dus nu vanáf de voorgaande random uitgevoerde mutatie!). <br />
6. Voer stappen 1 tm 5 geheel opnieuw uit voor een vooraf bepaald aantal iteraties. Bewaar de sequentie mutaties met de laagste _upperbound_ wanneer alle iteraties uitgevoerd zijn. Dit is de uiteindelijke oplossing. <br />
<br />
Dit algoritme is niet exhaustive. Enkel in het theoretische voorbeeld wanneer het aantal iteraties op oneindig wordt gezet, is het algoritme exhaustive. In dat geval wordt met zekerheid de beste oplossing gevonden. Aangezien het aantal iteraties niet op oneindig gezet kán worden, weten we niet zeker of we de beste oplossing hebben gevonden. Het is echter wél een verbetering ten opzichte van Greedy, aangezien Greedy maar één route af gaat en dit Random-Greedy algoritme zo veel als maar gespecificeerd is door de gebruiker (dmv iteraties).<br />
Om het algoritme mogelijk nóg meer te versnellen geven we de gebruiker de mogelijkheid om te kiezen tussen de opties _"uniform"_ en _"non-uniform"_. Uniform houdt in dat in stap 2 de random mutatie optie gekozen wordt volgens de uniforme kansverdeling. Dat betekent dus dat 'slechte' opties (opties die zorgen voor relatief veel mutatiepunten) even veel kans hebben om gekozen te worden als 'goede' opties (opties die zorgen voor relatief weinig mutatiepunten). Non-uniform houdt in dat 'goede' opties een hogere kans hebben om gekozen te worden. We maken hierbij gebruik van de _triangular_ kansverdeling. Het idee hier achter is dat de kans zo groter is om sneller de optimale oplossing te vinden.

## Auteurs
* Max Bijkerk 10627510
* Steven Schoenmaker 10777679
* Milou Fuhri Snethlage 10770747
