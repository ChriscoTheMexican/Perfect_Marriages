# Chris Swanson and Chris Casey - CSC 440 - September 20, 2017
import sys

# Global Variables
knights = {}
ladies = {}
matches = {}
numPairs = 0

# Reads in the given data file line by line
def read_file(filename):
    i = 0
    with open(filename, 'r') as f:
        # gets the first value of the file so that we know how many matches we need to make
        # this is a string value at the moment
        numPairs = f.readline()
        j = int(numPairs)

        # reads each of the other lines of the dictionary
        for line in f:
            # splits the knights and ladies into separate dictionaries
            if (i < j):
                items = line.split()
                key, values = items[0], items[1:]
                knights[key] = values
                i = i + 1
            else:
                items = line.split()
                key, values = items[0], items[1:]
                ladies[key] = values

# def perfect_matches():


# Prints out the matches in the specified format
def printPairings():
        print("Functionality to be added")

def main():
    read_file('ten.txt')
    perfect_matches()

main()