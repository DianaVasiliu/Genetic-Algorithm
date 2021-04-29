import random


def makeSelection(selectionIntervals, functionValues, isElitist):
    selectedChromosomes = []
    outputText = ""
    newPopulation = []
    n = len(functionValues)

    # The elitist criterion:
    # chromosomes with the highest fitness function are automatically passed on to the next generation
    # we pass only one elitist chromosome further
    if isElitist:
        maxValue = max(functionValues)
        for i in range(n):
            if functionValues[i] == maxValue:
                newPopulation.append(i + 1)
                break

    # Roulette criteria:
    # we generate a number u between 0 and 1 and we find the selection interval [i, i + 1] in which u is
    # we choose the (i + 1)'th chromosome
    for i in range(n - len(newPopulation)):
        u = random.random()
        chrNumber = binarySearch(selectionIntervals, u)
        selectedChromosomes.append(chrNumber)
        outputText += "u = {:f}   selecting chromosome {}\n".format(u, chrNumber)

    return selectedChromosomes, newPopulation, outputText


def binarySearch(arr, element):
    low = 0
    high = len(arr) - 1
    mid = (high + low) // 2

    while low <= high:
        mid = (high + low) // 2

        if arr[mid - 1] <= element <= arr[mid]:
            return mid
        elif arr[mid] < element:
            low = mid + 1
        elif arr[mid] > element:
            high = mid - 1

    return mid
