# A E I O U
from itertools import product

def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    
    for i in range(len(words)):
        prod = list(product(words, repeat = i + 1))
        for p in prod:
            dictionary.append(''.join(p))
    dictionary.sort()
    
    return dictionary.index(word) + 1