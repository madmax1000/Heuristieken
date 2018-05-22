# Heuristieken

## Fruitvliegen genoom

Het genoom van dieren die aan elkaar nauw aan elkaar verwant zijn zal meer overeenkomen met elkaar dan dieren die dit niet zijn.
Mutaties hebben voor deze verschillen gezorgd, dus er kan ook gesteld worden dat wanneer er weinig mutaties zijn opgetreden tussen 2
genomen, de dieren nauw aan elkaar verwant is. In onze case worden genoom sequenties met elkaar vergeleken en ons doel is het om de korst
mogelijke sequentie van mutaties te vinden als indicator van hoe verwant soorten aan elkaar zijn.

Er wordt door ons enkel naar één soort mutatie gekeken, namelijk een 'flip' mutatie waarin een bepaald stukje genoom helemaal is
omgekeerd. (4 5 - 3 2 1 6 - 7 9) -> (4 5 - 6 1 2 3 - 7 9) (mutatie tussen streepjes)

De genoom sequentie zal gezien worden als een volgorde van getallen die door een algoritme in een oplopende volgorde geplaatst moet worden in
zo min mogelijk aantal stappen.

## Aan de slag
### Vereisten
Het programma is geschreven in python3.
### Run Code
Om code uit te voeren:
```python
python main.py
```
Vervolgens krijgt u de keuze om:
1. Het genoom van de D. Melanogaster te gebruiken, of:
2. Een random gegenereerd genoom van gewenste lengte te gebruiken.

Hierna krijgt u de keuze uit verschillende algoritmes:
1. Bubble Sort
2. Greedy
3. Branch and Bound

## Auteurs
* Max Bijkerk 10627510
* Steven Schoenmaker 10777679
* Milou Fuhri Snethlage 10770747
