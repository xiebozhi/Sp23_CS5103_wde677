# Bobb Shields
# wde677
#

# Stats for text passed in as the singular parameter
# First sprint: count_words
# Second sprint: count_lines, count_chars
#
import string

# Combine all the functions together in one function, for ease   
# 
#
def print_stats(text):

    return ( "Num Lines: " + str(count_lines(text)) +"\n" +
            "Num Chars: " + str(count_chars(text)) + "\n" +
            "Word Stats:\n" + str(count_words(text) )
        )

# One function, near the top, that enables input error checking for all functions  
# 
#
def check_input(text):

    if (text==""):
        raise ValueError("Input cannot be empty")

    if (len(text)>=10000):
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
            
    return word_counts

# Count of the lines.  
# (Counting the new strings)
#
def count_lines (text): #looks for all “\n” tokens in the given string
    #check input and it will throw errors if needed
    check_input(text)

    # Line count starts at 1 because a non-empty string with no \n's is itself a line 
    line_count = 1
    for i in range(0,len(text) ):
        if text[i] == "\n": 
            line_count = line_count + 1

    return line_count

# Count of the individual characters.  
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
