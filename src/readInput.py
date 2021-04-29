import re


def readInput(inputFile):
    # population dimension
    n = int(re.findall(r"[-+]?\d*\.\d+|\d+", inputFile.readline())[0])
    # function's domain
    domain = [int(x) for x in re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", inputFile.readline())]
    # function's coefficients
    coeff = [int(x) for x in re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", inputFile.readline())]
    # precision (the number of decimals used)
    precision = int(re.findall(r"[-+]?\d*\.\d+|\d+", inputFile.readline())[0])
    # probability of crossover
    pc = float(re.findall(r"[-+]?\d*\.\d+|\d+", inputFile.readline())[0])
    # probability of mutation
    pm = float(re.findall(r"[-+]?\d*\.\d+|\d+", inputFile.readline())[0])
    # number of steps of the algorithm
    noOfSteps = int(re.findall(r"[-+]?\d*\.\d+|\d+", inputFile.readline())[0])

    return n, domain, coeff, precision, pc, pm, noOfSteps
