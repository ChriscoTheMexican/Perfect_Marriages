# Chris Swanson and Chris Casey - CSC 440 - September 20, 2017
import sys

knights = {}
ladies = {}
people = {}

knights1 = {
    'Galahad': ['Guinevere', 'Elaine'],
    'Lancelot': ['Guinevere', 'Elaine']}
ladies1 = {
    'Guinevere': ['Galahad', 'Lancelot'],
    'Elaine': ['Lancelot', 'Galahad']}
matches = []
numPairs = 0

def read_file(filename):
    with open(filename, 'r') as f:
        file = []

        # gets the first value of the file so that we know how many matches we need to make
        # this is a string value at the moment
        numPairs = f.readline()

        # reads each of the other lines of the dictionary
        for line in f:
            items = line.split()
            key, values = items[0], items[1:]
            people[key] = values
        print("Number of pairs: ", numPairs)
        print(people, end='')

def printPairings():
    print("Functionality to be added")

def perfect_matches():
    for key, value in knights1.items():
        matches.append(key)
        matches.append(value)

def main():
    read_file('ten.txt')
    perfect_matches()

main()