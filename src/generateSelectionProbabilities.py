def generateSelectionProbabilities(functionValues):
    probabilities = []
    sumfx = sum(functionValues)     # total population performance

    for fx in functionValues:
        p = fx / sumfx              # the probability of selecting the i'th chromosome
        probabilities.append(p)

    return probabilities
