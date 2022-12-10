import time
from typing import Callable


def calc_time(fn: Callable, text:str):
    start = time.time()
   
    print(fn(text))
    
    end = time.time()
    print(f"Execution time: {end - start}s")

def processor(name:str) -> Callable:
    print(name)

class Processor:
    def __init__(self, word_ind, num_words):
        self.word_ind = word_ind
        self.num_words = num_words
        
    def __call__(self, text):
        lst_words = text.split()
        return lst_words[self.word_ind: self.word_ind + self.num_words]

func = Processor(1, 4)
calc_time(func, 'Alex Mylnikov age 76')