def sum(tableau: list[int]) -> int:
    """
    Function that returns the sum of the elements of the array
    :param tableau: the array to sum
    :return: the sum of the elements of the array
    """
    import builtins
    return builtins.sum(tableau) if tableau else 0


def average(tableau: list[int]) -> float:
    """
    Function that returns the average of the elements of the array
    :param tableau: the array to average
    :return: the average of the elements of the array
    """
    import builtins
    return builtins.sum(tableau) / len(tableau) if tableau else 0


def min(tableau: list[int]) -> int:
    """
    Function that returns the minimum of the elements of the array
    :param tableau: the array to find the minimum of
    :return: the minimum of the elements of the array
    """
    import builtins
    return builtins.min(tableau) if tableau else 0


def max(tableau: list[int]) -> int:
    """
    Function that returns the maximum of the elements of the array
    :param tableau: the array to find the maximum of
    :return: the maximum of the elements of the array
    """
    import builtins
    return builtins.max(tableau) if tableau else 0


def min_max(tableau: list[int]) -> tuple[int, int]:
    """
    Function that returns the minimum and maximum of the elements of the array
    :param tableau: the array to find the minimum and maximum of
    :return: the minimum and maximum of the elements of the array
    """
    import builtins
    if not tableau:
        return (0, 0)
    return (builtins.min(tableau), builtins.max(tableau))


def mode(tableau: list[int]) -> int:
    """
    Function that returns the mode of the elements of the array
    The mode is the value that appears most often in a set of data values.
    If there is a tie, the mode is the smallest value.
    :param tableau: the array to find the mode of
    :return: the mode of the elements of the array
    """
    if not tableau:
        return 0
    from collections import Counter
    import builtins
    counts = Counter(tableau)
    max_count = builtins.max(list(counts.values()))
    modes = [k for k, v in counts.items() if v == max_count]
    return builtins.min(modes)

def variance(tableau: list[int]) -> float:
    """
    Function that returns the variance of the elements of the array
    :param tableau: the array to find the variance of
    :return: the variance of the elements of the array
    """
    if not tableau:
        return 0.0
    import builtins
    mean = builtins.sum(tableau) / len(tableau)
    return builtins.sum([(x - mean) ** 2 for x in tableau]) / len(tableau)

        
    

def standard_deviation(tableau: list[int]) -> float:
    """
    Function that returns the standard deviation of the elements of the array
    The standard deviation is the square root of the variance.
    :param tableau: the array to find the standard deviation of
    :return: the standard deviation of the elements of the array
    """
    import math
    return math.sqrt(variance(tableau))


def exist(tableau: list[int], valeur: int) -> bool:
    """
    Function that returns True if the value exists in the array
    :param tableau: the array to check if the value exists in
    :param valeur: the value to check if it exists in the array
    :return: True if the value exists in the array, False otherwise
    """
    return valeur in tableau


def position(tableau: list[int], valeur: int) -> int:
    """
    Function that returns the position of the first value in the array
    If the value does not exist in the array, it returns -1
    :param tableau: the array to find the position of
    :param valeur: the value to find the position of
    :return: the position of the value in the array
    """
    try:
        return tableau.index(valeur)
    except ValueError:
        return -1


def similars(arr1: list[int], arr2: list[int]) -> bool:
    """
    Function that returns True if the two arrays are similar
    :param arr1: the first array
    :param arr2: the second array
    :return: True if the two arrays are similar, False otherwise
    """
    return sorted(arr1) == sorted(arr2)


def is_list(tableau) -> bool:
    """
    Function that returns True if the array is a table
    :param tableau: the array to check if it is a table
    :return: True if the array is a table, False otherwise
    """
    return isinstance(tableau, list)


def is_list_of_numbers(tableau) -> bool:
    """
    Function that returns True if the array is a table of numbers
    :param tableau: the array to check if it is a table of numbers
    :return: True if the array is a table of numbers, False otherwise
    """
    return isinstance(tableau, list) and all(isinstance(x, (int, float)) for x in tableau)


def sort_ascending(arr: list[int]) -> list[int]:
    """
    Function that returns the sorted array in ascending order 
    :param arr: the array to sort
    :return: the sorted array in ascending order
    """
    return sorted(arr)


def sort_descending(arr: list[int]) -> list[int]:
    """
    Function that returns the sorted array in descending order 
    :param arr: the array to sort
    :return: the sorted array in descending order
    """
    return sorted(arr, reverse=True)


def median(tableau: list[int]) -> int:
    """
    Function that returns the median of the elements of the array
    :param tableau: the array to find the median of
    :return: the median of the elements of the array
    """
    if not tableau:
        return 0
    sorted_arr = sorted(tableau)
    n = len(sorted_arr)
    if n % 2 == 0:
        return int((sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2)
    else:
        return sorted_arr[n//2]