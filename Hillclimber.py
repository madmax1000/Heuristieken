import helpers
import GenomeSequence as genomeClass
import copy
from random import shuffle
import random

def randomMutation(testLength):
    middleGenome = [i for i in range(1, testLength)]
    shuffle(middleGenome)
    return [0] + middleGenome + [testLength]

current = [0] * 32
best = []
#melanoGenome = [0,23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9,26]
melanoGenome = [0,8,5,7,4,2,6,3,1,9]
#melanoGenome = randomMutation(12)


genomeObject = genomeClass.GenomeSequence(melanoGenome)
mirandaGenome = [i for i in range(len(melanoGenome))]
numberOfMutations = 0
history = []
while genomeObject.genome != mirandaGenome:
    numberOfMutations += 1
    genomeObject.genome, i, j, deltaPHI = genomeObject.Mutate("Greedy")
    history.append([i, j, deltaPHI])
    print("Mutation number: ", numberOfMutations, " ", genomeObject.genome)
print("Your genome has been solved in ", numberOfMutations, " mutations!")
# verschillende start sequenties
x = 0

while x < 10:
    x = x + 1
    # niet int
    mutationsLocation = random.randint(0,len(history) - 1)
    genomeObject.genome = melanoGenome
    for mutation in history[:mutationsLocation]:
        genomeObject.genome = genomeObject.Reverse(mutation[0], mutation[1])
    optionList = genomeObject.Mutate("B&B")
    rng = random.random()
    if rng < 0.7 and len(optionList[0]) > 0:
        selectedList = optionList[0]
    else:
        selectedList = optionList[1]
    selectedMutation = random.choice(selectedList)

    genomeObject.genome = genomeObject.Reverse(selectedMutation[0], selectedMutation[1])

    genomeObject.createBreakpointList(genomeObject.genome)

    history = []
    # keep track of the number of mutations
    numberOfMutations = 0

    # Execute Greedy until the genomes are equal
    while genomeObject.breakpointPairs > 15:
        numberOfMutations += 1
        genome, i, j, deltaPHI = genomeObject.Mutate("Greedy")
        history.append([i, j, deltaPHI])
        print("Mutation number: ", numberOfMutations, " ", genomeObject.genome)
        
    current = [0] * 32
    best = []

    # initialize genomeObject with its breakpointPairs
    breakpointPairs = genomeObject.breakpointPairs

    # start Branch and Bound!
    upperBound, current, best = helpers.BnB(genomeObject, 0, 30, current, best, breakpointPairs, mirandaGenome)

    # store the shortest sequence of mutations
    best = best[:upperBound]

    print("\nThe Branch and Bound algorithm has finished. The shortest solution possibile equals ", len(best))
    print("Your original genome equals: ", genomeObject.genome)
    print("The shortest sequence of mutations (i,j) equals: ", best)
    print("Executing this very sequence of mutations on the original genome results in the following intermediate genomes: ")

    numberOfMutations = 0
    for mutation in best:
        numberOfMutations += 1
        genomeObject.genome = genomeObject.Reverse(mutation[0], mutation[1])
        print("Mutation number: ", numberOfMutations, " ", genomeObject.genome)

    print("Your genome has been solved in ", numberOfMutations, " mutations!")
    