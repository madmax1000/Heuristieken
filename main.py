import helpers as helpers

def main():

    # let user choose the genome
    genome = []
    genomeInput = input("Which genome do you wish to sort? Type \"1\" for the D. Melanogaster genome, or type \"2\" for a random generated genome. Press Enter afterwards.\n")

    if genomeInput == '1':
        genome = [0, 23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9, 26]
        print("You've chosen the D. Melanogaster genome: ", genome, "\n")
    elif genomeInput == '2':
        lengthInput = int(input("How many genes should your genome contain?\n"))
        genome = helpers.RandomMutation(lengthInput)
        print("This is your random generated genome: ", genome, "\n")
    else:
        print("Run the program again and follow the instructions this time!\n")
        exit()

    # specify the target genome (in other words: a sorted array of numbers)
    targetGenome = [i for i in range(len(genome))]

    # let user choose the algorithm
    method = ""
    methodInput = input("Which mutating algorithm do you want to use? Type \"1\" for Bubble Sort, type \"2\" for Greedy, or type \"3\" for Branch and Bound. Press Enter afterwards. \n")

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

    confirmation = ""
    confirmation = input("Press Enter to start mutating.\n")

    # check if user confirmed with pressing Enter
    if confirmation == "":
        if method == "Bubble":
            print("START CONFIRMED\n")

            print("BUBBLE ALGORITHM STARTS\n")
            numberOfMutations = helpers.bubblesort(genome)

            print("Your genome has been solved in ", numberOfMutations, " mutations!")

        if method == "Greedy":
            print("START CONFIRMED\n")

            print("GREEDY ALGORITHM STARTS\n")

            numberOfMutations = 0

            # Execute Greedy until the genomes are equal
            while genome != targetGenome:
                numberOfMutations += 1
                genomeObject = helpers.GenomeSequence(genome)
                genome = genomeObject.Mutate("Greedy")
                print("Mutation number: ", numberOfMutations, " ", genome)

            print("Your genome has been solved in ", numberOfMutations, " mutations!")

        if method == "BnB":

            secondConfirmation = ""
            secondConfirmation = input("WARNING: The Branch and Bound algorithm can have a very long run-time for long genomes. Press Enter to continue.")
            if secondConfirmation == "":
                print("START CONFIRMED\n")

                print("BRANCH AND BOUND ALGORITHM STARTS\n")

                current = [0] * 32
                best = []

                genomeObject = helpers.GenomeSequence(genome)
                breakpointPairs = genomeObject.breakpointPairs

                upperBound, current, best = helpers.BnB(genomeObject, 0, 30, current, best, breakpointPairs, targetGenome)
                best = best[:upperBound]

                print("\nThe Branch and Bound algorithm has finished. The shortest solution possibile equals ", len(best))
                print("This sequence of mutations (i,j) looks like: ", best)
                print("Executing this very sequence of mutations on the original genome results in the following intermediate genomes: ")

                numberOfMutations = 0
                for mutation in best:
                    numberOfMutations += 1
                    genomeObject.genome = genomeObject.Reverse(mutation[0], mutation[1])
                    print("Mutation number: ", numberOfMutations, " ", genomeObject.genome)

                print("Your genome has been solved in ", numberOfMutations, " mutations!")

            else:
                print("Run the program again and follow the instructions this time!\n")

    else:
        print("Run the program again and follow the instructions this time!\n")

if __name__ == "__main__":
    main()