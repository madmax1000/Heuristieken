import math
from random import shuffle
import copy

# A function for making random mutations for testing purposes
def RandomMutation(length):
    middleGenome = [i for i in range(1, length)]
    shuffle(middleGenome)
    return [0] + middleGenome + [length]

# A function to calculate the lowerBound in the Branch and Bound algorithm
def LowerBound(breakpointpairsCurrent):
    return math.ceil(breakpointpairsCurrent / 2)


# sorts the genome by using the bubble sort algorithm
def Bubblesort(genome):

    sortedPart = 1
    lengthGenome = len(genome)
    targetGenome = [i for i in range(lengthGenome)]

    numberOfMutations = 0

    while genome != targetGenome:
        switch = False
        for i in range(lengthGenome - sortedPart):

            if genome[i] > genome[i + 1]:
                genome[i], genome[i + 1] =  genome[i + 1], genome[i]
                switch = True
                numberOfMutations += 1
                print("Mutation number: ", numberOfMutations, " ", genome)
        sortedPart += 1

    return(numberOfMutations)

# sorts the genome by executing the Branch and Bound algorithm
def BnB(genomeObj, depth, upperBound, current, best, breakpointPairs, targetGenome):
    depth0count = 0

    #print("----------Branch and Bound was started-----------")

    #print("Depth: ", depth)
    #print("upperBound: ", upperBound)
    #print("Current: ", current)
    #print("Best: ", best)

    #print("Our current genome looks like this: ", genomeObj.genome)
    if genomeObj.genome == targetGenome:

        #print("--------------------------------------!The genome has been SOLVED!--------------------------------------")

        if depth <= upperBound:

            #print("!!A new best (upperBound) has been found!!")

            best = []
            upperBound, best = depth, current
            print("Updated upperBound: ", upperBound)
            print("Updated best: ", best)

            #print("Return: upperbound, current, best")


            best = copy.copy(best)
            return upperBound, current, best


    else:
        #print("The genome has not been solved yet.")

        allOptions = genomeObj.Mutate("B&B")

        #print("The optionList equals: ", allOptions)

        for optionList in range(len(allOptions)):
            if depth == 0:
                depth0count += 1
                print("-------------- ROOT. Right now you're in list ", depth0count, "out of 3 --------------")

            optionCount = 0
            #print("Currently revising the optionList with index ", optionList)
            breakpointPairsCurrent = breakpointPairs - abs(optionList - 2)

            lowerBound = LowerBound(breakpointPairsCurrent) + depth + 2
            # print("--Depth = " ,depth)

            if lowerBound <= upperBound:
                for option in allOptions[optionList]:
                    #print("Currently revising option number ", optionCount, ": ", option)
                    # optionCount += 1
                    # if depth == 1:
                    #     print("--Depth = 1, # of options here are: ", len(allOptions[0]) + len(allOptions[1]) + len(allOptions[2]))
                    # if depth == 2:
                    #     print("----Depth = 2, # of options here are: ", len(allOptions[0]) + len(allOptions[1]) + len(allOptions[2]))
                    # if depth == 3:
                    #     print("------Depth = 3, # of options here are: ", len(allOptions[0]) + len(allOptions[1]) + len(allOptions[2]))
                    # if depth == 4:
                    #     print("--------Depth = 4, # of options here are: ", len(allOptions[0]) + len(allOptions[1]) + len(allOptions[2]))
                    # if depth == 5:
                    #     print("----------Depth = 5, # of options here are: ", len(allOptions[0]) + len(allOptions[1]) + len(allOptions[2]))
                    # if depth == 6:
                    #     print("------------Depth = 6, # of options here are: ", len(allOptions[0]) + len(allOptions[1]) + len(allOptions[2]))
                    # if depth == 7:
                    #     print("--------------Depth = 7, # of options here are: ", len(allOptions[0]) + len(allOptions[1]) + len(allOptions[2]))
                    # if depth == 8:
                    #     print("----------------Depth = 8, # of options here are: ", len(allOptions[0]) + len(allOptions[1]) + len(allOptions[2]))
                    # if depth > 8:
                    #     print("----------------------- Deeper than 8...")

                    # check if lowerBound is less OR equal than upperBound.
                    # (we use leq, because the challenge is: if there are MULTIPLE best solutions, compare them)

                    i, j = option[0], option[1]
                    #print("i equals: ", i)
                    #print("j equals: ", j)

                    current[depth] = (i, j)

                    #print("After editing current[depth], current now equals: ", current)

                    genomeObj.genome = genomeObj.Reverse(i, j)

                    #print("After reversing the genome now equals: ", genomeObj.genome)

                    genomeObj.UpdateBreakpointList(i, j)
                    #print("Our breakpointlist is updated and equals: ", genomeObj.breakpointList)

                    #print("We go deeeeeeeepeeeer")

                    upperBound, current, best = BnB(genomeObj, depth + 1, upperBound, current, best, breakpointPairsCurrent, targetGenome)
                    #print("We're out of depth")

                    genomeObj.genome = genomeObj.Reverse(i,j)
                    genomeObj.UpdateBreakpointList(i, j)
                    #print("Our current genome is: einde ", genomeObj.genome)
                    #print("Depth: ", depth)
                    #print("upperBound: ", upperBound)
                    #print("Current: ", current)
                    #print("Best: ", best)
    return upperBound, current, best