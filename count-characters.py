
map = {}

def count(str):
    words_in_line = str.split(" ")
    for word in words_in_line:
        if word in map:
            count = map[word]
            count = count + 1
            map[word] = count
        else:
            map[word] = 1

def print_map():
    for word in map:
        count = map[word]
        print("word " + str(word) + " count: " + str(count))

if __name__ == "__main__":
    count("this this this can can why can why yes")
    print_map()
