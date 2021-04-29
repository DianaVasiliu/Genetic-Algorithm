import re


def readInput(inputFile):
    # population dimension
    n = float(re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", inputFile.readline())[0])
    # function's domain
    domain = [float(x) for x in re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", inputFile.readline())]
    # function's coefficients
    coeff = [float(x) for x in re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", inputFile.readline())]
    # precision (the number of decimals used)
    precision = float(re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", inputFile.readline())[0])
    # probability of crossover
    pc = float(re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", inputFile.readline())[0])
    # probability of mutation
    pm = float(re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", inputFile.readline())[0])
    # number of steps of the algorithm
    noOfSteps = float(re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", inputFile.readline())[0])

    validData = checkInputData(n, domain, precision, pc, pm, noOfSteps)
    if not validData:
        print("Invalid input data")
        exit(0)

    n = int(n)
    precision = int(precision)
    noOfSteps = int(noOfSteps)
    return n, domain, coeff, precision, pc, pm, noOfSteps


def checkInputData(n, domain, precision, pc, pm, noOfSteps):
    if n <= 0 or not n.is_integer():
        return False
    if domain[0] > domain[1]:
        return False
    if precision <= 0 or not precision.is_integer():
        return False
    if pc < 0 or pc > 1:
        return False
    if pm < 0 or pm > 1:
        return False
    if noOfSteps <= 0 or not noOfSteps.is_integer():
        return False

    return True
