###############################    MAIN FILE WHERE EVERYTHNG IS RUN AND WHAT IS WANTED CAN BE CHANGED    ###############################

# Main file where input text file can be changed and the name of modifed text can be changed. The characters/words to be counted can 
# also be changed. Right now it only print out the number of times a character occurs before/after the replacements for the characters
# æ, ø, å. But it would also be able to print out the count for the words that will be replaced.

########################################################################################################################################


# Defined functions
import count
import replace
import print_count
import word_length_dist_box_hist
import input_reader

# Read and save txt files
content, all, all_replacement = input_reader.input_reader("input.txt", "replacement.txt")
# Save just the characters æ,ø,å because we only want to print out the count for these
characters = all[:3]
# Name of the file with the replacements
file_out = "modified_text.txt"

# Count the number of times each character occurs
num_before = count.count(characters, content)
# Replace all given characters/words and safes the text in a new file 
content = replace.replace(content, all, all_replacement, file_out)
# Count numer of times each character occurs in the modified text
num_after = count.count(characters, content) # Gives list of number of times each character appears in text after replacement
# Print the numer of times each character occurs in the terminal before and after the replacements
print_count.print_count(characters, num_before, num_after)

# Plot the world length distribution of the modified text in a box plot and a histogram
word_length_dist_box_hist.word_length_dist_box_hist(content)