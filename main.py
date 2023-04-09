# Bobb Shields
# wde677
#

# Unit testing code for word statistics functions
# First sprint: count_words
# Second sprint: count_lines, count_chars, check_input, test scenarios
# Third sprint: replace_word, check_input([list])

import word_stats

print("This is a general test of the broadcast system.\n Please return to your homes\n 1234 5678\n")
print(word_stats.print_stats("This is a general test of the broadcast system.\n Please return to your homes\n 1234 5678\n"))

#The FFF THE FFFe three
print("***")
print("Replace Words:\n\"The the THE thee three\" \'the\' - \'FFF\'")
print(word_stats.replace_word("The the THE thee three", "the", "FFF") )
print("***")

#infinite while loop, easily broken out of 
while True:
    input_text = input("Enter text to analyze (or '\q' to exit): ")
    if input_text.lower() == "\q":
        break
    print(word_stats.print_stats(input_text))

