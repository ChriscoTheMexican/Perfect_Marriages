# Chris Swanson and Chris Casey - CSC 440 - September 20, 2017
import sys

knights = {
    'Galahad': ['Guinevere', 'Elaine'],
    'Lancelot': ['Guinevere', 'Elaine']}
ladies = {
    'Guinevere': ['Galahad', 'Lancelot'],
    'Elaine': ['Lancelot', 'Galahad']}
matches = []

def getdata(fname):
    file = open(fname, 'r')
    # input = open ('inputfilename', 'r')

    with open(fname, 'r') as f:
        first_line = f.readline()
    print(first_line)

    lines = []
    with open(fname) as file:
        for line in file:
            line = line.strip()
            lines.append(line)
    lines.pop(0)

    i = 0
    while i < (len(lines) / 2):
        knights.append(lines[i])
        i = i + 1

    while (i + 1) <= (len(lines)):
        ladies.append(lines[i])
        i += 1

def perfect_matches():
    x = 0

def main(argv):
    file_name = sys.argv[0]
    getdata(file_name)

main("10.txt")