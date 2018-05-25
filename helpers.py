import math

import random
from random import shuffle

import copy

import GenomeSequence as genomeClass




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



    # initialize variables

    sortedPart = 1

    lengthGenome = len(genome)

    targetGenome = [i for i in range(lengthGenome)]

    numberOfMutations = 0



    # continue while genome is not sorted

    while genome != targetGenome:

        

        # iterate over unsorted genome

        for i in range(lengthGenome - sortedPart):

            

            # switches two numbers if not in ascending order

            if genome[i] > genome[i + 1]:

                genome[i], genome[i + 1] =  genome[i + 1], genome[i]

                numberOfMutations += 1

                print("Mutation number: ", numberOfMutations, " ", genome)

        

        # increases sortedPart 

        sortedPart += 1



    return(numberOfMutations)



# sorts the genome by executing the Branch and Bound algorithm

def BnB(genomeObj, depth, upperBound, current, best, breakpointPairs, targetGenome):

    

    # shows user BnB was initialized



    # checks genome for new best qualities

    if genomeObj.genome == targetGenome:

        if depth <= upperBound:

            

            # assigns new best and upperbound

            best = []

            upperBound, best = depth, current

            best = copy.copy(best)



            return upperBound, current, best



    # if genome not target genome execute

    else:



        # gets options

        allOptions = genomeObj.MutateBnB()



        # iterates through optionsLists

        for optionList in range(len(allOptions)):

            

            # update breakpointPairsCurrent and lowerBound

            breakpointPairsCurrent = breakpointPairs - abs(optionList - 2)

            lowerBound = LowerBound(breakpointPairsCurrent) + depth + 2

           

            # checks if upperbound is not yet reached

            if lowerBound <= upperBound:



                # itterates through OptionList

                for option in allOptions[optionList]: 



                    # updates i, j and current

                    i, j = option[0], option[1]

                    current[depth] = (i, j)



                    # calles Reverse() and updateBreakpointList()

                    genomeObj.genome = genomeObj.Reverse(i, j)

                    genomeObj.UpdateBreakpointList(i, j)

                    

                    # goes further into the recursion

                    upperBound, current, best = BnB(genomeObj, depth + 1, upperBound, current, best, breakpointPairsCurrent, targetGenome)



                    # Reverses back and updateBreakpointList

                    genomeObj.genome = genomeObj.Reverse(i,j)

                    genomeObj.UpdateBreakpointList(i, j)



    return upperBound, current, best

