"""
Word Occurrences
Estimated time: 30 minutes
Actual time: [To be filled] minutes
"""

text = input("Text: ")

words = text.split()
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

max_word_length = max(len(word) for word in word_counts) if word_counts else 0

for word in sorted(word_counts):
    print(f"{word:{max_word_length}} : {word_counts[word]}")