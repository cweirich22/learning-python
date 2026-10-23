import os

def word_count(path):
    with open(path, "r") as f:
        counts = {}
        for line in f:
            words = line.lower().split()
            for word in words:
                counts[word] = counts.get(word, 0) + 1
        return counts

print(word_count("day1-files/sample.txt"))