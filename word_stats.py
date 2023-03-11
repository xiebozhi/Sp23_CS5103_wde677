# Bobb Shields
# wde677
#

# Stats for text passed in as the singular parameter
#
#

# Count of the individual words.  
# All characters pushed to lowercase as to make this case insensitive
#
 

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