def Hillclimber(melanoGenome, steps):
    
    branchAndBoundThreshold = 8
    genomeObject = genomeClass.GenomeSequence ( melanoGenome )

    mirandaGenome = [i for i in range ( len ( melanoGenome ) )]



    # initialize numberOfMutations, prevI, prevJ and history

    numberOfMutations = 0

    prevI = -1

    prevJ = -1

    history = []



    # run greedy sequence once

    while genomeObject.genome != mirandaGenome:

        numberOfMutations += 1

        genomeObject.genome, i, j, deltaPHI = genomeObject.MutateGreedy ( prevI, prevJ )

        prevI, prevJ = i, j

        history.append ( [i, j, deltaPHI] )





    # initialize BnBDepth, x and set UpperBound

    BnBDepth = 0

    x = 0 

    bestBound = 26



    # depth on which a random 

    choiceDepth = 0
    x = 0







    # Start Iteration

    while x < int(steps):

        # increase x

        x += 1



        # clear history after choiceDepth

        history = history[:choiceDepth]



        # reset genomeObject

        genomeObject = genomeClass.GenomeSequence(melanoGenome)



        # mutate the genome UNTIL the specified depth

        for mutation in history[:choiceDepth]:



            # execute the mutations, update breakpointList and number of genomeObject.breakpointPairs

            genomeObject.genome = genomeObject.Reverse(mutation[0], mutation[1])

            genomeObject.UpdateBreakpointList(mutation[0], mutation[1])

            genomeObject.breakpointPairs -= mutation[2]

        



        # at CURRENT depth, check all options

        optionList = genomeObject.MutateBnB()

        



        # select a RANDOM optionList (either eliminate 2 breakpoints or 1 breakpoint) with preference for the list of remove 2 breakpoints

        rng = random.random()

        if (rng < 0.7 and len(optionList[0]) > 0) or (len(optionList[1]) == 0 and len(optionList[2]) == 0):

            selectedList = optionList[0]



            # you know that you're going to eliminate 2 breakpoints!

            genomeObject.breakpointPairs -= 2



            # save deltaPHI to update history a few lines below

            historyPHI = 2



        elif len(optionList[1]) > 0 or len(optionList[2]) == 0:

            selectedList = optionList[1]



            # you know that you're going to eliminate 1 breakpoint!

            genomeObject.breakpointPairs -= 1



            # save deltaPHI to update history a few lines below

            historyPHI = 1



        else:

            selectedList = optionList[2]

            historyPHI = 0



        # select a RANDOM mutation from the selected optionList

        if len(selectedList) > 1:

            selectedMutation = random.choice(selectedList)

        else:

            selectedMutation = selectedList[0]



        # execute the just selected mutation (no need to update the genomeObject.breakpointPairs; already done a few lines above)

        genomeObject.genome = genomeObject.Reverse(selectedMutation[0], selectedMutation[1])

        genomeObject.UpdateBreakpointList(selectedMutation[0], selectedMutation[1])



        # update the history with historyPHI from a few lines above

        history.append([selectedMutation[0], selectedMutation[1], historyPHI])





        # -------- GREEDY PART --------



        # set prevI, PrevJ and breakPointPairss

        prevI = selectedMutation[0]

        prevJ = selectedMutation[1]



        # Execute Greedy until the number of genomeObject.breakpointPairs threshold has been reached

        while  genomeObject.breakpointPairs > branchAndBoundThreshold:

            genomeObject.genome, i, j, deltaPHI = genomeObject.MutateGreedy ( prevI, prevJ )

            genomeObject.UpdateBreakpointList(i, j)

            prevI, prevJ = i, j

            genomeObject.breakpointPairs -= deltaPHI

            history.append([i, j, deltaPHI])





        # -------- BRANCH AND BOUND PART --------



        # Set BnBDepth

        BnBDepth = len(history)

        choiceDepth += 1

        

        # resets choiceDepth 

        if choiceDepth >= BnBDepth:

            choiceDepth = 0



        # initialize empty arrays

        current = [0] * 32

        best = []

        

        # start Branch and Bound!

        genomeObject.createBreakpointList(genomeObject.genome)



        # upperbound for part  in branch and bound

        boundForBnB = bestBound - len(history) + 1

        upperBound, current, best = BnB(genomeObject, 0, boundForBnB, current, best, genomeObject.breakpointPairs, mirandaGenome)



        

        # store best number of mutations 

        best = best[:upperBound]



        # total length of best mutation list

        totalLength = len(history) + len(best)



        # resets number of mutations resets genome

        numberOfMutations = 0

        genomeObject = genomeClass.GenomeSequence(melanoGenome)



        # walkes through all mutations to get final genome and counts number of mutations 

        for mutation in history:

            numberOfMutations += 1

            genomeObject.genome = genomeObject.Reverse(mutation[0], mutation[1])



        for mutation in best:

            numberOfMutations += 1

            genomeObject.genome = genomeObject.Reverse(mutation[0], mutation[1])



        # checks for invalid solution

        if best == [] and genomeObject.genome != mirandaGenome:

            continue



        # prints valid solution and extra information

        print("History looks like: ", history)

        print("Best looks like: ", best)

        print("Genome after mutation: ", genomeObject.genome)

        print("Your genome has been solved in ", numberOfMutations, " mutations!")



        # adjusts bestBound

        if bestBound > totalLength:

            bestBound = totalLength

            

    # print final best number of mutations
    print("Best number of mutations overall", bestBound)

