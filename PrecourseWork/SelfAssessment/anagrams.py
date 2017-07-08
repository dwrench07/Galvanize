from collections import defaultdict


def anagram(word_list):
    """
    1. Create a defaultDict - Returns a new dictionary-like object.
    Using list as the default_factory, it is easy to group a sequence of key-value pairs into a dictionary of lists.

    Example:
        >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
        >>> d = defaultdict(list)
        >>> for k, v in s:
        ...     d[k].append(v)
        ...
        >>> sorted(d.items())
        [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

    Explanation:
        When each key is encountered for the first time, it is not already in the mapping;
        so an entry is automatically created using the default_factory function which returns an empty list.
        The list.append() operation then attaches the value to the new list.
        When keys are encountered again,
        the look-up proceeds normally (returning the list for that key)
        and the list.append() operation adds another value to the list.

    2. Loop through the list of words
    2.1. Lowercase words - So we can sort them all the same (no [a-zA-Z] issues)
    2.2. Sort the words - Giving us the words sorted alphabetically

    Example:
        'live' and 'evil' both == 'eilv' when sorted

    2.3. Join the words in a list - 'eilv' is then stored in the table
    2.4. Append the word to the list

    3. Loop through each item in the defaultDict
    3.1. If there is more than one (1) it is an anagram

    Example:
        {..., 'eilv': ['evil', 'live'], ...}

    4. Return the list of anagrams

    :param word_list:
    :return results:
    """
    anagrams = defaultdict(list)

    for word in word_list:
        anagrams[''.join(sorted(word.lower()))].append(word)
        result = [v for k, v in anagrams.items() if len(v) > 1]

    print(result)


anagram(['si', 'ton', 'is', 'not', 'in', 'grandma', 'anagram', 'aaagnmr'])
