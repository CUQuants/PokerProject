def linearInterpolation(value,  min,  max, minCard = 2.0, maxCard  =14.0):
    return min + (value - minCard) * (max - min) / (maxCard - minCard)