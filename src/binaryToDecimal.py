def binaryToDecimal(string):
    """
    :param string: binary chromosome string that needs to be converted to number
    :return: the corresponding decimal number
    """
    length = len(string)
    number = 0
    for i in range(length):
        number += int(string[i]) * 2 ** (length - i - 1)
    return number
