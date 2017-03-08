import collections


counter = collections.Counter()

def count(str):
    words = str.split(" ")
    for word in words:
        counter[word] += 1



def print_counter():
    for word in counter:
        print("word " + word + " occured : " + str(counter[word]))



if __name__ == "__main__":
    text = "this is new this is new"
    count(text)
    print_counter()
