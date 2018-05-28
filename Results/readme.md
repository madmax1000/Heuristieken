# Results
Hier zijn de resultaten van elk van de challenges beschreven. Ook zijn er grafieken toegevoegd om de resultaten te visualiseren. 

### Challenge a) Bepaal een sequentie van mutaties dat het genoom van D. Melanogaster in het genoom van D. Miranda verandert. Bepaal ook de grenzen van de oplossingskwaliteit en de toestandsruimte.
Voor deze challenge hebben we het Bubble Sort algoritme en het Greedy algoritme gebruikt. Zie voor een beschrijving van het Greedy algoritme de README.md file op de vorige pagina. Wij gaan er van uit dat het Bubble Sort algorimte bekend is bij de lezer. 

#### Bubble Sort
Bubble Sort vindt voor het Melanogaster genoom in een minimale tijd (< 1 sec) een sequentie van __154 mutaties__ die het genoom van D. Melanogaster naar die van D. Miranda verandert.<\br>

BUBBLE ALGORITHM STARTS<br />
<br />
Mutation number:  1   [0, 1, 23, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  2   [0, 1, 2, 23, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  3   [0, 1, 2, 11, 23, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  4   [0, 1, 2, 11, 23, 22, 24, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  5   [0, 1, 2, 11, 23, 22, 19, 24, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  6   [0, 1, 2, 11, 23, 22, 19, 6, 24, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  7   [0, 1, 2, 11, 23, 22, 19, 6, 10, 24, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  8   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  9   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 25, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  10   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 25, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  11   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 25, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  12   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 25, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  13   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 25, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  14   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 25, 14, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  15   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 25, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  16   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 25, 16, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  17   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 25, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  18   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 25, 21, 3, 4, 9, 26]<br />
Mutation number:  19   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 25, 3, 4, 9, 26]<br />
Mutation number:  20   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 25, 4, 9, 26]<br />
Mutation number:  21   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 25, 9, 26]<br />
Mutation number:  22   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]<br />
Mutation number:  23   [0, 1, 2, 11, 22, 23, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]<br />
Mutation number:  24   [0, 1, 2, 11, 22, 19, 23, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]<br />
Mutation number:  25   [0, 1, 2, 11, 22, 19, 6, 23, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]<br />
Mutation number:  26   [0, 1, 2, 11, 22, 19, 6, 10, 23, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]<br />
Mutation number:  27   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]<br />
Mutation number:  28   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 24, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]<br />
Mutation number:  29   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 24, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]<br />
Mutation number:  30   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 24, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]<br />
Mutation number:  31   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 24, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]<br />
Mutation number:  32   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 24, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]<br />
Mutation number:  33   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 24, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]<br />
Mutation number:  34   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 24, 15, 16, 17, 21, 3, 4, 9, 25, 26]<br />
Mutation number:  35   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 24, 16, 17, 21, 3, 4, 9, 25, 26]<br />
Mutation number:  36   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 24, 17, 21, 3, 4, 9, 25, 26]<br />
Mutation number:  37   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 24, 21, 3, 4, 9, 25, 26]<br />
Mutation number:  38   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 24, 3, 4, 9, 25, 26]<br />
Mutation number:  39   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 24, 4, 9, 25, 26]<br />
Mutation number:  40   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 24, 9, 25, 26]<br />
Mutation number:  41   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]<br />
Mutation number:  42   [0, 1, 2, 11, 19, 22, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]<br />
Mutation number:  43   [0, 1, 2, 11, 19, 6, 22, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]<br />
Mutation number:  44   [0, 1, 2, 11, 19, 6, 10, 22, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]<br />
Mutation number:  45   [0, 1, 2, 11, 19, 6, 10, 7, 22, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]<br />
Mutation number:  46   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 23, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]<br />
Mutation number:  47   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 23, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]<br />
Mutation number:  48   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 23, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]<br />
Mutation number:  49   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 23, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]<br />
Mutation number:  50   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 23, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]<br />
Mutation number:  51   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 23, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]<br />
Mutation number:  52   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 23, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]<br />
Mutation number:  53   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 23, 16, 17, 21, 3, 4, 9, 24, 25, 26]<br />
Mutation number:  54   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 23, 17, 21, 3, 4, 9, 24, 25, 26]<br />
Mutation number:  55   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 23, 21, 3, 4, 9, 24, 25, 26]<br />
Mutation number:  56   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 23, 3, 4, 9, 24, 25, 26]<br />
Mutation number:  57   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 23, 4, 9, 24, 25, 26]<br />
Mutation number:  58   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 23, 9, 24, 25, 26]<br />
Mutation number:  59   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]<br />
Mutation number:  60   [0, 1, 2, 11, 6, 19, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]<br />
Mutation number:  61   [0, 1, 2, 11, 6, 10, 19, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]<br />
Mutation number:  62   [0, 1, 2, 11, 6, 10, 7, 19, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]<br />
Mutation number:  63   [0, 1, 2, 11, 6, 10, 7, 19, 20, 22, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]<br />
Mutation number:  64   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 22, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]<br />
Mutation number:  65   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 22, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]<br />
Mutation number:  66   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 22, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]<br />
Mutation number:  67   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 22, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]<br />
Mutation number:  68   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 22, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]<br />
Mutation number:  69   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 22, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]<br />
Mutation number:  70   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 22, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]<br />
Mutation number:  71   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 22, 17, 21, 3, 4, 9, 23, 24, 25, 26]<br />
Mutation number:  72   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 22, 21, 3, 4, 9, 23, 24, 25, 26]<br />
Mutation number:  73   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 22, 3, 4, 9, 23, 24, 25, 26]<br />
Mutation number:  74   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 22, 4, 9, 23, 24, 25, 26]<br />
Mutation number:  75   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 22, 9, 23, 24, 25, 26]<br />
Mutation number:  76   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]<br />
Mutation number:  77   [0, 1, 2, 6, 11, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]<br />
Mutation number:  78   [0, 1, 2, 6, 10, 11, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]<br />
Mutation number:  79   [0, 1, 2, 6, 10, 7, 11, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]<br />
Mutation number:  80   [0, 1, 2, 6, 10, 7, 11, 19, 5, 20, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]<br />
Mutation number:  81   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 20, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]<br />
Mutation number:  82   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 20, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]<br />
Mutation number:  83   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 20, 13, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]<br />
Mutation number:  84   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 13, 20, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]<br />
Mutation number:  85   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 13, 14, 20, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]<br />
Mutation number:  86   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 13, 14, 15, 20, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]<br />
Mutation number:  87   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 13, 14, 15, 16, 20, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]<br />
Mutation number:  88   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 13, 14, 15, 16, 17, 20, 21, 3, 4, 9, 22, 23, 24, 25, 26]<br />
Mutation number:  89   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 13, 14, 15, 16, 17, 20, 3, 21, 4, 9, 22, 23, 24, 25, 26]<br />
Mutation number:  90   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 13, 14, 15, 16, 17, 20, 3, 4, 21, 9, 22, 23, 24, 25, 26]<br />
Mutation number:  91   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 13, 14, 15, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  92   [0, 1, 2, 6, 7, 10, 11, 19, 5, 8, 18, 12, 13, 14, 15, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  93   [0, 1, 2, 6, 7, 10, 11, 5, 19, 8, 18, 12, 13, 14, 15, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  94   [0, 1, 2, 6, 7, 10, 11, 5, 8, 19, 18, 12, 13, 14, 15, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  95   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 19, 12, 13, 14, 15, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  96   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 19, 13, 14, 15, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  97   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 13, 19, 14, 15, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  98   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 13, 14, 19, 15, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  99   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 13, 14, 15, 19, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  100   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 13, 14, 15, 16, 19, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  101   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 13, 14, 15, 16, 17, 19, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  102   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 13, 14, 15, 16, 17, 19, 3, 20, 4, 9, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  103   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 13, 14, 15, 16, 17, 19, 3, 4, 20, 9, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  104   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 13, 14, 15, 16, 17, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  105   [0, 1, 2, 6, 7, 10, 5, 11, 8, 18, 12, 13, 14, 15, 16, 17, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  106   [0, 1, 2, 6, 7, 10, 5, 8, 11, 18, 12, 13, 14, 15, 16, 17, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  107   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 18, 13, 14, 15, 16, 17, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  108   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 13, 18, 14, 15, 16, 17, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  109   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 13, 14, 18, 15, 16, 17, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  110   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 13, 14, 15, 18, 16, 17, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  111   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 13, 14, 15, 16, 18, 17, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  112   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  113   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 13, 14, 15, 16, 17, 18, 3, 19, 4, 9, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  114   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 13, 14, 15, 16, 17, 18, 3, 4, 19, 9, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  115   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 13, 14, 15, 16, 17, 18, 3, 4, 9, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  116   [0, 1, 2, 6, 7, 5, 10, 8, 11, 12, 13, 14, 15, 16, 17, 18, 3, 4, 9, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  117   [0, 1, 2, 6, 7, 5, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 3, 4, 9, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  118   [0, 1, 2, 6, 7, 5, 8, 10, 11, 12, 13, 14, 15, 16, 17, 3, 18, 4, 9, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  119   [0, 1, 2, 6, 7, 5, 8, 10, 11, 12, 13, 14, 15, 16, 17, 3, 4, 18, 9, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  120   [0, 1, 2, 6, 7, 5, 8, 10, 11, 12, 13, 14, 15, 16, 17, 3, 4, 9, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  121   [0, 1, 2, 6, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 3, 4, 9, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  122   [0, 1, 2, 6, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 3, 17, 4, 9, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  123   [0, 1, 2, 6, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 3, 4, 17, 9, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  124   [0, 1, 2, 6, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 3, 4, 9, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  125   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 3, 4, 9, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  126   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 3, 16, 4, 9, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  127   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 3, 4, 16, 9, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  128   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 3, 4, 9, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  129   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 14, 3, 15, 4, 9, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  130   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 14, 3, 4, 15, 9, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  131   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 14, 3, 4, 9, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  132   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 3, 14, 4, 9, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  133   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 3, 4, 14, 9, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  134   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 3, 4, 9, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  135   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 3, 13, 4, 9, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  136   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 3, 4, 13, 9, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  137   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 3, 4, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  138   [0, 1, 2, 5, 6, 7, 8, 10, 11, 3, 12, 4, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  139   [0, 1, 2, 5, 6, 7, 8, 10, 11, 3, 4, 12, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  140   [0, 1, 2, 5, 6, 7, 8, 10, 11, 3, 4, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  141   [0, 1, 2, 5, 6, 7, 8, 10, 3, 11, 4, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  142   [0, 1, 2, 5, 6, 7, 8, 10, 3, 4, 11, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  143   [0, 1, 2, 5, 6, 7, 8, 10, 3, 4, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  144   [0, 1, 2, 5, 6, 7, 8, 3, 10, 4, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  145   [0, 1, 2, 5, 6, 7, 8, 3, 4, 10, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  146   [0, 1, 2, 5, 6, 7, 8, 3, 4, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  147   [0, 1, 2, 5, 6, 7, 3, 8, 4, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  148   [0, 1, 2, 5, 6, 7, 3, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  149   [0, 1, 2, 5, 6, 3, 7, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  150   [0, 1, 2, 5, 6, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  151   [0, 1, 2, 5, 3, 6, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  152   [0, 1, 2, 5, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  153   [0, 1, 2, 3, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
Mutation number:  154   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
__Your genome has been solved in  154  mutations!__

#### Greedy
Greedy vindt voor het Melanogaster genoom in een minimale tijd (< 1 sec) een sequentie van __14 mutaties__ die het genoom van D. Melanogaster naar die van D. Miranda verandert. Een grote verbetering ten opzichte van Bubble Sort (154 mutaties)!

GREEDY ALGORITHM STARTS<br />
<br />
Mutation number:  1   [0, 23, 1, 2, 11, 24, 22, 19, 20, 25, 7, 10, 6, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutation number:  2   [0, 23, 1, 2, 11, 24, 22, 19, 20, 25, 7, 10, 6, 5, 4, 3, 21, 17, 16, 15, 14, 13, 12, 18, 8, 9, 26]<br />
Mutation number:  3   [0, 23, 1, 2, 11, 24, 22, 19, 20, 25, 7, 10, 6, 5, 4, 3, 21, 12, 13, 14, 15, 16, 17, 18, 8, 9, 26]<br />
Mutation number:  4   [0, 23, 1, 2, 11, 24, 22, 19, 20, 25, 7, 10, 9, 8, 18, 17, 16, 15, 14, 13, 12, 21, 3, 4, 5, 6, 26]<br />
Mutation number:  5   [0, 23, 1, 2, 11, 24, 22, 19, 20, 25, 7, 6, 5, 4, 3, 21, 12, 13, 14, 15, 16, 17, 18, 8, 9, 10, 26]<br />
Mutation number:  6   [0, 23, 1, 2, 11, 24, 22, 19, 20, 25, 18, 17, 16, 15, 14, 13, 12, 21, 3, 4, 5, 6, 7, 8, 9, 10, 26]<br />
Mutation number:  7   [0, 23, 1, 2, 11, 24, 22, 19, 20, 10, 9, 8, 7, 6, 5, 4, 3, 21, 12, 13, 14, 15, 16, 17, 18, 25, 26]<br />
Mutation number:  8   [0, 23, 1, 2, 11, 24, 22, 21, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 12, 13, 14, 15, 16, 17, 18, 25, 26]<br />
Mutation number:  9   [0, 23, 1, 2, 11, 24, 22, 21, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 25, 26]<br />
Mutation number:  10   [0, 23, 1, 2, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10, 9, 8, 7, 6, 5, 4, 3, 21, 22, 24, 25, 26]<br />
Mutation number:  11   [0, 23, 1, 2, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 21, 22, 24, 25, 26]<br />
Mutation number:  12   [0, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26]<br />
Mutation number:  13   [0, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 24, 25, 26]<br />
Mutation number:  14   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]<br />
__Your genome has been solved in  14  mutations!__

### Challenge b) Vind de "kortste" sequentie van mutaties dat het genoom van D. Melanogaster in het genoom van D. Miranda verandert. Als er meerdere kortste oplossingen zijn, vergelijk ze dan met elkaar.

#### Branch and Bound
Zoals uitgelegd op de vorige pagina is het probleem met Greedy dat je niet zeker weet of de kortste sequentie mutaties gevonden is. Om daadwerkelijk de kortste sequentie mutaties te vinden gebruiken wij het exhaustive Branch and Bound algoritme, dat _gegarandeerd_ de kortste sequentie mutaties vindt.<br />
Omdat de run-time van het Branch and Bound algoritme voor grote genomen extreem lang is, hebben wij het Branch and Bound algoritme voor het Melanogaster genoom niet volledig kunnen laten draaien. De run-time van het Branch and Bound algoritme is positief gecorreleerd met het aantal breakpoints in het originele genoom. Immers, meer breakpoints genereren meer opties om uit te voeren en dus een grotere boom die meer tijd kost om te doorlopen. Zie hier een scatter-plot die deze positieve correlatie weergeeft. De genomen zijn random gegenereerd voor lengte 2 tot en met 14. Voor elke lengte zijn er 100 genomen gegenereerd. De tijd is weergeven in seconden.
![alt text](https://github.com/madmax1000/Heuristieken/blob/master/Results/Images/BnB-RunTimePerBreakpoint1.png)

In de onderstaande scatter-plot is wederom te zien hoe het aantal breakpoints in het originele genoom zich verhoudt tot het minimale aantal mutatie stappen die uitgevoerd moeten worden om het genoom op te lossen. Aangezien voor het genereren van deze plot het Branch and Bound algoritme is gebruikt, weten we zeker dat dit daadwerkelijk het _minimale_ aantal mutaties is dat uitgevoerd moest worden voor dat specifieke genoom van een bepaalde lengte. 
![alt text](https://github.com/madmax1000/Heuristieken/blob/master/Results/Images/Number%20of%20breakpoints%20in%20ori%20genome%20per%20mutation%20steps%20till%20completion.png)

#### Random-Greedy-Branch and Bound
Dit algoritme gebruikt gedeeltelijk Greedy en gedeeltelijk Branch and Bound. Zo wordt de run-time drastisch versneld en wordt het exhaustive aspect van het Branch and Bound algoritme nog steeds deels benut. </br>
De threshold voor de inzet van het Branch and Bound algoritme hebben wij gezet op 8 breakpoints. Dat betekent dat Greedy wordt uitgevoerd totdat er nog slechts 8 breakpoints over zijn. Vervolgens wordt het genoom verder gemuteerd met Branch and Bound. Zie de vorige pagina voor een uitgebreide uitleg. <br />
Dit algoritme vindt in een zeer geringe tijd (< 3 sec) voor het Melanogaster genoom met 150 iteraties meerdere sequenties van __13 mutaties__. Dit is dus een verbetering ten opzichte van het Greedy algoritme en tevens onze beste oplossing! Éen van deze oplossingen is hier onder weergeven in de vorm (i, j): <br />

RANDOM - GREEDY - BRANCH AND BOUND ALGORITHM STARTS<br />
<br />
Greedy part: (8, 12) (14, 24), (17, 22), (12, 25), (7, 13), (11, 25), (16, 24), (5, 24), (4, 19), (2, 23) <br />
Branch and Bound part: (1, 23), (3, 7), (8, 21) <br />
__Your genome has been solved in  13  mutations!__

<br />
Om een indicatie te geven van het aantal iteraties dat nodig is voor het algoritme om een sequentie van 13 mutaties te vinden, hebben we het Melanogaster genoom duizend keer opgelost met 150 iteraties. Hier onder is een histogram weergeven dat laat zien op welke iteratie er een oplossing van 13 mutaties is gevonden. 
![alt text](https://github.com/madmax1000/Heuristieken/blob/master/Results/Images/13.png)

Het moge dus duidelijk zijn dat dit algoritme beter is dan het Greedy algoritme, aangezien er een kortere sequentie van mutaties wordt gevonden. Een algemeen voordeel van dit algoritme is dat de lengte van het genoom nauwelijks invloed heeft op de run-time. Dit komt omdat de lengte van het genoom nauwelijks invloed heeft op de run-time van het Greedy gedeelte, en het Branch and Bound gedeelte pas begint vanaf een bepaalde threshold, waardoor het Branch and Bound gedeelte óók ongeveer dezelfde run-time blijft behouden!

#### Greedy Points
Greedy vindt voor het Melanogaster genoom met __score functie n__ in een minimale tijd (< 1 sec) een sequentie mutaties van totaal __100 punten__ die het genoom van D. Melanogaster naar die van D. Miranda verandert. <br />

GREEDY POINTS ALGORITHM STARTS<br />
<br />
Your original genome looks like:  [0, 23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutated genome:  [0, 23, 1, 2, 11, 24, 22, 19, 10, 6, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+ 2  points)<br />
Mutated genome:  [0, 11, 2, 1, 23, 24, 22, 19, 10, 6, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+ 4  points)<br />
Mutated genome:  [0, 11, 2, 1, 24, 23, 22, 19, 10, 6, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+ 2  points)<br />
Mutated genome:  [0, 1, 2, 11, 24, 23, 22, 19, 10, 6, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+ 3  points)<br />
Mutated genome:  [0, 1, 2, 11, 24, 23, 22, 19, 10, 20, 25, 7, 6, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+ 4  points)<br />
Mutated genome:  [0, 1, 2, 11, 24, 23, 22, 10, 19, 20, 25, 7, 6, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+ 2  points)<br />
Mutated genome:  [0, 1, 2, 11, 24, 23, 22, 10, 19, 20, 25, 5, 6, 7, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+ 3  points)<br />
Mutated genome:  [0, 1, 2, 22, 23, 24, 11, 10, 19, 20, 25, 5, 6, 7, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+ 4  points)<br />
Mutated genome:  [0, 1, 2, 22, 23, 24, 25, 20, 19, 10, 11, 5, 6, 7, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+ 5  points)<br />
Mutated genome:  [0, 1, 2, 22, 23, 24, 25, 20, 19, 10, 11, 5, 6, 7, 8, 18, 17, 16, 15, 14, 13, 12, 21, 3, 4, 9, 26] (+ 6  points)<br />
Mutated genome:  [0, 1, 2, 22, 23, 24, 25, 20, 19, 10, 11, 12, 13, 14, 15, 16, 17, 18, 8, 7, 6, 5, 21, 3, 4, 9, 26] (+ 11  points)<br />
Mutated genome:  [0, 1, 2, 22, 23, 24, 25, 20, 19, 10, 11, 12, 13, 14, 15, 16, 17, 18, 8, 7, 6, 5, 4, 3, 21, 9, 26] (+ 3  points)<br />
Mutated genome:  [0, 1, 2, 22, 23, 24, 25, 20, 19, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 3, 4, 5, 6, 7, 8, 9, 26] (+ 7  points)<br />
Mutated genome:  [0, 1, 2, 22, 23, 24, 25, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 21, 3, 4, 5, 6, 7, 8, 9, 26] (+ 9  points)<br />
Mutated genome:  [0, 1, 2, 22, 23, 24, 25, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 21, 26] (+ 8  points)<br />
Mutated genome:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 24, 23, 22, 21, 26] (+ 22  points)<br />
Mutated genome:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26] (+ 5  points)<br />
__Your genome has been solved with a total of  100 points.__

Greedy vindt voor het Melanogaster genoom met __score functie 1/2 n^2__ in een minimale tijd (< 1 sec) een sequentie mutaties van totaal __486 punten__ die het genoom van D. Melanogaster naar die van D. Miranda verandert. <br />

GREEDY POINTS ALGORITHM STARTS<br />
<br />
Your original genome looks like:  [0, 23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]<br />
Mutated genome:  [0, 23, 1, 2, 11, 24, 22, 19, 10, 6, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+  2.0  points)<br />
Mutated genome:  [0, 11, 2, 1, 23, 24, 22, 19, 10, 6, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+  8.0  points)<br />
Mutated genome:  [0, 11, 2, 1, 24, 23, 22, 19, 10, 6, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+  2.0  points)<br />
Mutated genome:  [0, 1, 2, 11, 24, 23, 22, 19, 10, 6, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+  4.5  points)<br />
Mutated genome:  [0, 1, 2, 11, 24, 23, 22, 19, 10, 20, 25, 7, 6, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+  8.0  points)<br />
Mutated genome:  [0, 1, 2, 11, 24, 23, 22, 10, 19, 20, 25, 7, 6, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+  2.0  points)<br />
Mutated genome:  [0, 1, 2, 11, 24, 23, 22, 10, 19, 20, 25, 5, 6, 7, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+  4.5  points)<br />
Mutated genome:  [0, 1, 2, 22, 23, 24, 11, 10, 19, 20, 25, 5, 6, 7, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+  8.0  points)<br />
Mutated genome:  [0, 1, 2, 22, 23, 24, 25, 20, 19, 10, 11, 5, 6, 7, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26] (+  12.5  points)<br />
Mutated genome:  [0, 1, 2, 22, 23, 24, 25, 20, 19, 10, 11, 5, 6, 7, 8, 18, 17, 16, 15, 14, 13, 12, 21, 3, 4, 9, 26] (+  18.0  points)<br />
Mutated genome:  [0, 1, 2, 22, 23, 24, 25, 20, 19, 10, 11, 12, 13, 14, 15, 16, 17, 18, 8, 7, 6, 5, 21, 3, 4, 9, 26] (+  60.5  points)<br />
Mutated genome:  [0, 1, 2, 22, 23, 24, 25, 20, 19, 10, 11, 12, 13, 14, 15, 16, 17, 18, 8, 7, 6, 5, 4, 3, 21, 9, 26] (+  4.5  points)<br />
Mutated genome:  [0, 1, 2, 22, 23, 24, 25, 20, 19, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 3, 4, 5, 6, 7, 8, 9, 26] (+  24.5  points)<br />
Mutated genome:  [0, 1, 2, 22, 23, 24, 25, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 21, 3, 4, 5, 6, 7, 8, 9, 26] (+  40.5  points)<br />
Mutated genome:  [0, 1, 2, 22, 23, 24, 25, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 21, 26] (+  32.0  points)<br />
Mutated genome:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 24, 23, 22, 21, 26] (+  242.0  points)<br />
Mutated genome:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26] (+  12.5  points)<br />
__Your genome has been solved with a total of  486.0 points.__


#### Random-Greedy Points

Zoals vermeld op de vorige pagina, gebruiken we twee kansverdelingen tijdens de random keuze die meerdere keren wordt uitgevoerd in dit algoritme: de uniforme kansverdeling, en de triangular kansverdeling. Onze hoop was dat het gebruik van de triangular kansverdeling de run-time van het algoritme versnelt. In de onderstaande plots is te zien dat dit voor dit specifieke geval inderdaad zo is.
<br />
Voor scorefunctie __n__:
<p float="center">
  <img src="https://github.com/madmax1000/Heuristieken/blob/master/Results/Images/uniform%20500%20n.png" width="350" title="Uniform" />
  <img src="https://github.com/madmax1000/Heuristieken/blob/master/Results/Images/non-uniform%20500%20n.png" width="350" title="Triangular" /> 
</p>

Voor scorefunctie __1/2 n^2__:
<p float="center">
  <img src="https://github.com/madmax1000/Heuristieken/blob/master/Results/Images/uniform%20500%2012n2.png" width="350" />
  <img src="https://github.com/madmax1000/Heuristieken/blob/master/Results/Images/non-uniform%20500%2012n2.png" width="350" /> 
</p>
