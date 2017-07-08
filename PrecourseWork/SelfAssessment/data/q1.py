#!/bin/python
"""Question 1:

Create a text content analyzer. This is a tool used by writers to find statistics 
such as word and sentence count on essays or articles they are writing.

Write a Python program that analyzes input from a file and compiles statistics on it.

The program should output:

1. The total word count
2. The count of unique words
3. The number of sentences

Example output:

Total word count: 468  
Unique words: 223  
Sentences: 38

Brownie points will be awarded for the following extras:
1. The ability to calculate the average sentence length in words
2. The ability to find often used phrases (a phrase of 3 or more words used over 3 times)
3. A list of words used, in order of descending frequency
4. The ability to accept input from STDIN, or from a file specified on the command line.

This question should be written in Python. 

"""

import os
import sys
import re
from collections import Counter


def text_context_analyzer(in_file):

    try:

        if os.stat(in_file).st_size > 0 and os.path.isfile(in_file):
            print("Analyzing '{}'...\n".format(os.path.basename(in_file)))

            with open(in_file, 'r', encoding='utf-8') as f:

                text = f.read().strip()
                counter = Counter(text.split())
                # values() = total of all (v)alues from counter k, v
                word_count = sum(counter.values())

                print('    Word Count = {:,}'.format(word_count))
                print('  Unique Words = {:,}\n'.format(len(counter)))
                print('Top 5 Most Frequent Words:')
                for k, v in counter.most_common(5):
                    print('{}: {:,}'.format(k, v))
                print()

                sentences = len(re.findall(r"[.!?]+", text))
                # Since we already have the word count, we don't need to
                # iterate over the sentences and count words
                sentence_avg_length = round(word_count / sentences, 2)

                print('     Sentence Count = {:,} words'.format(sentences))
                print('Avg Sentence Length = {:,} words'.format(sentence_avg_length))
                print('            Phrases = meh... did not accomplish.')

        else:
            print('Text Analyzer Canceled.')
            sys.exit(1)

    except Exception as e:
        print(e)


if __name__ == '__main__':

    print('-------------------------')
    print('  Text Context Analyzer  ')
    print('-------------------------')

    in_file = input('What file would you like to analyze? ')
    text_context_analyzer(in_file)

    print()
    print('Done.')
