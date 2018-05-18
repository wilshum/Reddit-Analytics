import matplotlib.pyplot as plt
import csv
from collections import defaultdict
import collections

columns = defaultdict(list)

with open('data.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        for i in range(len(row)):
            columns[i].append(row[i])
    columns = dict(columns)

print(columns)

allWords = []

for comment in columns[1]:
    words = comment.split()
    for word in words:
        allWords.append(word)
        # print(word)

allWords = map(str.lower, allWords)

counter = collections.Counter(allWords)
print(counter)
print(counter.keys())
print(counter.values())

x = list(counter.keys())[0:10]
y = list(counter.values())[0:10]
plt.title("Top 10 Words vs #times used")
plt.xlabel("words")
plt.ylabel("#times")
plt.bar(x, y)

plt.show()
