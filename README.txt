The program print out the number of times the characters æ,ø,å occur in a text saved as "input.txt" (counts
both upper case and lower case letters). The program also replaces these characters and the words
grim, grimme, trist, skidt with the characters/words 
ae, oe, aa, virkelig smuk, virkelig smukke, glad, godt
The number of times the characters occur before and after the replacement is printed in the terminal.
The program also counts the length of all words after splitting the text file (splitting is based on empty
space and special characters). This word count distribution is then plotted as a box plot and histogram.


To run the program, run the "main.py" file.
This file uses the functions defined in the files:
"input_reader.py", "count.py", "replace.py", "print_count.py", "word_length_distribution_box_hist.py"

The main file defines the filenames "input.txt" and "replacement.txt". These are files with the text and 
characters/words with their replacements respectively.

The function in "input_reader.py" uses these two .txt files. 
For the function to work as intended the "replacement.txt" file should be structured as a character/word 
followed by a tab and the character/word to replace it, and then a new line for more characters/words. E.g:
æ	ae
å	aa
grim	virkelig smuk 
grimme	virkelig smukke