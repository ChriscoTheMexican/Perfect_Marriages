# Chris Swanson and Chris Casey - CSC 440 - September 20, 2017
import sys

knights = {
    'Galahad': ['Guinevere', 'Elaine'],
    'Lancelot': ['Guinevere', 'Elaine']}
ladies = {
    'Guinevere': ['Galahad', 'Lancelot'],
    'Elaine': ['Lancelot', 'Galahad']}
matches = []

def read_file(filename):
    with open(filename, 'r') as f:
        file = []

        # gets the first value of the file so that we know how many matches we need to make
        # this is a string value at the moment
        totalMatches = f.readline()
        # print(totalMatches, end='')

        # reads each of the other lines of the file
        for line in f:
            file.append(line)
            # print(line, end='')
    # print(file)

def perfect_matches():
    for key, value in knights.items():
        matches.append(key)
        matches.append(value)


    print(matches)

def main():
    read_file('ten.txt')
    perfect_matches()

main()