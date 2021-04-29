import random
import convertChromosomeToNumber as conv


def generateInitialPopulation(nrOfChromosomes, lengthOfChromosome, domain, precision, f):
    population = []
    functionValues = []
    xValues = []

    for i in range(nrOfChromosomes):
        # we randomly generate binary values and convert them to a string
        chromozome = "".join([str(random.randint(0, 1)) for _ in range(lengthOfChromosome)])
        population.append(chromozome)
        # we calculate the values x and f(x) for the generated chromosome
        x = conv.convertChromosomeToNumber(chromozome, domain[0], domain[1], lengthOfChromosome, precision)
        fx = f(x)
        xValues.append(x)
        functionValues.append(fx)

    return population, xValues, functionValues
