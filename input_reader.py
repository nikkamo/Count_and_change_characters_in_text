######################################    READ TEXT, CHARACTERS/WORDS AND THEIR REPLACEMENT    ######################################

# Input variables:
#   text_path : The text to go through and replace characters/words in. Can be given as a txt file.
#   replacement_path : File with characters/words and their replacement. It should be written as a character/word followed by a tab
#                      and the character/word to replace it, and then a new line for more characters/words. E.g:
#                      æ    ae
#                      å    aa
#                      grim     virkelig smuk 
#                      grimme   virkelig smukke

# Output variables:
#   content : String of text_path.
#   all : List of strings containing characters/words in the text to change.
#   all_replacement : List of strings containing the replacement of characters/words in the text.

########################################################################################################################################


import re

def input_reader(text_path, replacement_path):
    
    f = open(text_path, 'r', encoding='utf-8') # Making sure file is read using UTF-8 encoding. 
    content = f.read()
    f.close() # No need for file after saving text as content

    f = open(replacement_path, 'r', encoding='utf-8')
    input = f.read()
    delimiters = "\t", "\n" # Split by tab and new line
    regex_pattern = '|'.join(map(re.escape, delimiters))
    input = re.split(regex_pattern, input) # input is now a list with strings
    f.close()
    
    all = []
    all_replacement = []
    for i,word in enumerate(input): # If the file is written the way explained, every other element is word and the other its replacement
        if i % 2 == 0:
            all.append(word)
        else:
            all_replacement.append(word)

    return content, all, all_replacement