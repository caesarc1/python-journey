EXPECTED_BAKE_TIME = 40
preparation_time = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - number of layers added to the lasagna.
    :return: int - number of minutes you would spend making them

    Function that takes the number of layers added to the lasagna and
    multiply by the `PREPARATION_TIME`
    """

    return number_of_layers * preparation_time


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.

    :param number_of_layers: int - number of layers added to the lasagna.
    :param elapsed_bake_time: int - number of minutes the lasagna has been baking in the oven
    :return: int - total number of minutes you've been cooking.
    """

    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
