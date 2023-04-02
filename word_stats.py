# Bobb Shields
# wde677
#

# Stats for text passed in as the singular parameter
# First sprint: count_words
# Second sprint: count_lines, count_chars
#

# Count of the individual words.  
# All characters pushed to lowercase as to make this case insensitive
#
import string

def count_words(text):
    # replace tabs and newlines with spaces
    text = text.replace("\t", "*").replace("\n", "*").replace(" ", "*") #breaks? on "  " double space?
    #print(text) #debug

    if (text==""):
        raise ValueError("Input document cannot be empty")

    if (len(text)>=10000):
        print(text)
        raise ValueError("Input document exceeds maximum length")
    else:

        # split text into lowercase words
        words = text.lower().split("*")
    
        # count frequency of each unique word
        word_counts = {}
        for word in words:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
            
        return word_counts

def count_lines (text): #looks for all “\n” tokens in the given string

    line_count = 0
    for i in range(0,len(text) ):
        if text[i] == "\n": 
            line_count = line_count + 1

    return line_count

def count_chars(text): #CharCount is simply the length of the text field.

    print(f"len = {len(text)}")
    char_count = 0
    for char in text:
        if char not in string.whitespace:
            char_count += 1

    return char_count
