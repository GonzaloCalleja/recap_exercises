from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
punctuation = ",.;:!?"
punctuation2 = ",.;:!?\"'()[]{}-*<>"

# url = "http://wikiroulette.co/"
# url = "https://en.wikipedia.org/wiki/Tyrannosaurus"
# fd = urlopen(url)


fd = open("trex.txt", "r")

longest = ""
size = 0

for line in fd:
    #  line = line.decode()
    for c in punctuation:
        line = line.replace(c, " ")
    words = line.split()
    for word in words:
        if len(word) > size:
            size = len(word)
            longest = word
print("longest words is:", longest)
fd.close()

fd = open("example.txt", "r")
all_words = []
for line in fd:
    #  line = line.decode()
    for c in punctuation2:
        line = line.replace(c, " ")
    words = line.split()
    for word in words:
        if word not in all_words:
            all_words.append(word)
            
all_words.sort()
print("all the words are", all_words)
print("distinct words", len(all_words))
fd.close()

# write a program that counts all the distinct words that appear at least twice in the file

fd = open("example.txt", "r")
every_word = []
repeated = []
for line in fd:
    for c in punctuation2:
        line = line.replace(c, " ")
    words = line.split()
    for word in words:
        if word in every_word and word not in repeated:
            repeated.append(word)
        every_word.append(word)

fd.close()
print(every_word)

print("There are", len(repeated), "repeated words.")

