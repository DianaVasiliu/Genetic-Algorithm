import binaryToDecimal as btod


def convertChromosomeToNumber(chrom, a, b, length, precision):
    """
    :param chrom: binary chromosome
    :param a: left end of the interval
    :param b: right end of the interval
    :param length: chromosome length
    :param precision: the working precision
    :return: the converted chromosome

    transformation formula:
    X(2) -> X(10) -> (b-a) / (2^l - 1) * X(10) + a
    """
    convertedChrom = btod.binaryToDecimal(chrom)
    convertedChrom = (b - a) / (2 ** length - 1) * convertedChrom + a
    convertedChrom = float(("{:." + str(precision) + "f}").format(convertedChrom))
    return convertedChrom
