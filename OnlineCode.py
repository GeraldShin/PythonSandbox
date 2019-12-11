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
    
