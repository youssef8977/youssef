from collections import Counter

with open("random_paragraphs.txt", "r") as file:
    text = file.read()

stop_words = ["the", "and", "is", "in", "to", "of", "a", "for", "on", "with", "that", "this"]

words = text.split()

filtered_words = [word for word in words if word.lower() not in stop_words]

filtered_text = ' '.join(filtered_words)

print(filtered_text)

# Count the frequency of each word
word_freq = Counter(filtered_words)

# Print the word frequencies
for word, freq in word_freq.items():
    print(f"{word}: {freq}")