# Bobb Shields
# wde677
#

# Allows a single call to activate the whole stats suite
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

