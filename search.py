# Open the file in read mode
with open('about.txt', 'r') as file:
  # Read all lines from the file
  lines = file.readlines()

# Initialize a dictionary to store the word counts
word_counts = {}

# Iterate over each line in the file
for line in lines:
  # Split the line into a list of words
  words = line.split()

  # Iterate over each word in the line
  for word in words:
    # If the word has at least 6 letters
    if len(word) >= 6:
      # Increment the count for the word in the dictionary
      if word in word_counts:
        word_counts[word] += 1
      else:
        word_counts[word] = 1

# Find the most frequently used word
most_frequent_word = max(word_counts, key=word_counts.get)

# Print the results
print(f"Words with at least 6 letters: {word_counts}")
print(f"Most frequently used word: {most_frequent_word}")