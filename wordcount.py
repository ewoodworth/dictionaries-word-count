# put your code here.
def word_count(path):
    """Takes a text file and returns nothing
    Takes a text file from the directory and counts the occurances of each word inside.
    Print the words and their counts nicely.
    """
    input_text = open(path)
    word_counts = {}
    for line in input_text:
        line = line.rstrip()
        line = line.split(" ")
        for word in line:
            word_counts[word] = word_counts.get(word, 0) + 1

    input_text.close()

    for word, count in word_counts.items():
        print "%s %s" % (word, count)

word_count("test.txt")






def word_count_generated(path):
    """
    Takes a text file and returns nothing
    Takes a text file from the directory and counts the occurances of each word inside.
    Print the words and their counts nicely. 

    Uses iteritems to accommodate longer input file.
    """
    input_text = open(path)
    word_counts = {}
    for line in input_text:
        line = line.rstrip()
        line = line.split(" ")
        for word in line:
            word_counts[word] = word_counts.get(word, 0) + 1

    input_text.close()

    # return word_counts
    for word, count in word_counts.iteritems():
        print "%s %s" % (word, count)


print word_count_generated("twain.txt")
