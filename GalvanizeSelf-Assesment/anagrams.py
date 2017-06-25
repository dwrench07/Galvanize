from collections import Counter


# Create a dictionary for anagram key value pairs.
anagrams = {}


def anagram(word_list):
    # Loop through the given list
    for word in word_list:
        Counter(word)
        # Compare the current item to the next item
        current_item, next_item = word_list[idx], word_list[idx + 1]
        # Get a count on each item
        if Counter(current_item) == Counter(next_item):
            # Add anagrams to anagram dict
            anagrams[current_item] = next_item

    return print(anagrams)

anagram(['anagram', 'si', 'ton', 'is', 'not', 'in', 'grandma', 'anagram', 'aaagnmr'])

