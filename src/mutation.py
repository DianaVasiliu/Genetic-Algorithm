import random


def mutation(population, probabilityOfMutation, mutationType):
    n = len(population)
    chrLength = len(population[0])
    outputText = "Modified chromosomes:"

    print("Selected chromosomes for mutation: ")

    # mutationType = 1 => rare mutation
        # on each chromosome, at most one position changes "probably"
    # for each chromosome, we generate a random u between 0 and 1
        # if u <pm,
            # we generate a random position in the chromosome
            # we change the respective position in the complement
    if mutationType == 1:
        for i in range(n):
            u = random.random()
            if u < probabilityOfMutation:
                p = random.randint(0, chrLength - 1)
                population[i] = changeGene(population[i], p, i)
                outputText += "\n" + str(i + 1)

    # mutationType = 2
        # on each chromosome, at most all positions change "probably"
    # for each chromosome and for each gene in it,
        # we generate a random number u between 0 and 1
        # if u <pm,
            # we generate a random position in the chromosome
            # we change the respective position in the complement
    elif mutationType == 2:
        for i in range(n):
            for j in range(chrLength):
                u = random.random()
                if u < probabilityOfMutation:
                    population[i] = changeGene(population[i], j, i)
                    outputText += "\n" + str(i + 1)

    else:
        return "Invalid type of mutation"

    return outputText


def changeGene(chromosome, position, chromosomeNumber):
    print("No.", chromosomeNumber + 1)
    print("Modified position: ", position)
    print("Before: ", chromosome[:position], chromosome[position], chromosome[position + 1:])

    if chromosome[position] == '0':
        newGene = '1'
    else:
        newGene = '0'
    chromosome = chromosome[:position] + newGene + chromosome[position + 1:]

    print("After:  ", chromosome[:position], chromosome[position], chromosome[position + 1:])
    print()

    return chromosome
