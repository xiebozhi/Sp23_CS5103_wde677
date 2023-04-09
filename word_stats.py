# Bobb Shields
# wde677
#

# Stats for text passed in as the singular parameter
# First sprint: count_words
# Second sprint: count_lines, count_chars, check_input
# Third sprint: replace_word, check_input([list])

import string
import re

# Combine function calls with same parameter together to print and label 
# Just a courtesy 
#
def print_stats(text):

    return ("Num Lines: " + str(count_lines(text)) +"\n" +
            "Num Chars: " + str(count_chars(text)) + "\n" +
            "Word Counts by freq:\n" + str(count_words(text) )
        )

# Global input bounds checker that throws specific errors if failed  
# 
#
def check_input(text):

    #if input is a single string, save as a list
    if isinstance(text, str):
        text_list = [text]
    elif isinstance(text, list):
        text_list = text
    else:
        raise TypeError("Input must be a string or a list")

    for text in text_list:
        if not isinstance(text, str):
            raise TypeError("Elements in list must be strings")

        if text == "":
            raise ValueError("Input cannot be empty")

        if len(text) >= 10000:
            print(text)
            raise ValueError("Input exceeds maximum length")
    
    return True

# Count of the individual words.  
# All characters pushed to lowercase as to make this case insensitive
#
def count_words(text):
    #check input and it will throw errors if needed
    check_input(text)

    # replace tabs and newlines with spaces
    text = text.replace("\t", "*").replace("\n", "*").replace(" ", "*") #breaks? on "  " double space?

    # split text into lowercase words
    words = text.lower().split("*")
    
    # count frequency of each unique word
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
            
    # sort dictionary by value in descending order
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

    return sorted_word_counts

# Count of the lines.  
# number of new line characters + 1 
#
def count_lines (text): #looks for all \n tokens in the given string
    #check input and it will throw errors if needed
    check_input(text)

    # Line count starts at 1 because a non-empty string with no \n's is itself a line 
    line_count = 1
    for i in range(0,len(text) ):
        if text[i] == "\n": 
            line_count = line_count + 1

    return line_count

# Count of the individual characters
# Whitespace removed (space, tab, linefeed, return, formfeed, and vertical tab)
#
def count_chars(text): #CharCount is simply the length of the text field.
    #check input and it will throw errors if needed
    check_input(text)

    print(f"len = {len(text)}")
    char_count = 0
    for char in text:
        if char not in string.whitespace:
            char_count += 1

    return char_count

# Replace a word within a string.  
# Uses regular expression to evaluate against the whole word
# Adding ", flags=re.IGNORECASE" as arg to re.sub() affects case sensitivity 
def replace_word(text, find, replace):
    #check inputs and it will throw errors if needed
    check_input( [text, find, replace] )

   # use regular expression to match whole words only
    pattern = r'\b{}\b'.format(re.escape(find))
    text = re.sub(pattern, replace, text ) # <- Case sentitivity flag goes here if needed in future

    return text
