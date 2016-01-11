import string
import sys
import collections

def get_word_count(filepath):
    new_file = open(filepath)
    word_counts = collections.Counter()

    for line in new_file:
        words = normalize_line(line)
        for word in words:
            word_counts[word] += 1

    new_file.close()

    return word_counts

def print_word_count(dictionary):
    for word, count in dictionary.iteritems():
        print word, count

def normalize_line(line):
    # string.punctuation contains a string of puncuation marks
    for punctuation in string.punctuation:
        line = line.replace(punctuation, " ")
    new_line = line.rstrip().lower().split(" ")
    return [words for words in new_line if words]



print_word_count(get_word_count(sys.argv[1]))