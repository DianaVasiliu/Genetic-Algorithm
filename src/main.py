import math
import copy
import readInput as read
import generateInitialPopulation as genPop
import generateSelectionProbabilities as genSelProb
import selectionIntervals as si
import makeSelection as mkSel
import crossover
import mutation
import convertChromosomeToNumber as convert

inputFile = open("../input.txt", "r")
outputFile = open("../Evolution.txt", "w")

"""
    for generating a generation P(t + 1) from P(t):
         1) generate selection probabilities - generateSelectionProbabilities()
         2) we generate selection probability intervals - selectionIntervals()
         3) generate n values for u and select those in chromosomes that pass to the next generation - makeSelection()
         4) generate n values for u and select the chromosomes that will participate in the crossover()
         5) select the chromosomes that participate in the mutation and go through the process - mutation()
"""


def makeNewPopulation(chromosomes, values, fvalues, idx):
    """
    :param chromosomes: list of chromosomes from which to calculate the new values x and f(x)
    :param values: the resulting array of x values
    :param fvalues: f(x) values array
    :param idx: the index in the chromosomes for which x and f(x) must be calculated
    :return: string formatted for writing to file
    """
    out = ""
    chrom = chromosomes[idx]
    val = convert.convertChromosomeToNumber(chrom, domain[0], domain[1], l, precision)
    fval = f(val)
    values.append(val)
    fvalues.append(fval)
    out += ("{:5d}: {}   x = {: ." + str(precision) + "f}   f = {}\n")\
        .format(idx + 1, chrom, val, fval)

    return out


def f(x):
    res = 0
    coeffNr = len(coeff)
    for i in range(coeffNr):
        res += coeff[i] * x ** (coeffNr - i - 1)
    return res


