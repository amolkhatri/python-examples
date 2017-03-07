import sys

map = {}

for line in sys.stdin:
    words_in_line = line.split(" ")
    for word in words_in_line:
        if word in map:
            counter = map[word]
            counter += 1
            map[word] = counter
        else:
            counter = 1
            map[word] = counter


for word in map:
    print str(word) + " occured " + str(map[word])
