from stats import num_of_words
from stats import num_of_each_letter
import sys 

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)




print("============ BOOKBOT ============")
print("Analyzing book found at " + sys.argv[1] + "...")
print("----------- Word Count ----------")
print(num_of_words(sys.argv[1]))
print("--------- Character Count -------")
print(num_of_each_letter(sys.argv[1]))