if __name__ == "__main__":
    n, domain, coeff, precision, pc, pm, noOfSteps = read.readInput(inputFile)

    # #######################################################################

    # we perform the discretization of the interval (we divide [a, b] in (b-a)*10^p subintervals)
    # calculate the length of the chromosome according to the formula: 2^(l-1) < (b-a)*10^p <= 2^l
    noOfSubintervals = (domain[1] - domain[0]) * pow(10, precision)
    l = math.ceil(math.log2(noOfSubintervals))

    # choosing elitist criterion
    isElitist = input("Do you take into account the elitist criterion? (Y/N)")
    while isElitist not in ['Y', 'y', 'N', 'n']:
        print("Wrong choice, try again (Y/N)", end=" ")
        isElitist = input()

    if isElitist in ['Y', 'y']:
        isElitist = True
    else:
        isElitist = False

    # choosing mutation type
    # mutationType = 1 => rare mutation
        # on each chromosome, at most one position changes "probably"
    # mutationType = 2 =>
        # on each chromosome, at most all positions change "probably"
    print("1. Type 1 of mutation (rare mutation): at most ONE position changes \"probably\"")
    print("2. Type 2 of mutation: at most ALL positions change \"probably\"")

    mutationType = input("Choose the type of mutation to use (1/2)")
    while mutationType not in ['1', '2']:
        print("Wrong choice, try again (1/2)", end=' ')
        mutationType = input()
    mutationType = int(mutationType)

    print("---------------- STEP 1 ----------------")

    # ###########################################
    # ###### generarea populatiei initiale ######
    # ###########################################
    outputFile.write("Initial population\n")
    population, xValues, functionValues = genPop.generateInitialPopulation(n, l, domain, precision, f)

    # creating output for file
    output = ""
    for i in range(n):
        output += ("{:5d}: {}   x = {: ." + str(precision) + "f}   f = {}\n")\
            .format(i + 1, population[i], xValues[i], functionValues[i])
    outputFile.write(output + "\n")

    # ####################################################
    # ######## generating selection probabilities ########
    # ####################################################
    outputFile.write("Selection probabilities\n")
    selectionProbabilities = genSelProb.generateSelectionProbabilities(functionValues)

    # creating output for file
    output = ""
    i = 0
    for fx in functionValues:
        output += "chromosome {:5d}     probability {}\n".format(i + 1, selectionProbabilities[i])
        i += 1
    outputFile.write(output + "\n")

    # #################################################
    # ######## selection probability intervals ########
    # #################################################
    outputFile.write("Selection probability intervals\n")
    selectionIntervals = si.selectionIntervals(selectionProbabilities)

    # creating output for file
    output = ""
    i = 0
    for value in selectionIntervals:
        output += str(str(value) + " ")
        if i % 6 == 0 and i != 0:
            output += "\n"
        i += 1
    outputFile.write(output + "\n")

    # ##########################################################
    # ###### chromosome selection for the next generation ######
    # ##########################################################
    selectedChromosomes, nextGenChromosomes, output = \
        mkSel.makeSelection(selectionIntervals, functionValues, isElitist)

    # selectedChromosomes = chromosomes that will "probably" go through the crossover / mutation process
    # nextGenChromosomes = chromosomes that have passed through the elitist criterion in the next generation

    outputFile.write(output)

    # ##################################
    # ###### selected chromosomes ######
    # ##################################
    outputFile.write("After selection:\n")
    output = ""
    selectedChromosomesStrings = []

    # creating output for file +
    # create a list of selected chromosomes from the list of selected chromosome numbers
    for i in range(len(selectedChromosomes)):
        output += ("{:5d}: {}   x = {: ." + str(precision) + "f}   f = {}\n") \
            .format(i + 1,
                    population[selectedChromosomes[i] - 1],
                    xValues[selectedChromosomes[i] - 1],
                    functionValues[selectedChromosomes[i] - 1])
        selectedChromosomesStrings.append(population[selectedChromosomes[i] - 1])

    for i in range(len(nextGenChromosomes)):
        output += ("{:5d}: {}   x = {: ." + str(precision) + "f}   f = {}        ELITIST\n") \
            .format(len(selectedChromosomes) + i + 1,
                    population[nextGenChromosomes[i] - 1],
                    xValues[nextGenChromosomes[i] - 1],
                    functionValues[nextGenChromosomes[i] - 1])

    outputFile.write(output + "\n")

    # ####################################################
    # ###### selection of chromosomes for crossover ######
    # ####################################################
    outputFile.write("Probability of crossingover " + str(pc) + "\n")
    selectedChromForCO, output = crossover.makeSelectionForCrossover(selectedChromosomesStrings, pc)

    # creating output for file +
    for i in range(len(nextGenChromosomes)):
        output += "{:5d}: {}   ELITIST\n"\
            .format(len(selectedChromosomes) + i + 1, population[nextGenChromosomes[i] - 1])

    outputFile.write(output + "\n")

    # #######################################
    # ############ crossing over ############
    # #######################################
    output = crossover.crossover(selectedChromForCO, selectedChromosomesStrings)
    outputFile.write(output + "\n")

    # #####################################
    # ######## crossed chromosomes ########
    # #####################################
    outputFile.write("After crossing over: \n")
    output = ""
    index = 0
    xValues = []
    functionValues = []

    # recalculate the values for x and f(x) for the new chromosomes resulting from the crossover
    for i in range(len(selectedChromosomesStrings)):
        output += makeNewPopulation(selectedChromosomesStrings, xValues, functionValues, index)
        index += 1

    # recalculate the values for x and f(x) for the elitist chromosomes
    for i in range(len(nextGenChromosomes)):
        chromosome = population[nextGenChromosomes[i] - 1]
        x = convert.convertChromosomeToNumber(chromosome, domain[0], domain[1], l, precision)
        fx = f(x)
        xValues.append(x)
        functionValues.append(fx)
        output += ("{:5d}: {}   x = {: ." + str(precision) + "f}   f = {}        ELITIST\n") \
            .format(index + 1, chromosome, x, fx)
        index += 1

    outputFile.write(output + "\n")

    # ######################
    # ###### mutation ######
    # ######################
    outputFile.write("Probability of mutation for each gene " + str(pm) + "\n")

    output = mutation.mutation(selectedChromosomesStrings, pm, mutationType)
    outputFile.write(output + "\n\n")

    # ########################################
    # ###### chromosomes after mutation ######
    # ########################################
    outputFile.write("After mutation: \n")
    output = ""
    xValues = []
    functionValues = []
    index = 0

    # after the mutation, the next generation results
    # so in selectedChromosomesStrings we can add elitist chromosomes
    for i in range(len(nextGenChromosomes)):
        chromosome = population[nextGenChromosomes[i] - 1]
        selectedChromosomesStrings.append(chromosome)

    # recalculate the values for x and f(x) for the new chromosomes resulting from the mutation
    for i in range(len(selectedChromosomesStrings)):
        output += makeNewPopulation(selectedChromosomesStrings, xValues, functionValues, index)
        index += 1

    outputFile.write(output + "\n")

    # #####################################
    # ###### Maximum value evolution ######
    # #####################################
    outputFile.write("Maximum value evolution: \n")
    maxValue = max(functionValues)
    idx = functionValues.index(maxValue)
    x = xValues[idx]
    outputFile.write("maximum = " + str(maxValue) + "  x = " + str(x) + "\n")
    print()

    for step in range(2, noOfSteps + 1):
        print("---------------- STEP " + str(step) + " ----------------")

        # the current population on which we perform the operations becomes
        # the generation resulting from the previous step
        population = copy.deepcopy(selectedChromosomesStrings)

        # # recalculate selection probabilities and selection intervals for new f(x)
        selectionProbabilities = genSelProb.generateSelectionProbabilities(functionValues)
        selectionIntervals = si.selectionIntervals(selectionProbabilities)

        # we select again the chromosomes that enter the crossover / mutation processes, respectively the elitist ones
        selectedChromosomes, nextGenChromosomes, _ = \
            mkSel.makeSelection(selectionIntervals, functionValues, isElitist)

        # we build the list of chromosomes according to the number of the selected chromosome
        selectedChromosomesStrings = []
        for i in range(len(selectedChromosomes)):
            selectedChromosomesStrings.append(population[selectedChromosomes[i] - 1])

        # we make the selection for crossover + the crossover process
        selectedChromForCO, _ = crossover.makeSelectionForCrossover(selectedChromosomesStrings, pc)
        crossover.crossover(selectedChromForCO, selectedChromosomesStrings)

        # we perform the mutation process
        mutation.mutation(selectedChromosomesStrings, pm, mutationType)

        xValues = []
        functionValues = []
        index = 0
        # we add the elitist chromosomes to the selected and modified chromosomes for the next generation
        for i in range(len(nextGenChromosomes)):
            chromosome = population[nextGenChromosomes[i] - 1]
            selectedChromosomesStrings.append(chromosome)

        # recalculate the values for x and for f(x) for the resulting chromosomes
        for i in range(len(selectedChromosomesStrings)):
            output += makeNewPopulation(selectedChromosomesStrings, xValues, functionValues, index)
            index += 1

        # maximum function + average value of performance
        maxValue = max(functionValues)
        idx = functionValues.index(maxValue)
        x = xValues[idx]
        avgPerformance = sum(functionValues) / n
        outputFile.write("maximum = " + str(maxValue) + "  x = " + str(x) + "    " + str(avgPerformance) + "\n")
        print()
