# Chris Swanson and Chris Casey - CSC 440 - September 20, 2017
import sys
import time

start_time = time.time()

knights = {}
ladies = {}
engaged = {}
numPairs = 0

def read_file(filename):
    i = 0
    with open(filename, 'r') as f:
        # gets the first value of the file so that we know how many matches we need to make
        # this is a string value at the moment
        numPairs = f.readline()
        j = int(numPairs)

        # reads each of the other lines of the dictionary
        for line in f:
            if (i < j):
                items = line.split()
                key, values = items[0], items[1:]
                knights[key] = values
                i = i + 1
            else:
                items = line.split()
                key, values = items[0], items[1:]
                ladies[key] = values

def perfect_matches():
    # gets the next knight to be matched
    knights_left = [item[0:] for item in knights]

    while knights_left:
        # pops the first knight from the list
        current_knight = knights_left.pop(0)

        # Gets the current knights choice for a lady
        engagement_choices = knights[current_knight]

        # gets the ladies next preference for a knight
        current_lady = engagement_choices.pop(0)

        # matches current
        match = engaged.get(current_lady)

        # Checks to see if the lady is engaged
        if not match:
            engaged[current_lady] = current_knight
        else:
            # gets the current lady that needs to be matches
            ladiesToBeMatched = ladies[current_lady]

            if ladiesToBeMatched.index(match) > ladiesToBeMatched.index(current_knight):
                # The lady has found a better match
                engaged[current_lady] = current_knight

                if knights[match]:
                    # knight needs to look for another match
                    knights_left.append(match)
            else:
                if engagement_choices:
                    # Look again
                    knights_left.append(current_knight)
    return engaged

def print_pairings():
    # Prints out each match on its own line with the knight first and then
    for key, value in engaged.items():
        print(value, key)

def main():
    if len(sys.argv) == 2:
        read_file(sys.argv[1])

    elif len(sys.argv) == 1:
        print("Please enter the name of a file.")
        return 1

    else:
        print("Please enter a valid number of arguments!")
        return 1

    # Finds the matches for each knight and lady
    perfect_matches()

    # prints the pairings of knights and ladies
    print_pairings()

    print("-- %s seconds --" % (time.time() - start_time))

main()