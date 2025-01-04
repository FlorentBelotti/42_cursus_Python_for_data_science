def give_bmi(height: list[int | float], weight: list[int | float]):

    """
    Calculate the BMI for each pair of height and weight.

    :param height: List of heights in meters.
    :param weight: List of weights in kilograms.
    :return: List of BMI values.
    """

    bmi = []
    for h, w in zip(height, weight):
        bmi.append(w / (h ** 2))
    return bmi


def apply_limit(bmi: list[int | float], limit: int):

    """
    Apply a limit to the BMI values.

    :param bmi: List of BMI values.
    :param limit: The BMI limit.
    :return: List of booleans indicating if the BMI is above the limit.
    """
    return [b > limit for b in bmi]
