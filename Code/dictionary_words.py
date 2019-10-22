import random
import sys
from rearrange import rearrange

DEBUG = True

dictionary = open('/usr/share/dict/words', 'r')
dictionary_list = list()

if DEBUG:
    print(dictionary)
def random_sentence(num_words):
    word_list = list() # final list of words

    num_lines = 0 # total word count
    for line in dictionary:
        num_lines += 1
        dictionary_list.append(line)

    rand_indexes = gen_rand_indexes(num_lines, num_words)

    for index in rand_indexes:
        word_list.append(dictionary_list[index])
    
    return rearrange(word_list)

def gen_rand_indexes(num_lines, num_indexes):
    indexes = list()
    for i in range(num_indexes): # for the number of idexes 
        index = random.randint(0, num_lines)
        while index in indexes: # keeps randomizing so we don't have repeated indexes
            index = random.randint(0, num_lines)
        indexes.append(index)
    
    return indexes

if __name__=='__main__':
    num_words = sys.argv[1:]

    print(random_sentence(int(num_words[0])))
