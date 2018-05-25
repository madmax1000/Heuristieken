import helpers
import time
import GenomeSequence as genomeClass
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# (lees over dit heen: randomGreedyPoints = hillclimber)
def main():

    # let user choose what he/she wants to do
    action = input("\nWhat do you want to do? \nType \"1\" to mutate genomes \nType \"2\" to generate plots. Press Enter afterwards.\n")

    if action == '1':

        # let user choose between mutation steps or mutation points
        stepsOrPoints = input("\nDo you wish to search for an optimal solution in terms of mutation 'STEPS' or in terms of mutation 'POINTS'? \nType 1 for mutation steps \nType 2 for mutation points. Press Enter afterwards.\n")

        # let user choose the genome
        genome = []
        genomeInput = input ("\nWhich genome do you wish to sort? \nType \"1\" for the D. Melanogaster genome \nType \"2\" for a random generated genome. Press Enter afterwards.\n" )

        if genomeInput == '1':
            genome = [0, 23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]
            print ( "You've chosen the D. Melanogaster genome: ", genome, "\n" )
        elif genomeInput == '2':
            lengthInput = int ( input ( "\nHow many genes should your genome contain?\n" ) )
            genome = helpers.RandomMutation ( lengthInput )
            print ( "This is your random generated genome: ", genome, "\n" )
        else:
            print ( "Run the program again and follow the instructions this time!\n" )
            exit ()

        # specify the target genome (in other words: a sorted array of numbers)
        targetGenome = [i for i in range ( len ( genome ) )]

        if stepsOrPoints == '1':

            # let user choose the algorithm
            method = ""
            methodInput = input("Which mutating algorithm do you want to use? \nType \"1\" for Bubble Sort \nType \"2\" for Greedy \nType \"3\" for Branch and Bound \nType \"4\" for Random-Greedy-Branch and Bound.\nPress Enter afterwards. \n")

            if methodInput == '1':
                method = "Bubble"
                print("You've chosen to use Bubble Sort.\n")
            elif methodInput == '2':
                method = "Greedy"
                print("You've chosen to use Greedy.\n")
            elif methodInput == '3':
                method = "BnB"
                print("You've chosen to use Branch and Bound.\n")
            elif methodInput == '4':
                method = "Hillclimber"
                print ( "You've chosen to use Random-Greedy-Branch and Bound.\n" )
                numberOfSteps = input ( "Type a positive number of steps. Press enter afterwards.\n" )

            else:
                print("Run the program again and follow the instructions this time!\n")

            confirmation = input("Press Enter to start mutating.\n")

            # check if user confirmed with pressing Enter
            if confirmation == "":
                if method == "Bubble":
                    print("START CONFIRMED\n")

                    print("BUBBLE ALGORITHM STARTS\n")
                    numberOfMutations = helpers.Bubblesort(genome)

                    print("Your genome has been solved in ", numberOfMutations, " mutations!")

                if method == "Greedy":
                    print("START CONFIRMED\n")

                    print("GREEDY ALGORITHM STARTS\n")

                    # store Greedy's history in the form (i, j, deltaPHI)
                    history = []

                    # keep track of the number of mutations
                    numberOfMutations = 0
                    prevI = -1
                    prevJ = -1

                    # Execute Greedy until the genomes are equal
                    while genome != targetGenome:
                        numberOfMutations += 1
                        genomeObject = genomeClass.GenomeSequence(genome)
                        genome, i, j, deltaPHI = genomeObject.MutateGreedy(prevI, prevJ)
                        prevI, prevJ = i, j
                        history.append([i, j, deltaPHI])
                        print("Mutation number: ", numberOfMutations, " ", genome)
                    print("Your genome has been solved in ", numberOfMutations, " mutations!")

                if method == "BnB":

                    secondConfirmation = input("WARNING: The Branch and Bound algorithm can have a very long run-time for long genomes. Press Enter to continue.")
                    if secondConfirmation == "":
                        print("START CONFIRMED\n")

                        print("BRANCH AND BOUND ALGORITHM STARTS\n")

                        # initialize empty arrays
                        current = [0] * 32
                        best = []

                        # initialize genomeObject with its breakpointPairs
                        genomeObject = genomeClass.GenomeSequence(genome)
                        breakpointPairs = genomeObject.breakpointPairs

                        # start Branch and Bound!
                        upperBound, current, best = helpers.BnB(genomeObject, 0, 30, current, best, breakpointPairs, targetGenome)

                        # store the shortest sequence of mutations
                        best = best[:upperBound]

                        print("\nThe Branch and Bound algorithm has finished. The shortest solution possibile equals ", len(best))
                        print("Your original genome equals: ", genome)
                        print("The shortest sequence of mutations (i,j) equals: ", best)
                        print("Executing this very sequence of mutations on the original genome results in the following intermediate genomes: ")

                        numberOfMutations = 0
                        for mutation in best:
                            numberOfMutations += 1
                            genomeObject.genome = genomeObject.Reverse(mutation[0], mutation[1])
                            print("Mutation number: ", numberOfMutations, " ", genomeObject.genome)

                        print("Your genome has been solved in ", numberOfMutations, " mutations!")

                    else:
                        print("Run the program again and follow the instructions this time!\n")

                if method == "Hillclimber":
                    helpers.Hillclimber ( genome, numberOfSteps )

            else:
                print("Run the program again and follow the instructions this time!\n")

        elif stepsOrPoints == '2':
            # let user choose the algorithm
            method = ""
            methodInput = input ("Which mutating algorithm do you want to use? \nType \"1\" for Greedy \nType \"2\" for Random-Greedy. Press Enter afterwards. \n" )

            scoreFunction = input ("Which score function do you wish to use? \nType \"1\" for 'n' \nType \"2\" for 0.5*n^2. Press Enter afterwards.\n" )

            if scoreFunction == '1':
                scoreFunction = True
            elif scoreFunction == '2':
                scoreFunction = False
            else:
                print ("Run the program again and follow the instructions this time!\n" )

            if methodInput == '1':
                method = "Greedy"
                print("You've chosen to use Greedy.\n")

            elif methodInput == '2':
                method = "Hillclimber"
                print("You've chosen to use Random-Greedy.\n")
                iterations = int(input("How many iterations do you wish the algorithm to execute? (500 is fine for testing)\n"))

            else:
                print("Run the program again and follow the instructions this time!\n")

            confirmation = input("Press Enter to start mutating.\n")
            if confirmation == "":
                if method == "Greedy":

                    print("Your original genome looks like: ", genome)
                    totalPoints = 0

                    # start Greedy
                    while genome != targetGenome:
                        genomeObject = genomeClass.GenomeSequence(genome)
                        genome, currentLengthPoints = genomeObject.MutateGreedyPoints(hillclimberBoolean=False, normalScoreFunction=scoreFunction)
                        totalPoints += currentLengthPoints
                        print("Mutated genome: ", genome, "(this mutation cost ", currentLengthPoints, " points)")
                    print("Your genome has been solved with a total of ", totalPoints, "points.")

                elif method == "Hillclimber":
                    helpers.HillclimberPoints(genome, iterations, scoreFunction)


                else:
                    print("Run the program again and follow the instructions this time!\n" )

            else:
                print("Run the program again and follow the instructions this time!\n")

        else:
            print("Run the program again and follow the instructions this time!\n")


    elif action == '2':

        methodInput = ""
        methodInput = input("For which mutating algorithm do you wish to generate plots? Type \"1\" for Bubble Sort, type \"2\" for Greedy, or type \"3\" for Branch and Bound. Press Enter afterwards. \n")

        if methodInput == '1':
            method = "Bubble"
            print("You've chosen to use Bubble Sort.\n")
        elif methodInput == '2':
            method = "Greedy"
            print("You've chosen to use Greedy.\n")
        elif methodInput == '3':
            method = "BnB"
            print("You've chosen to use Branch and Bound.\n")
        else:
            print("Run the program again and follow the instructions this time!\n")

        plotType = input("What kind of plot do you want to generate? Type \"1\" for Run-time visualizations, or type \"2\" for Mutation steps visualizations. Press Enter afterwards. \n")

        confirmation = input("Press Enter to start generating plots.\n")
        # initialize empty arrays
        # check if user confirmed with pressing Enter
        if confirmation == "":
            t = []
            length = []
            breakpoints = []
            steps = []

            if method == "Bubble":

                maxLength = 40
                maxBreadth = 40

                # fill length
                for i in range(1, maxLength ):
                    for j in range(1, maxBreadth ):
                        length.append(i)

                if plotType == '1':

                    # RUN-TIME
                    for genomeLength in range(1,maxLength):
                        for i in range(1,maxBreadth):
                            genome = helpers.RandomMutation(20)
                            genomeObject = genomeClass.GenomeSequence(genome)

                            # save the number of breakpoints in the original genome
                            breakpoints.append(genomeObject.breakpointPairs)

                            t0 = time.time()
                            helpers.Bubblesort(genome)
                            t.append(time.time() - t0)

                    # plot the figure
                    fig = plt.figure()
                    ax = fig.add_subplot(111, projection='3d')
                    ax.scatter(length, breakpoints, t)
                    ax.set_xlabel("Genome Length")
                    ax.set_ylabel("# Breakpoints")
                    ax.set_zlabel("Run-time")
                    plt.show()

                if plotType == '2':

                    #MUTATION STEPS
                    for genomeLength in range(1, maxLength):
                        for i in range(1, maxBreadth):
                            genome = helpers.RandomMutation(genomeLength)
                            genomeObject = genomeClass.GenomeSequence(genome)

                            # save the number of breakpoints in the original genome
                            breakpoints.append(genomeObject.breakpointPairs)

                            currentSteps = helpers.Bubblesort(genome)
                            steps.append(currentSteps)

                    # plot the figure
                    fig = plt.figure()
                    ax = fig.add_subplot(111, projection='3d')
                    ax.scatter(length, breakpoints, steps)
                    ax.set_xlabel("Genome Length")
                    ax.set_ylabel("# Breakpoints")
                    ax.set_zlabel("Mutation Steps")
                    plt.show()

                else:
                    print("Run the program again and follow the instructions this time!\n" )

            if method == "Greedy":
                t = []
                length = []
                breakpoints = []
                steps = []

                maxLength = 40
                maxBreadth = 40

                # fill length
                for i in range(1, maxLength ):
                    for j in range(1, maxBreadth ):
                        length.append(i)

                if plotType == '1':

                    # RUN-TIME
                    for genomeLength in range(1, maxLength):
                        for i in range(1, maxBreadth):
                            genome = helpers.RandomMutation(genomeLength)
                            targetGenome = [i for i in range(len(genome))]

                            genomeObject = genomeClass.GenomeSequence(genome)
                            # save the number of breakpoints in the original genome
                            breakpoints.append(genomeObject.breakpointPairs )

                            # Execute Greedy until the genomes are equal
                            prevI = -1
                            prevJ = -1

                            t0 = time.time()
                            while genome != targetGenome:
                                genomeObject = genomeClass.GenomeSequence(genome)
                                genome, i, j, deltaPHI = genomeObject.MutateGreedy(prevI, prevJ)
                                prevI, prevJ = i, j
                            t.append(time.time() - t0)

                    # plot the figure
                    fig = plt.figure()
                    ax = fig.add_subplot(111, projection='3d')
                    ax.scatter(length, breakpoints, t)
                    ax.set_xlabel("Genome Length")
                    ax.set_ylabel("# Breakpoints")
                    ax.set_zlabel("Run-time")
                    plt.show()

                if plotType == '2':

                    # MUTATION STEPS
                    for genomeLength in range(1, maxLength):
                        for i in range(1, maxBreadth):
                            genome = helpers.RandomMutation(genomeLength)
                            targetGenome = [i for i in range(len(genome))]

                            genomeObject = genomeClass.GenomeSequence(genome)

                            # save the number of breakpoints in the original genome
                            breakpoints.append(genomeObject.breakpointPairs )

                            # Execute Greedy until the genomes are equal
                            prevI = -1
                            prevJ = -1
                            numberOfMutations = 0
                            while genome != targetGenome:
                                genomeObject = genomeClass.GenomeSequence(genome)
                                genome, i, j, deltaPHI = genomeObject.MutateGreedy(prevI, prevJ)
                                prevI, prevJ = i, j
                                numberOfMutations += 1
                            steps.append(numberOfMutations)

                    # plot the figure
                    fig = plt.figure()
                    ax = fig.add_subplot(111, projection='3d')
                    ax.scatter(length, breakpoints, steps)
                    ax.set_xlabel("Genome Length")
                    ax.set_ylabel("# Breakpoints")
                    ax.set_zlabel("Mutation Steps")
                    plt.show()

            if method == "BnB":

                t = []
                length = []
                breakpoints = []
                steps = []

                maxLength = 13
                maxBreadth = 20

                # fill length
                for i in range(1, maxLength ):
                    for j in range(1, maxBreadth ):
                        length.append(i)

                if plotType == '1':

                    # RUN-TIME
                    for genomeLength in range(1, maxLength):
                        for i in range(1, maxBreadth):
                            # initialize empty arrays
                            current = [0] * 32
                            best = []

                            genome = helpers.RandomMutation(genomeLength)
                            targetGenome = [i for i in range(len(genome))]

                            # initialize genomeObject with its breakpointPairs
                            genomeObject = genomeClass.GenomeSequence(genome)
                            breakpointPairs = genomeObject.breakpointPairs

                            breakpoints.append(genomeObject.breakpointPairs )

                            t0 = time.time()
                            # start Branch and Bound!
                            upperBound, current, best = helpers.BnB(genomeObject, 0, 30, current, best,
                                                                      breakpointPairs, targetGenome)
                            t.append(time.time() - t0)

                    # plot the figure
                    fig = plt.figure()
                    ax = fig.add_subplot(111, projection='3d')
                    ax.scatter(length, breakpoints, t)
                    ax.set_xlabel ( "Genome Length")
                    ax.set_ylabel ( "# Breakpoints" )
                    ax.set_zlabel ( "Run-time" )
                    plt.show ()

                if plotType == '2':

                    # MUTATION STEPS
                    for genomeLength in range ( 1, maxLength ):
                        for i in range ( 1, maxBreadth ):
                            # initialize empty arrays
                            current = [0] * 32
                            best = []

                            genome = helpers.RandomMutation ( genomeLength )
                            targetGenome = [i for i in range ( len ( genome ) )]

                            # initialize genomeObject with its breakpointPairs
                            genomeObject = genomeClass.GenomeSequence ( genome )
                            breakpointPairs = genomeObject.breakpointPairs

                            breakpoints.append ( genomeObject.breakpointPairs )

                            # start Branch and Bound!
                            upperBound, current, best = helpers.BnB ( genomeObject, 0, 30, current, best,
                                                                      breakpointPairs, targetGenome )
                            # store the shortest sequence of mutations
                            best = best[:upperBound]
                            steps.append(len(best))

                    # plot the figure
                    fig = plt.figure ()
                    ax = fig.add_subplot ( 111, projection='3d' )
                    ax.scatter ( length, breakpoints, steps )
                    ax.set_xlabel ( "Genome Length" )
                    ax.set_ylabel ( "# Breakpoints" )
                    ax.set_zlabel ( "Mutation Steps" )
                    plt.show ()

        else:
            print("Run the program again and follow the instructions this time!\n")

    else:
        print("Run the program again and follow the instructions this time!\n")


if __name__ == "__main__":
    main()
