import random


def makeSelectionForCrossover(population, probabilityOfCrossingOver):
    """
        for each chromosome, we generate a random number u between 0 and 1
        if u < pc,
            then the chromosome participates at the crossover
    """

    outputText = ""
    selectedChromForCO = []

    for i in range(len(population)):
        u = random.random()
        outputText += "{:5d}: {}   u = {}".format(i + 1, population[i], u)
        if u < probabilityOfCrossingOver:
            outputText += " < " + str(probabilityOfCrossingOver) + " participates\n"
            selectedChromForCO.append(i + 1)
        else:
            outputText += "\n"

    print("Selected chromosomes for crossover: ", selectedChromForCO)

    return selectedChromForCO, outputText


def crossover(selectedChromosomes, selectedChromosomesStrings):
    """
        to choose the random pairs, we randomly change the order of the values in the selectedChromosomes

        form disjoint pairs with selected chromosomes:
             if there is an even number, then pairs are formed (i, i + 1)
             if there is an odd number > 2, then we group the last 3 (n-3, n-2, n-1)

        depending on the case (n even / odd), we call crossingover on the respective number of chromosomes
    """
    random.shuffle(selectedChromosomes)
    n = len(selectedChromosomes)
    outputText = ""

    for i in range(0, n - 1, 2):
        chromosome1 = selectedChromosomes[i]        # selected chromosome's index
        chromosome2 = selectedChromosomes[i + 1]    # selected chromosome's index

        if n >= 3 and n % 2 != 0 and i == n - 3:
            chromosome3 = selectedChromosomes[i + 2]    # selected chromosome's index
            chrom1, chrom2, chrom3, output = \
                crossover3Chromosomes(chromosome1, chromosome2, chromosome3, selectedChromosomesStrings)
            selectedChromosomesStrings[chromosome3 - 1] = chrom3
        else:
            chrom1, chrom2, output = crossover2Chromosomes(chromosome1, chromosome2, selectedChromosomesStrings)

        selectedChromosomesStrings[chromosome1 - 1] = chrom1
        selectedChromosomesStrings[chromosome2 - 1] = chrom2
        outputText += output

    return outputText


def crossover2Chromosomes(chromNo1, chromNo2, selectedChromosomes):
    outputText = "Crossing over chromosome " + str(chromNo1) \
                 + " and chromosome " + str(chromNo2) + ":\n"

    chromosome1 = selectedChromosomes[chromNo1 - 1]
    chromosome2 = selectedChromosomes[chromNo2 - 1]

    # we generate a random cut point
    point = random.randint(0, len(chromosome1) - 1)

    outputText += "\t" + chromosome1 + "   " + chromosome2 + "  cut point  " + str(point) + "\n"
    outputText += "\tResulted chromosomes     "

    # we break and cross the chromosomes according to the point generated
    rez1 = chromosome1[:point] + chromosome2[point:]
    rez2 = chromosome2[:point] + chromosome1[point:]

    outputText += rez1 + "   " + rez2 + "\n"

    return rez1, rez2, outputText


def crossover3Chromosomes(chromNo1, chromNo2, chromNo3, selectedChromosomes):
    outputText = "Crossing over chromosome " + str(chromNo1) \
                 + " and chromosome " + str(chromNo2) + " and chromosome " + str(chromNo3) + ":\n"

    chromosome1 = selectedChromosomes[chromNo1 - 1]
    chromosome2 = selectedChromosomes[chromNo2 - 1]
    chromosome3 = selectedChromosomes[chromNo3 - 1]

    # we generate a random cut point
    point = random.randint(0, len(chromosome1) - 1)

    outputText += "\t" + chromosome1 + "   " + chromosome2 + "   " + chromosome3 + "  cut point  " + str(point) + "\n"
    outputText += "\tResulted chromosomes     "

    # we break and cross the chromosomes according to the point generated
    # a circular cross is made
    rez1 = chromosome1[:point] + chromosome2[point:]
    rez2 = chromosome2[:point] + chromosome3[point:]
    rez3 = chromosome3[:point] + chromosome1[point:]

    outputText += rez1 + "   " + rez2 + "   " + rez3

    return rez1, rez2, rez3, outputText
