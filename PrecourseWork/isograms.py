"""
Implement a function that counts the number of isograms in a list of strings.
    * An isogram is a word that has no repeating letters, consecutive or non-consecutive.
    * Assume the empty string is an isogram and that the function should be case insensitive.
"""


def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True


def isogram(in_file):
    with open(in_file) as f:
        print(f)
        text = f.read()
        print(text)
        words = [word for word in text if word.isalpha()]
        print(words)
        for word in words:
            print(word)
            for char in word:
                print(char)
                if word.count(char) > 1:
                    words.remove(word)
    print(words)
    return words


def better_isogram(in_file):
    with open(in_file) as f:
        isograms = [word for word in f if word == set(word)]

    print(isograms)
    yield isograms


# def best_isogram(in_file):
#     with open(in_file) as f:
#         words = f.read().split()
#         for word in words:
#             if set(word) in words:
#                 isograms.append(word)
#
#     print(isograms)
#     yield isograms

print("\nIsograms:")
isogram('/Users/david/dev/Galvanize/PrecourseWork/SelfAssessment/data/test.txt')
print("\nBetter Isograms:")
better_isogram('data/test.txt')
# print("\nBest Isograms:")
# best_isogram(['iso', 'sio'])