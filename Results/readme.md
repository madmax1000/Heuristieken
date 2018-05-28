# Results
Hier zijn de resultaten van elk van de challenges beschreven. Ook zijn er grafieken toegevoegd om de resultaten te visualiseren. 

### Challenge a) Bepaal een sequentie van mutaties dat het genoom van D. Melanogaster in het genoom van D. Miranda verandert. Bepaal ook de grenzen van de oplossingskwaliteit en de toestandsruimte.
Voor deze challenge hebben we het Bubble Sort algoritme en het Greedy algoritme gebruikt. Zie voor een beschrijving van het Greedy algoritme de README.md file op de vorige pagina. Wij gaan er van uit dat het Bubble Sort algorimte bekend is bij de lezer. 

#### Bubble Sort

BUBBLE ALGORITHM STARTS

Mutation number:  1   [0, 1, 23, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]
Mutation number:  2   [0, 1, 2, 23, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]
Mutation number:  3   [0, 1, 2, 11, 23, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]
Mutation number:  4   [0, 1, 2, 11, 23, 22, 24, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]
Mutation number:  5   [0, 1, 2, 11, 23, 22, 19, 24, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]
Mutation number:  6   [0, 1, 2, 11, 23, 22, 19, 6, 24, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]
Mutation number:  7   [0, 1, 2, 11, 23, 22, 19, 6, 10, 24, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]
Mutation number:  8   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]
Mutation number:  9   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 25, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]
Mutation number:  10   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 25, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]
Mutation number:  11   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 25, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]
Mutation number:  12   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 25, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]
Mutation number:  13   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 25, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]
Mutation number:  14   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 25, 14, 15, 16, 17, 21, 3, 4, 9, 26]
Mutation number:  15   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 25, 15, 16, 17, 21, 3, 4, 9, 26]
Mutation number:  16   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 25, 16, 17, 21, 3, 4, 9, 26]
Mutation number:  17   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 25, 17, 21, 3, 4, 9, 26]
Mutation number:  18   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 25, 21, 3, 4, 9, 26]
Mutation number:  19   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 25, 3, 4, 9, 26]
Mutation number:  20   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 25, 4, 9, 26]
Mutation number:  21   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 25, 9, 26]
Mutation number:  22   [0, 1, 2, 11, 23, 22, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]
Mutation number:  23   [0, 1, 2, 11, 22, 23, 19, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]
Mutation number:  24   [0, 1, 2, 11, 22, 19, 23, 6, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]
Mutation number:  25   [0, 1, 2, 11, 22, 19, 6, 23, 10, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]
Mutation number:  26   [0, 1, 2, 11, 22, 19, 6, 10, 23, 7, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]
Mutation number:  27   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 24, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]
Mutation number:  28   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 24, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]
Mutation number:  29   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 24, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]
Mutation number:  30   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 24, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]
Mutation number:  31   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 24, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]
Mutation number:  32   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 24, 13, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]
Mutation number:  33   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 24, 14, 15, 16, 17, 21, 3, 4, 9, 25, 26]
Mutation number:  34   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 24, 15, 16, 17, 21, 3, 4, 9, 25, 26]
Mutation number:  35   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 24, 16, 17, 21, 3, 4, 9, 25, 26]
Mutation number:  36   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 24, 17, 21, 3, 4, 9, 25, 26]
Mutation number:  37   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 24, 21, 3, 4, 9, 25, 26]
Mutation number:  38   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 24, 3, 4, 9, 25, 26]
Mutation number:  39   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 24, 4, 9, 25, 26]
Mutation number:  40   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 24, 9, 25, 26]
Mutation number:  41   [0, 1, 2, 11, 22, 19, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]
Mutation number:  42   [0, 1, 2, 11, 19, 22, 6, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]
Mutation number:  43   [0, 1, 2, 11, 19, 6, 22, 10, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]
Mutation number:  44   [0, 1, 2, 11, 19, 6, 10, 22, 7, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]
Mutation number:  45   [0, 1, 2, 11, 19, 6, 10, 7, 22, 23, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]
Mutation number:  46   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 23, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]
Mutation number:  47   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 23, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]
Mutation number:  48   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 23, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]
Mutation number:  49   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 23, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]
Mutation number:  50   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 23, 13, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]
Mutation number:  51   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 23, 14, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]
Mutation number:  52   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 23, 15, 16, 17, 21, 3, 4, 9, 24, 25, 26]
Mutation number:  53   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 23, 16, 17, 21, 3, 4, 9, 24, 25, 26]
Mutation number:  54   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 23, 17, 21, 3, 4, 9, 24, 25, 26]
Mutation number:  55   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 23, 21, 3, 4, 9, 24, 25, 26]
Mutation number:  56   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 23, 3, 4, 9, 24, 25, 26]
Mutation number:  57   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 23, 4, 9, 24, 25, 26]
Mutation number:  58   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 23, 9, 24, 25, 26]
Mutation number:  59   [0, 1, 2, 11, 19, 6, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]
Mutation number:  60   [0, 1, 2, 11, 6, 19, 10, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]
Mutation number:  61   [0, 1, 2, 11, 6, 10, 19, 7, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]
Mutation number:  62   [0, 1, 2, 11, 6, 10, 7, 19, 22, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]
Mutation number:  63   [0, 1, 2, 11, 6, 10, 7, 19, 20, 22, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]
Mutation number:  64   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 22, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]
Mutation number:  65   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 22, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]
Mutation number:  66   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 22, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]
Mutation number:  67   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 22, 13, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]
Mutation number:  68   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 22, 14, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]
Mutation number:  69   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 22, 15, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]
Mutation number:  70   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 22, 16, 17, 21, 3, 4, 9, 23, 24, 25, 26]
Mutation number:  71   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 22, 17, 21, 3, 4, 9, 23, 24, 25, 26]
Mutation number:  72   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 22, 21, 3, 4, 9, 23, 24, 25, 26]
Mutation number:  73   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 22, 3, 4, 9, 23, 24, 25, 26]
Mutation number:  74   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 22, 4, 9, 23, 24, 25, 26]
Mutation number:  75   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 22, 9, 23, 24, 25, 26]
Mutation number:  76   [0, 1, 2, 11, 6, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]
Mutation number:  77   [0, 1, 2, 6, 11, 10, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]
Mutation number:  78   [0, 1, 2, 6, 10, 11, 7, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]
Mutation number:  79   [0, 1, 2, 6, 10, 7, 11, 19, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]
Mutation number:  80   [0, 1, 2, 6, 10, 7, 11, 19, 5, 20, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]
Mutation number:  81   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 20, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]
Mutation number:  82   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 20, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]
Mutation number:  83   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 20, 13, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]
Mutation number:  84   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 13, 20, 14, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]
Mutation number:  85   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 13, 14, 20, 15, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]
Mutation number:  86   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 13, 14, 15, 20, 16, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]
Mutation number:  87   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 13, 14, 15, 16, 20, 17, 21, 3, 4, 9, 22, 23, 24, 25, 26]
Mutation number:  88   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 13, 14, 15, 16, 17, 20, 21, 3, 4, 9, 22, 23, 24, 25, 26]
Mutation number:  89   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 13, 14, 15, 16, 17, 20, 3, 21, 4, 9, 22, 23, 24, 25, 26]
Mutation number:  90   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 13, 14, 15, 16, 17, 20, 3, 4, 21, 9, 22, 23, 24, 25, 26]
Mutation number:  91   [0, 1, 2, 6, 10, 7, 11, 19, 5, 8, 18, 12, 13, 14, 15, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]
Mutation number:  92   [0, 1, 2, 6, 7, 10, 11, 19, 5, 8, 18, 12, 13, 14, 15, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]
Mutation number:  93   [0, 1, 2, 6, 7, 10, 11, 5, 19, 8, 18, 12, 13, 14, 15, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]
Mutation number:  94   [0, 1, 2, 6, 7, 10, 11, 5, 8, 19, 18, 12, 13, 14, 15, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]
Mutation number:  95   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 19, 12, 13, 14, 15, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]
Mutation number:  96   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 19, 13, 14, 15, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]
Mutation number:  97   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 13, 19, 14, 15, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]
Mutation number:  98   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 13, 14, 19, 15, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]
Mutation number:  99   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 13, 14, 15, 19, 16, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]
Mutation number:  100   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 13, 14, 15, 16, 19, 17, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]
Mutation number:  101   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 13, 14, 15, 16, 17, 19, 20, 3, 4, 9, 21, 22, 23, 24, 25, 26]
Mutation number:  102   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 13, 14, 15, 16, 17, 19, 3, 20, 4, 9, 21, 22, 23, 24, 25, 26]
Mutation number:  103   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 13, 14, 15, 16, 17, 19, 3, 4, 20, 9, 21, 22, 23, 24, 25, 26]
Mutation number:  104   [0, 1, 2, 6, 7, 10, 11, 5, 8, 18, 12, 13, 14, 15, 16, 17, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  105   [0, 1, 2, 6, 7, 10, 5, 11, 8, 18, 12, 13, 14, 15, 16, 17, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  106   [0, 1, 2, 6, 7, 10, 5, 8, 11, 18, 12, 13, 14, 15, 16, 17, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  107   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 18, 13, 14, 15, 16, 17, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  108   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 13, 18, 14, 15, 16, 17, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  109   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 13, 14, 18, 15, 16, 17, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  110   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 13, 14, 15, 18, 16, 17, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  111   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 13, 14, 15, 16, 18, 17, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  112   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19, 3, 4, 9, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  113   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 13, 14, 15, 16, 17, 18, 3, 19, 4, 9, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  114   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 13, 14, 15, 16, 17, 18, 3, 4, 19, 9, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  115   [0, 1, 2, 6, 7, 10, 5, 8, 11, 12, 13, 14, 15, 16, 17, 18, 3, 4, 9, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  116   [0, 1, 2, 6, 7, 5, 10, 8, 11, 12, 13, 14, 15, 16, 17, 18, 3, 4, 9, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  117   [0, 1, 2, 6, 7, 5, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 3, 4, 9, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  118   [0, 1, 2, 6, 7, 5, 8, 10, 11, 12, 13, 14, 15, 16, 17, 3, 18, 4, 9, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  119   [0, 1, 2, 6, 7, 5, 8, 10, 11, 12, 13, 14, 15, 16, 17, 3, 4, 18, 9, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  120   [0, 1, 2, 6, 7, 5, 8, 10, 11, 12, 13, 14, 15, 16, 17, 3, 4, 9, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  121   [0, 1, 2, 6, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 3, 4, 9, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  122   [0, 1, 2, 6, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 3, 17, 4, 9, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  123   [0, 1, 2, 6, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 3, 4, 17, 9, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  124   [0, 1, 2, 6, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 3, 4, 9, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  125   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 3, 4, 9, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  126   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 3, 16, 4, 9, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  127   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 3, 4, 16, 9, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  128   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 3, 4, 9, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  129   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 14, 3, 15, 4, 9, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  130   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 14, 3, 4, 15, 9, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  131   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 14, 3, 4, 9, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  132   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 3, 14, 4, 9, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  133   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 3, 4, 14, 9, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  134   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 13, 3, 4, 9, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  135   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 3, 13, 4, 9, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  136   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 3, 4, 13, 9, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  137   [0, 1, 2, 5, 6, 7, 8, 10, 11, 12, 3, 4, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  138   [0, 1, 2, 5, 6, 7, 8, 10, 11, 3, 12, 4, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  139   [0, 1, 2, 5, 6, 7, 8, 10, 11, 3, 4, 12, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  140   [0, 1, 2, 5, 6, 7, 8, 10, 11, 3, 4, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  141   [0, 1, 2, 5, 6, 7, 8, 10, 3, 11, 4, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  142   [0, 1, 2, 5, 6, 7, 8, 10, 3, 4, 11, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  143   [0, 1, 2, 5, 6, 7, 8, 10, 3, 4, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  144   [0, 1, 2, 5, 6, 7, 8, 3, 10, 4, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  145   [0, 1, 2, 5, 6, 7, 8, 3, 4, 10, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  146   [0, 1, 2, 5, 6, 7, 8, 3, 4, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  147   [0, 1, 2, 5, 6, 7, 3, 8, 4, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  148   [0, 1, 2, 5, 6, 7, 3, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  149   [0, 1, 2, 5, 6, 3, 7, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  150   [0, 1, 2, 5, 6, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  151   [0, 1, 2, 5, 3, 6, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  152   [0, 1, 2, 5, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  153   [0, 1, 2, 3, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Mutation number:  154   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
Your genome has been solved in  154  mutations!

#### Greedy
Greedy vindt in een minimale tijd (< 1 sec) een sequentie van __14 mutaties__ die het genoom van D. Melanogaster naar die van D. Miranda verandert. Een grote verbetering ten opzichte van Bubble Sort (154 mutaties)!

### Challenge b) Vind de "kortste" sequentie van mutaties dat het genoom van D. Melanogaster in het genoom van D. Miranda verandert. Als er meerdere kortste oplossingen zijn, vergelijk ze dan met elkaar.

#### Branch and Bound
Zoals uitgelegd op de vorige pagina is het probleem met Greedy dat je niet zeker weet of de kortste sequentie mutaties gevonden is. Om daadwerkelijk de kortste sequentie mutaties te vinden gebruiken wij het exhaustive Branch and Bound algoritme, dat _gegarandeerd_ de kortste sequentie mutaties vindt.<br />
Omdat de run-time van het Branch and Bound algoritme voor grote genomen extreem lang is, hebben wij het Branch and Bound algoritme voor het Melanogaster genoom niet volledig kunnen laten draaien. De run-time van het Branch and Bound algoritme is positief gecorreleerd met het aantal breakpoints in het originele genoom. Immers, meer breakpoints genereren meer opties om uit te voeren en dus een grotere boom die meer tijd kost om te doorlopen. Zie hier een scatter-plot die deze positieve correlatie weergeeft. De tijd is weergeven in seconden.
![alt text](https://github.com/madmax1000/Heuristieken/blob/master/Results/Images/BnB-RunTimePerBreakpoint.png)

In de onderstaande scatter-plot is wederom te zien hoe het aantal breakpoints in het originele genoom zich verhoudt tot het minimale aantal mutatie stappen die uitgevoerd moeten worden om het genoom op te lossen. Aangezien voor het genereren van deze plot het Branch and Bound algoritme is gebruikt, weten we zeker dat dit daadwerkelijk het _minimale_ aantal mutaties is dat uitgevoerd moest worden voor dat specifieke genoom van een bepaalde lengte. 
![alt text](https://github.com/madmax1000/Heuristieken/blob/master/Results/Images/Number%20of%20breakpoints%20in%20ori%20genome%20per%20mutation%20steps%20till%20completion.png)

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
