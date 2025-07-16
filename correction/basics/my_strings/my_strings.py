def count_words(sentence: str) -> int:
    """
    Function to count the number of words in a given sentence.
    :param sentence: The sentence to analyze.
    :return: The number of words in the sentence.
    """
    return len(sentence.split())


def reverse_word(word: str) -> str:
    """
    Function to reverse the characters in a word.
    :param word: The word to reverse.
    :return: The reversed word.
    """
    return word[::-1]


def is_palindrome(word: str) -> bool:
    """
    Function to check if a word is a palindrome.
    A palindrome is a word that reads the same backward as forward.
    :param word: The word to check.
    :return: True if the word is a palindrome, False otherwise.
    """
    return word.lower() == word.lower()[::-1]


def count_characters(word: str) -> int:
    """
    Function to count the number of characters in a word.
    :param word: The word to analyze.
    :return: The number of characters in the word.
    """
    return len(word)


def count_letters(word: str) -> int:
    """
    Function to count the number of alphabetic letters in a word.
    :param word: The word to analyze.
    :return: The number of letters in the word.
    """
    return sum(1 for char in word if char.isalpha())


def count_vowels(word: str) -> int:
    """
    Function to count the number of vowels in a word.
    :param word: The word to analyze.
    :return: The number of vowels in the word.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)


def count_consonants(word: str) -> int:
    """
    Function to count the number of consonants in a word.
    :param word: The word to analyze.
    :return: The number of consonants in the word.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char.isalpha() and char not in vowels)


def concatenate_words(word1: str, word2: str) -> str:
    """
    Function to concatenate two words into a single string.
    :param word1: The first word.
    :param word2: The second word.
    :return: The concatenated string.
    """
    return word1 + word2