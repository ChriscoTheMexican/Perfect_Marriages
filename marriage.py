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

        # Exits the program if the first value is not an even number
        if int(numPairs) % 2 != 0:
            sys.exit(1)

        # Initialization: if the input file is empty then no matches need to be made
        # Exits the program if the file is empty
        if not numPairs:
            sys.exit(1)

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
    # Maintenance: keeps a record of how many available bachelors are left
    # gets the next knight to be matched
    knights_left = [item[0:] for item in knights]

    # loop invariant: for all knights in the knights dictionary, add them to
    # knights_left, and will iterate through knights_left until the length
    # of knights_left is empty. --> len(knights_left) == 0
    while knights_left:
        # pops the first knight from the list
        current_knight = knights_left.pop(0)

        # Maintenance: takes the knight that was removed from the dictionary and puts
        # his choices into a list

        # Gets the current knights choice for a lady
        engagement_choices = knights[current_knight]

        # Maintenance: takes the ladies choices of a knight

        # gets the ladies next preference for a knight
        current_lady = engagement_choices.pop(0)

        # Maintenance: Reply's maybe to the person waiting to see if a better match
        # will become available

        # matches current
        matched = engaged.get(current_lady)

        # Checks to see if the lady is engaged
        if not matched:
            engaged[current_lady] = current_knight

        # If she is matched, check to see if the there is a better match
        else:
            # Base Case: The lady is engaged

            # gets the current lady
            ladiesToBeMatched = ladies[current_lady]

            # Induction: takes the current lady and makes a comparision to the knight,
            # if the lady found a better match the knight will go back and look for another lady
            # another induction step will go to the next knight and will continue to do so until
            # one of two things either there is a perfect match, or for the the length of the

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

    # Termination: When the list of available knights (knights_left) is empty
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