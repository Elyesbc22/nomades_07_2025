def create_empty_set() -> set:
    """
    Function to create an empty set.
    :return: An empty set.
    """
    return set()


def create_set_from_list(lst: list) -> set:
    """
    Function to create a set from a list.
    :param lst: The list to convert into a set.
    :return: A set created from the list.
    """
    return set(lst)


def add_element(s: set, element) -> None:
    """
    Function to add an element to a set.
    :param s: The set to add the element to.
    :param element: The element to add.
    """
    s.add(element)


def remove_element(s: set, element) -> None:
    """
    Function to remove an element from a set.
    If the element does not exist, no action is taken.
    :param s: The set to remove the element from.
    :param element: The element to remove.
    """
    s.discard(element)


def check_element(s: set, element) -> bool:
    """
    Function to check if an element exists in a set.
    :param s: The set to check.
    :param element: The element to look for.
    :return: True if the element exists in the set, False otherwise.
    """
    return element in s


def count_elements(s: set) -> int:
    """
    Function to count the number of elements in a set.
    :param s: The set to analyze.
    :return: The number of elements in the set.
    """
    return len(s)


def union_sets(s1: set, s2: set) -> set:
    """
    Function to find the union of two sets.
    :param s1: The first set.
    :param s2: The second set.
    :return: A set containing all elements from both sets.
    """
    return s1.union(s2)


def intersect_sets(s1: set, s2: set) -> set:
    """
    Function to find the intersection of two sets.
    :param s1: The first set.
    :param s2: The second set.
    :return: A set containing elements that are in both sets.
    """
    return s1.intersection(s2)


def difference_sets(s1: set, s2: set) -> set:
    """
    Function to find the difference of two sets.
    :param s1: The first set.
    :param s2: The second set.
    :return: A set containing elements in s1 but not in s2.
    """
    return s1.difference(s2)


def check_subset(s1: set, s2: set) -> bool:
    """
    Function to check if one set is a subset of another.
    :param s1: The first set.
    :param s2: The second set.
    :return: True if s1 is a subset of s2, False otherwise.
    """
    return s1.issubset(s2)


def check_disjoint(s1: set, s2: set) -> bool:
    """
    Function to check if two sets are disjoint (no common elements).
    :param s1: The first set.
    :param s2: The second set.
    :return: True if the sets are disjoint, False otherwise.
    """
    return s1.isdisjoint(s2)


def clear_set(s: set) -> None:
    """
    Function to clear all elements from a set.
    :param s: The set to clear.
    """
    s.clear()


def copy_set(s: set) -> set:
    """
    Function to create a copy of a set.
    :param s: The set to copy.
    :return: A copy of the set.
    """
    return s.copy()


def find_maximum(s: set) -> int:
    """
    Function to find the maximum element in a set.
    :param s: The set to analyze.
    :return: The maximum element in the set.
    """
    return max(s) if s else 0


def check_equal(s1: set, s2: set) -> bool:
    """
    Function to check if two sets are equal.
    :param s1: The first set.
    :param s2: The second set.
    :return: True if the sets are equal, False otherwise.
    """
    return s1 == s2