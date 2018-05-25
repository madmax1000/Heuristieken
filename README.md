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
<br /><br />
Greedy vindt in een minimale tijd (< 1 sec) een sequentie van 14 mutaties die het genoom van D. Melanogaster naar die van D. Miranda verandert. Een grote verbetering ten opzichte van Bubble Sort (154 mutaties).<br />
Zie de paragraaf "Aan de slag" voor hoe je Greedy kunt runnen.

#### Branch and Bound
Het probleem met Greedy is dat je niet zeker kan weten of de kortste sequentie mutaties gevonden is. Om daadwerkelijk de kortste sequentie mutaties te vinden gebruiken wij het Branch and Bound algoritme.<br />
Dit algoritme vindt _gegarandeerd_ de korste sequentie mutaties! Dit gaat echter ten koste aan een zeer veel langere run-time.<br /><br />
Zie de paragraaf "Aan de slag" voor hoe je Branch and Bound kunt runnen.

#### Random-Greedy-Branch and Bound
Voor ons derde algoritme is een zelf bedachte constructie gebruikt. We wilden het aspect dat Branch and Bound altijd zorgt voor de allerbeste oplossing behouden. Het probleem dat we nu moesten oplossen is dus de run time veel te lang is bij lange (lengte 23 +) genomen. Als oplossing hiervoor laten we de Branch and Bound pas runnen vanaf genomen, die een door ons ingesteld aantal breakpoints zijn verwijdert vanaf een genoom wat volledig op volgorde staat. Om te komen op het punt waarop het branch and bound algoritme te runnen, zal er eerst vanaf et originele genoom een random mutatie gekozen worden, welke vervolgens zal worden gemuteerd via greedy, tot het punt waarop de branch and bound kan worden ingezet. Vervolgens wordt op de volgende depth vanaf het originele genoom een nieuwe random mutatie gekozen vervolgt door greedy-branch and bound. Dit blijft doorgaan tot de grens van de branch and bound waarna vervolgens een nieuwe eerste mutatie wordt gekozen vanaf het originele genoom.

#### Greedy Points
Dit algoritme is bedoelt om genoom sequenties op te lossen in een laag aantal mutatie punten. Het werkt op dezelfde manier als ons vorig greedy algoritme, het enige verschil is dat we hier steeds de mutatie kiezen die het meest aantal breakpoints oplossen voor het minst aantal punten.

#### Random-Greedy Points
Dit is ons tweede algoritme om genoom seuquenties op te lossen in een laag aantal mutatie punten. Het algoritme lijkt op het Random-Greedy-Branch and Bound algoritme, het verschil hier is dat we de branch and bound niet gebruiken, aangezien dit niet werkt voor mutatie punnten. 


## Auteurs
* Max Bijkerk 10627510
* Steven Schoenmaker 10777679
* Milou Fuhri Snethlage 10770747
