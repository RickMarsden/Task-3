# Create a list to store the 6 letter words
sixLetterWords= []
# Open the file
with open('read.txt') as fin:
    # Read each line
    for line in fin.readlines():
        # Split the line into words
        for word in line.split(" "):
            # Check each word's length
            if len(word) == 6:
                # Add the 6 letter word to the list
                sixLetterWords.append(word)
# Print out the result
print(sixLetterWords)