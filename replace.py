###########################################    REPLACE STRINGS IN TEXT WITH OTHER STRINGS    ###########################################

# Input variables:
#   content : The text in which to replace strings. It is given as a string.
#   all : The original strings from text to be replaced. It is given as a list of strings.
#   all_replacement : The strings to act as replacements in the text. It is given as a list of strings.
#   file_out : Name of modified file with the replacements. It is given as a string, e.g. "output.txt".

# Output variables:
#   content : Modified text with the replacements. It is given as a string.

########################################################################################################################################


def replace(content, all, all_replacement, file_out): # Replace characters/words and add to a new txt file
    fout = open(file_out, "w") # Make a new txt file to add replacements
    content_words = content.split(' ') # Split up the long text into each word (space-seperated)
    for index,word in enumerate(content_words):
        if word.startswith("https://"): # If come across a link then continue to next word
            continue

        for i in range(len(all)): # Replacing characters
            word_lowercase = word.lower() # Make all leters in word lower case to check if character is in word
            if all[i] in word_lowercase: 
                find_index = word_lowercase.index(all[i])
                if word[find_index].istitle(): # If the character in the word is upper case make the replacement have first letter as upper case
                    replace = all_replacement[i].title()
                    word = word.replace(all[i].title(), replace)
                else:
                    replace = all_replacement[i]
                    word = word.replace(all[i], replace)
                content_words[index] = word

    content = ' '.join(content_words) # Join the words back together to form the long string again - now with the replacements
    fout.write(content)
    fout.close()
    return content