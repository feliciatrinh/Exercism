def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    factors = {1} if number > 1 else {}
    for factor in range(2, int(number ** 0.5) + 1):
        if number % factor == 0:
            factors.add(factor)
            factors.add(number // factor)

    aliquot_sum = sum(factors)
    if number == aliquot_sum:
        classification = "perfect"
    elif number < aliquot_sum:
        classification = "abundant"
    else:
        classification = "deficient"

    return classification