def HillclimberPoints(originalGenome, iterations, scoreFunction):
    # instantiate the genome
    genome = originalGenome
    genomeObject = genomeClass.GenomeSequence(genome)
    targetGenome = [i for i in range(len(genome))]

    # initialize variables
    totalPoints = 0
    upperBound = 0
    genomeHistory = [genome]
    pointHistory = [totalPoints]

    # Execute Greedy for the first time
    while genome != targetGenome:
        genomeObject = genomeClass.GenomeSequence ( genome )
        genome, currentLengthPoints = genomeObject.MutateGreedyPoints ( hillclimberBoolean=False, normalScoreFunction=scoreFunction )
        totalPoints += currentLengthPoints
        genomeHistory.append(genome)
        pointHistory.append(currentLengthPoints)

    # set the new upperBound for points
    upperBound = totalPoints
    print("Old upperBound: ", totalPoints)

    bestGenomeHistory = genomeHistory
    bestPointHistory = pointHistory

    for iter in range(0, iterations):
        print("\n************************ NEW ITERATION WITH UPPERBOUND: ", upperBound, "POINTS. ************************")

        # Start hillclimber

        # Instantiate the genome again
        genome = originalGenome
        genomeObject = genomeClass.GenomeSequence(genome)

        # initialize variables
        depth = 0
        totalPoints = 0
        genomeHistory = [genome]
        pointHistory = [totalPoints]

        while True:

            # go one depth deeper
            depth += 1

            # initialize variables again
            probabilistic = True

            # initialize the genomeObject again
            genomeObject = genomeClass.GenomeSequence(genomeHistory[depth - 1])

            while genome != targetGenome:

                if probabilistic:

                    # get the optionList from Greedy
                    optionList = genomeObject.MutateGreedyPoints(hillclimberBoolean=probabilistic, normalScoreFunction=scoreFunction )

                    # get a random option from optionList
                    randomIndex = random.randint(0, len(optionList) - 1)

                    # mutate the genome
                    genome = genomeObject.Reverse(optionList[randomIndex][0], optionList[randomIndex][1])

                    # update the points (by the length of strip: j - i + 1)
                    totalPoints += optionList[randomIndex][1] - optionList[randomIndex][0] + 1

                    # update the history
                    genomeHistory.append(genome)
                    pointHistory.append(totalPoints)

                    # set hillclimberBoolean to False, so that the next time it will just execute Greedy (i.e. non-probabilistic)
                    probabilistic = False

                else:

                    # make new genomeObject
                    genomeObject = genomeClass.GenomeSequence(genome)

                    # execute Greedy (non-probabilistic)
                    mutatedGenome = genomeObject.MutateGreedyPoints(hillclimberBoolean=probabilistic, normalScoreFunction=scoreFunction )

                    # store the new genome
                    genome = mutatedGenome[0]

                    # update the points and numberOfMutations
                    totalPoints += mutatedGenome[1]

                    # update the history
                    genomeHistory.append(genome)
                    pointHistory.append(totalPoints)

            historyLength = len(genomeHistory)

            totalPoints = pointHistory[len(pointHistory) - 1]

            if totalPoints < upperBound:
                upperBound = totalPoints
                bestGenomeHistory = genomeHistory
                bestPointHistory = pointHistory
                print("New best !!")

            genomeHistory = genomeHistory[:depth + 1]
            pointHistory = pointHistory[:depth + 1]

            genome = genomeHistory[len(genomeHistory) - 1]
            currentPoints = pointHistory[len(pointHistory) - 1]

            if currentPoints >= upperBound:
                break

    print("The best found sequence of mutations looks like: ", bestGenomeHistory)
    print("This sequence of mutations has been solved in: ", bestPointHistory[len(bestPointHistory) - 1], " points!")
