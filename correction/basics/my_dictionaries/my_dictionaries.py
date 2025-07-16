from typing import Dict, Any

def create_empty_dictionary() -> Dict[Any, Any]:
    """
    Function to create an empty dictionary.
    :return: An empty dictionary.
    """
    return {}


def add_key_value(dictionary: Dict[Any, Any], key: Any, value: Any) -> None:
    """
    Function to add a key-value pair to a dictionary.
    :param dictionary: The dictionary to add to.
    :param key: The key to add.
    :param value: The value associated with the key.
    :return: None.
    """
    dictionary[key] = value


def get_value(dictionary: Dict[Any, Any], key: Any) -> Any:
    """
    Function to get the value associated with a key in a dictionary.
    :param dictionary: The dictionary to search.
    :param key: The key to look for.
    :return: The value associated with the key.
    """
    return dictionary.get(key)


def check_key(dictionary: Dict[Any, Any], key: Any) -> bool:
    """
    Function to check if a key exists in the dictionary.
    :param dictionary: The dictionary to check.
    :param key: The key to look for.
    :return: True if the key exists, False otherwise.
    """
    return key in dictionary


def remove_key_value(dictionary: Dict[Any, Any], key: Any) -> None:
    """
    Function to remove a key-value pair from the dictionary.
    :param dictionary: The dictionary to modify.
    :param key: The key to remove.
    :return: None.
    """
    if key in dictionary:
        del dictionary[key]


def count_key_value_pairs(dictionary: Dict[Any, Any]) -> int:
    """
    Function to count the number of key-value pairs in a dictionary.
    :param dictionary: The dictionary to count.
    :return: The number of key-value pairs.
    """
    return len(dictionary)


def get_keys(dictionary: Dict[Any, Any]) -> list:
    """
    Function to get the keys of a dictionary.
    :param dictionary: The dictionary to extract keys from.
    :return: A list of keys.
    """
    return list(dictionary.keys())


def get_values(dictionary: Dict[Any, Any]) -> list:
    """
    Function to get the values of a dictionary.
    :param dictionary: The dictionary to extract values from.
    :return: A list of values.
    """
    return list(dictionary.values())


def get_items(dictionary: Dict[Any, Any]) -> list:
    """
    Function to get the key-value pairs (items) of a dictionary.
    :param dictionary: The dictionary to extract items from.
    :return: A list of tuples representing key-value pairs.
    """
    return list(dictionary.items())


def update_values(dictionary: Dict[Any, Any], key: Any, value: Any) -> None:
    """
    Function to update the value of a specific key in the dictionary.
    :param dictionary: The dictionary to modify.
    :param key: The key whose value needs to be updated.
    :param value: The new value to set for the key.
    :return: None.
    """
    dictionary[key] = value


def merge_dictionaries(dictionary1: Dict[Any, Any], dictionary2: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Function to merge two dictionaries.
    :param dictionary1: The first dictionary.
    :param dictionary2: The second dictionary.
    :return: A new dictionary containing the merged key-value pairs.
    """
    merged = dictionary1.copy()
    merged.update(dictionary2)
    return merged


def clear_dictionary(dictionary: Dict[Any, Any]) -> None:
    """
    Function to clear all key-value pairs from a dictionary.
    :param dictionary: The dictionary to clear.
    :return: None.
    """
    dictionary.clear()


def find_key_with_max_value(dictionary: Dict[Any, Any]) -> Any:
    """
    Function to find the key with the maximum value in a dictionary.
    :param dictionary: The dictionary to search.
    :return: The key with the maximum value.
    """
    if not dictionary:
        return None
    max_key = None
    max_value = None
    for key, value in dictionary.items():
        if max_value is None or value > max_value:
            max_value = value
            max_key = key
    return max_key


def find_key_with_min_value(dictionary: Dict[Any, Any]) -> Any:
    """
    Function to find the key with the minimum value in a dictionary.
    :param dictionary: The dictionary to search.
    :return: The key with the minimum value.
    """
    if not dictionary:
        return None
    min_key = None
    min_value = None
    for key, value in dictionary.items():
        if min_value is None or value < min_value:
            min_value = value
            min_key = key
    return min_key


def check_same_key_value_pairs(dictionary1: Dict[Any, Any], dictionary2: Dict[Any, Any]) -> bool:
    """
    Function to check if two dictionaries have the same key-value pairs.
    :param dictionary1: The first dictionary.
    :param dictionary2: The second dictionary.
    :return: True if both dictionaries have the same key-value pairs, False otherwise.
    """
    return dictionary1 == dictionary2