#This will be snippets of useful code you find online that you can copy+paste when needed.


#Emoji Package
#I don't know when this will ever be helpful, but there is an Emoji package in Python.

$ pip install emoji

from emoji import emojize
print(emojize(":thumbs_up:")) #thumbs up emoji, check notes for more.

#List comprehensions
#You could probably get better at these... here is an easy example for reference

numbers = [1,2,3,4,5,6,7]
evens = [x for x in numbers if x % 2 is 0]
odds = [y for y in numbers if y not in evens]
cities = ['London', 'Dublin', 'Oslo']
def visit(city):
    print("Welcome to "+city)
for city in cities:
    visit(city)
    
def split_lines(s): #split a string into pieces using a separator
  return s.split('\n')
split_lines('50\n python\n snippets')


language = "python" #reverse the order of the letters in a word                                 
reversed_language = language[::-1]
print(reversed_language)

def union(a,b): #find elements that exist in both lists
  return list(set(a + b))
union([1, 2, 3, 4, 5], [6, 2, 8, 1, 4])


def unique(list): #finds if all elements in a list are unique
    if len(list)==len(set(list)):
        print("All elements are unique")
    else:
        print("List has duplicates")
unique([1,2,3,4,5]) # All elements are unique


from collections import Counter #counts freq of appearance of elements
list = [1, 2, 3, 2, 4, 3, 2, 3]
count = Counter(list)
print(count) # {2: 3, 3: 3, 1: 1, 4: 1}

def most_frequent(list): #piggy-backing, finds most freq appearance of elements
    return max(set(list), key = list.count)
numbers = [1, 2, 3, 2, 4, 3, 1, 3]
most_frequent(numbers) # 3

def multiply(n): #mapping applies the function in the parens to the data element in the parens
    return n * n 
  
list = (1, 2, 3) 
result = map(multiply, list) 
print(list(result)) # {1, 4, 9}

