def selectionIntervals(selectionProbabilities):
    # the first value in the selection ranges is the very first probability
    intervals = [0, selectionProbabilities[0]]

    # the sum of the current probability and the last calculated interval end is realized
    # that is, the probability accumulated in step i
    for i in range(1, len(selectionProbabilities)):
        newValue = intervals[-1] + selectionProbabilities[i]
        intervals.append(newValue)

    # round the last value to 1.0 (being a sum of probabilities, it is 1)
    intervals[-1] = round(intervals[-1], 1)

    return intervals
