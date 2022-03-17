''' Lab_1 '''
import os
from StringSplit import SplitW, SplitL


def fuct(number_of_ngrams: int, top_k: int):
    if number_of_ngrams == 0 or top_k == 0:
        raise ValueError("Incorrect input")
    input_string: str = input("str:\n")
    words: SplitW = SplitW(input_string, top_k, number_of_ngrams)
    letters: SplitW = SplitL(input_string, top_k, number_of_ngrams)
    words.count_words()
    words.print_dictionary()
    display(words)
    letters.create_dictionary()
    letters.find_top()
    
def display(words: SplitW):
    print(f"\nMedian: {words.find_median()}")
    print(f"Average: {words.find_average()}\n")
    
try:
    n: int = int(input("Enter N: "))
    k: int = int(input("Enter K: "))
    funct(n, k)

except ValueError as value_error:
    print(value_error)

except EOFError as exception:
    print(exception)
