# Bobb Shields
# wde677
#

# Stats for text passed in as the singular parameter
# First sprint: count_words
# Second sprint: count_lines, count_chars, check_input
# Third sprint: replace_word, check_input([list])

import string
import re

def print_stats(text):
    """Simple helper function to count lines & chars & words

    Args:
        text (string): Any given text: A paragraph with symbols, punctuation, numbers, and letters. 

    Returns:
        null: Prints a summary of the three functions.  Used in main.py
    """
    return ("Num Lines: " + str(count_lines(text)) +"\n" +
            "Num Chars: " + str(count_chars(text)) + "\n" +
            "Word Counts by freq:\n" + str(count_words(text) )
        )

def check_input(text):
    """Global input bounds checker that throws specific errors if failed

    Args:
        text (string): Any given text: A paragraph with symbols, punctuation, numbers, and letters. 

    Raises:
        TypeError: Check for string or list
        TypeError: When a list - check elements for whether string
        ValueError: Cannot be empty
        ValueError: Exceding maximum text length

    Returns:
        boolean: Returns true, if no errors were thrown
    """
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

def to_upper_or_lower(validated_text, toCase):
    """Transform the text to lower- or uppercase

    Args:
        validated_text (string): Any given text: A paragraph with symbols, punctuation, numbers, and letters. Should already be checked by check_input
        toCase (string): Flags: {'lower', 'upper', 'sensitive'}
    """
     #check case
    match toCase:
        case "lower":
            validated_text= validated_text.lower()
        case "upper":
            validated_text= validated_text.upper()
        case "sensitive":
            #do nothing
            print("")
        case _:
            print("Case parameter = "+ toCase + ". Not performing upper or lower conversion, defaulting to case sensitive.")
    return validated_text

def count_words(text,toCase ='lower', tokenizers=["\t","\n"," "] ):
    """Count of the individual words.  

    Args:
        text (string): Any given text: A paragraph with symbols, punctuation, numbers, and letters. 
        toCase (str, optional): Transform text to 'upper' or 'lower' case, or stay case 'sensitive'. Defaults to 'lower'.
        tokenizers (list, optional): User provided list of tokens upon which to split the text. Defaults to ["\t","\n"," "].

    Returns:
        dictionary: The individual words and their counts, sorted from highest to lowest
    """
    #check input text and it will throw errors if needed
    check_input(text)
    
    #Convert text to upper or lower, if specified in the parameters
    text = to_upper_or_lower(text, toCase)
        
    for token in tokenizers:   
        # replace tabs and newlines with spaces
        text = text.replace(token, " ")

    # split text into lowercase words
    words = text.split(" ")
    
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

def count_lines (text): #looks for all \n tokens in the given string
    """Count of the lines: num(newline chars) + 1

    Args:
        text (string): Any given text: A paragraph with symbols, punctuation, numbers, and letters. 

    Returns:
        integer: Returns the number of lines in the text
    """
    #check input and it will throw errors if needed
    check_input(text)

    # Line count starts at 1 because a non-empty string with no \n's is itself a line 
    line_count = 1
    for i in range(0,len(text) ):
        if text[i] == "\n": 
            line_count = line_count + 1

    return line_count

def count_chars(text, toCase ='lower'): 
    """Count of the individual characters of the input text with whitespace removed (space, tab, linefeed, return, formfeed, and vertical tab)

    Args:
        text (string): Any given text: A paragraph with symbols, punctuation, numbers, and letters. 
        toCase (str, optional): Transform text to 'upper' or 'lower' case, or stay case 'sensitive'. Defaults to 'lower'.

    Returns:
        integer: Returns the number of non-trivial characters in the text
    """
    #check input and it will throw errors if needed
    check_input(text)
    
    #Convert text to upper or lower, if specified in the parameters
    text = to_upper_or_lower(text, toCase)

    print(f"len = {len(text)}")
    char_count = 0
    for char in text:
        if char not in string.whitespace:
            char_count += 1

    return char_count



def replace_word(text, find, replace):
    """# Replace a word within a string.  Uses regular expression to evaluate against the whole word

    Args:
        text (string): Any given text: A paragraph with symbols, punctuation, numbers, and letters. 
        find (string): The word or body of text to be replaced
        replace (string): The word or body of text to be substituted in 
    
    Returns:
        string: Original text with keywords replaced
    """
    #check inputs and it will throw errors if needed
    check_input( [text, find, replace] )

   # use regular expression to match whole words only
    pattern = r'\b{}\b'.format(re.escape(find))
    text = re.sub(pattern, replace, text ) # <- Case sentitivity flag goes here if needed in future

    return text
