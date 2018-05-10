import math

newsSets = []
allWords = set()
for line in open("seg.txt", encoding="utf8"):
    words = set(line.split(" "))
    newsSets.append(words)
    allWords = words | allWords
docs = len(newsSets)
idf = {}
for word in allWords:
    wordCount = 0
    for newsSet in newsSets:
        if word in newsSet:
            wordCount += 1
    idf[word] = math.log(docs / wordCount + 1)

pass
