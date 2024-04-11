#########################################    COUNT NUMBER OF TIMES CHARACTERS OCCUR IN TEXT    #########################################

# Input variables:
#   characters : The characters to be counted. This could be both letters or longer strings. It is given as a list of strings.
#   content : The text in which to count characters. It is given as a string.
#   num : Initial number of times the characters appear. This is lso given as a list as long as characters.
#   case_sensitive : If true it counts characters both if they are upper or lower case letters. If False only counts characters as
#                    defined in the characters list.

# Output variables:
#   num_updated : A list of the number of times each character appears in the text.

########################################################################################################################################


def count(characters, content, num=None, case_sensitive=True): # Count number of times each character appears in each line
    if num is None:
        num_updated = [0 for i in characters] # Default initial counts are zero.
    else:
        num_updated = num.copy() # Do not change original num as output

    for lines in content.split('\n'): # Go through each line of txt file (easier to check if gives correct number) - but could go through whole content instead
        if case_sensitive:
            line = lines.lower() # Make everything lower case so upper case letters are also counted
        else: 
            line = lines

        for char in characters: # Go through each character we are considering
             index = characters.index(char) # Returns index of first character with value char
             count = line.count(char) # Returns number of times char appears in line
             num_updated[index] += count # Update number of times the character appears by adding the number of times it appears in the line
    return num_updated