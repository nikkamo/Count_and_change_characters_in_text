#####################################    PLOT BOXPLOT AND HISTOGRAM OF WORD LENGTH DISTRIBUTION    #####################################

# The function removes all special characters from the text and split words with special characters in between into different words.
# All blank spaces are then removed and the remaining words are put into a list. Then all words a counted and these numbers are put
# into a new list. This list is used to make the box plot and histogram.

# Input variable:
#   content : the text in which to count words

########################################################################################################################################


import matplotlib.pyplot as plt
from matplotlib import cbook
import numpy as np
#from scipy.stats import norm
from scipy.optimize import curve_fit 

def word_length_dist_box_hist(content):
    # Replace special characters with a space 
    special_characters = [',','.',':',';','!','?','"', '/', '(', ')']
    for string in special_characters:
        content = content.replace(string, " ")
    text_words = content.split() # Split up text by removing new lines and space

    # Count the length of all words and put it in a list
    word_lengths = []
    for word in text_words:
        word_lengths.append(len(word))

    # Make subplot for histogram and box plot
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.2, .8)}, figsize = (7,5))
    ax_box.grid()
    ax_hist.grid()

    # Box plot properties and plot
    boxprops = dict(color='purple', linewidth=3, label='Interquartile range')
    medianprops = dict(color='red', linewidth=3, label='Median')
    meanprops = dict(color='blue', linewidth=3, label='Mean')
    capprops = dict(color='magenta', linewidth=3, linestyle=':') #, label='Min and Max')
    flierprops = dict(marker='o', markerfacecolor='green', markersize=5, label='Outliers')

    ax_box.boxplot(word_lengths, vert = False, widths=0.8, showmeans = True, meanline = True,
                   meanprops=meanprops, flierprops=flierprops, boxprops=boxprops, medianprops=medianprops, capprops=capprops)

    # Add numbers above the quartiles, mean and minimum, maximum (including outliers)
    data = cbook.boxplot_stats(word_lengths)
    values = [data[0][i] for i in ['q1','med','q3','mean']] + [min(word_lengths),max(word_lengths)]
    for v in values:
        ax_box.text(v,1.6,str(round(v)),fontsize=9,horizontalalignment='center')

    ax_box.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=10)
    ax_box.set(xlabel=None) # Remove x axis lable for boxplot
    ax_box.set(ylabel=None)
    ax_box.xaxis.set_ticks_position('none') # Remove x-axis tick marks
    ax_box.yaxis.set_ticks_position('none')

    # Plot histogram 
    bins = range(min(word_lengths), max(word_lengths)+1)
    ax_hist.hist(word_lengths, histtype="bar", density=True, bins = bins, edgecolor="black") 
    ax_hist.set_xticks(bins)
    ax_hist.set_xticklabels(bins)

    ax_hist.set(xlabel='Word Length')
    ax_hist.set(ylabel='Probability')
    ax_hist.set(xlim=[min(word_lengths)-0.5, max(word_lengths)+1])

    f.suptitle('Box plot and histogram of word length distribution',fontsize=13,horizontalalignment='center')
    plt.show()