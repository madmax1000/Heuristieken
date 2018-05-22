# Heuristieken

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

## De challenges
### Challenge 1: Bepaal een sequentie van mutaties dat het genoom van D. Melanogaster in het genoom van D. Miranda verandert. Bepaal ook de grenzen van de oplossingskwaliteit en de toestandsruimte.
Voor deze challenge hoeft er dus geen rekening gehouden te worden met het aantal mutatiestappen dat nodig is om het genoom van D. Melanogaster in het genoom van D. Miranda te veranderen.
We hebben gekozen voor het gebruik van het Bubble Sort algoritme.<br />
Dit algoritme vindt een oplossing in 154(!) mutatiestappen.<br />
Zie de paragraaf "Run Code" voor hoe je Bubble Sort kunt runnen.

### Challenge 2: Vind de "kortste" sequentie van mutaties dat het genoom van D. Melanogaster in het genoom van D. Miranda verandert. Als er meerdere kortste oplossingen zijn, vergelijk ze dan met elkaar.
De 154 sequentie mutatiestappen die Bubble Sort heeft gevonden is zeer waarschijnlijk níet hoe de mutatiesequentie die daadwerkelijk heeft plaatsgevonden in de natuur. Het is meer aannemelijk dat er een korte sequentie van mutaties heeft plaatsgevonden.<br />
In deze challenge zoeken we naar de *kortste* sequentie mutaties.<br /><br />

#### Greedy
Het Greedy algoritme kijkt na elke mutatie welke mutatie op dat specifieke moment de hoogste 'opbrengst' levert. Opbrengst hebben wij gedefinieerd als het aantal 'breakpoints' dat verwijderd wordt. Een breakpoint is gedefinieerd als een indexkoppel (i, i + 1) waarvoor geldt: __abs(genoom[i] + genoom[i + 1]) != 1__<br />
Er kunnen op elk moment in het genoom óf 2, óf 1, óf 0 breakpoints verwijderd worden.<br />
Als er een mutatie mogelijk is waarbij er 2 breakpoints verwijderd kunnen worden, zal Greedy altijd kiezen om deze mutatie uit te voeren! Er is namelijk geen hogere opbrengst mogelijk.<br />
Als er geen 2 breakpoints verwijderd kunnen worden, zal Greedy kiezen om een mutatie uit te voeren die 1 breakpoint verwijdert. Het is belangrijk om te weten dat een mutatie die een afnemende reeks getallen creëert, geprefereerd wordt boven een mutatie die een toenemde reeks getallen creëert. We refereren hierbij naar het paper dat wij voor deze opdracht hebben gebruikt: https://www2.cs.arizona.edu/~kece/Research/papers/KS95.ps
<br /><br />
Greedy vindt in een minimale tijd (< 1 sec) een sequentie van 14 mutaties die het genoom van D. Melanogaster naar die van D. Miranda verandert. Een grote verbetering ten opzichte van Bubble Sort (154 mutaties).<br />
Zie de paragraaf "Run Code" voor hoe je Greedy kunt runnen.

#### Branch and Bound
Het probleem met Greedy is dat je niet zeker kan weten of de kortste sequentie mutaties gevonden is. Om daadwerkelijk de kortste sequentie mutaties te vinden gebruiken wij het Branch and Bound algoritme.<br />
Dit algoritme vindt _gegarandeerd_ de korste sequentie mutaties! Dit gaat echter ten koste aan een zeer veel langere run-time.<br /><br />
Zie de paragraaf "Run Code" voor hoe je Branch and Bound kunt runnen.

## Aan de slag
### Vereisten
Het programma is geschreven in python3.

### Run Code
Om code uit te voeren:
```python
python main.py
```

U komt vervolgens in een keuzemenu.

Allereerst kunt u kiezen welk genoom u wilt muteren:
1) Het genoom van de D. Melanogaster, of
2) Een random gegenereerd genoom van een door u opgegeven lengte.

Vervolgens kunt u kiezen welk algoritme u wilt gebruiken om het genoom te sorteren:
1) Bubble Sort
2) Greedy
3) Branch and Bound (Waarschuwing: lange run-time voor grote genomen)

## Auteurs
* Max Bijkerk 10627510
* Steven Schoenmaker 10777679
* Milou Fuhri Snethlage 10770747
