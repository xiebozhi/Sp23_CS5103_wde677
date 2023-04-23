# Sp23_CS5103_wde677
# Bobb Shields
# wde677

##CS 5103 Course Project: Software Engineering Practice##

Schedule: 
Mar. 10th: Requirements, implementation (with repo link), unit tests, and readme file (describing how to run your code) for the first batch of requirement. 
Mar. 31th: Requirements, implementation (with the same repo link), unit tests, and readme file (describing how to run your code) for the second batch of requirement. 
Apr. 28th: Requirements, implementation (with repo link), readme file, for the last batch of requirement, design change report (reporting the design principles and design  
patterns you used if any), tool application report (reporting the results and experience of using automatic tools mentioned above). 

Code Example:
from word_stats import count_words
print_stats("I love coding.  Don't you love coding?")

Unit testing is working in Visual Studio Enterprise 

First Sprint: count words between tokens
Second sprint: count lines and characters
Third sprint: replace words (case sensitive and whole words only) 

To run this code, you can execute main.py.  It will print out a few examples then bring up a while true loop that accepts input and spits out statistics.
Enter \q to this prompt to quit. 

NAME
    word_stats

DESCRIPTION
    # Bobb Shields
    # wde677
    #

FUNCTIONS
    check_input(text)
        Global input bounds checker that throws specific errors if failed

        Args:
            text (string): Any given text: A paragraph with symbols, punctuation, numbers, and letters.

        Raises:
            TypeError: Check for string or list
            TypeError: When a list - check elements for whether string
            ValueError: Cannot be empty
            ValueError: Exceding maximum text length

        Returns:
            boolean: Returns true, if no errors were thrown

    count_chars(text, toCase='lower')
        Count of the individual characters of the input text with whitespace removed (space, tab, linefeed, return, formfeed, and vertical tab)

        Args:
            text (string): Any given text: A paragraph with symbols, punctuation, numbers, and letters.
            toCase (str, optional): Transform text to 'upper' or 'lower' case, or stay case 'sensitive'. Defaults to 'lower'.

        Returns:
            integer: Returns the number of non-trivial characters in the text

    count_lines(text)
        Count of the lines: num(newline chars) + 1

        Args:
            text (string): Any given text: A paragraph with symbols, punctuation, numbers, and letters.

        Returns:
            integer: Returns the number of lines in the text

    count_words(text, toCase='lower', tokenizers=['\t', '\n', ' '])
        Count of the individual words.

            Args:
                text (string): Any given text: A paragraph with symbols, punctuation, numbers, and letters.
                toCase (str, optional): Transform text to 'upper' or 'lower' case, or stay case 'sensitive'. Defaults to 'lower'.
                tokenizers (list, optional): User provided list of tokens upon which to split the text. Defaults to ["  ","
        "," "].

            Returns:
                dictionary: The individual words and their counts, sorted from highest to lowest

    print_stats(text)
        Simple helper function to count lines & chars & words

        Args:
            text (string): Any given text: A paragraph with symbols, punctuation, numbers, and letters.

        Returns:
            null: Prints a summary of the three functions.  Used in main.py

    replace_word(text, find, replace)
        # Replace a word within a string.  Uses regular expression to evaluate against the whole word

        Args:
            text (string): Any given text: A paragraph with symbols, punctuation, numbers, and letters.
            find (string): The word or body of text to be replaced
            replace (string): The word or body of text to be substituted in

        Returns:
            string: Original text with keywords replaced

    to_upper_or_lower(validated_text, toCase)
        Transform the text to lower- or uppercase

        Args:
            validated_text (string): Any given text: A paragraph with symbols, punctuation, numbers, and letters. Should already be checked by check_input
            toCase (string): Flags: {'lower', 'upper', 'sensitive'}