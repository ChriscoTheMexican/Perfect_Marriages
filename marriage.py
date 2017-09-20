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
        numPairs = f.readline()
        j = int(numPairs)

        # reads each of the other lines of the dictionary
        for line in f:
            # reads the first half of the file into the knights dictionary
            if (i < j):
                items = line.split()
                key, values = items[0], items[1:]
                knights[key] = values
                i = i + 1
            # reads the second half of the file into the ladies dictionary
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
        matched = engaged.get(current_lady)

        # Checks to see if the lady is engaged
        if not matched:
            engaged[current_lady] = current_knight

        # If she is matched, check to see if the there is a better match
        else:
            # gets the current lady
            ladiesToBeMatched = ladies[current_lady]

            # checks to see lady has found a better match
            if ladiesToBeMatched.index(matched) > ladiesToBeMatched.index(current_knight):
                engaged[current_lady] = current_knight

                # knight needs to look for another match, because a better match has been found
                if knights[matched]:
                    knights_left.append(matched)

            # No better match has been found so they lady keeps looking for a better match
            else:
                if engagement_choices:
                    knights_left.append(current_knight)
    return engaged


def print_pairings():
    # Prints out each match on its own line with the knight first and then
    for key, value in engaged.items():
        current_marriage = value + " " + key + "\n"
        sys.stdout.write(current_marriage)


def main():
    # Input validation to handle user input, only one file name can be entered
    if len(sys.argv) == 2:
        read_file(sys.argv[1])
    else:
        sys.exit(1)

    perfect_matches()

    print_pairings()

    # print("-- %s seconds --" % (time.time() - start_time))


main()