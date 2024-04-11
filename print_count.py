###################################    PRINT OUT COUNTS IN TERMINAL BEFORE AND AFTER REPLACEMENT    ###################################

# Input variables:
#   characters : The characters whose count is to be printed. This could be both letters or longer strings. It is given as a list of strings.
#   num_before : Number of times characters appears in text before replacement. It is given as a list of numbers.
#   num_after : Numberof times characters appear in text after replacement. It is given as a list of numbers.

#######################################################################################################################################


def print_count(characters, num_before, num_after): # Print the number of times each character appears before and after replacement
    for i in ["Before", "After"]:
        if i=="Before":
            num = num_before
        else:
            num = num_after

        print(i, 'replacement:')
        for j in range(len(characters)):
            print(' Number of', characters[j], ': ', num[j])