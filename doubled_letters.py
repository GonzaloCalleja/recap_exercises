print("this program checks if all the letters in the word are doubled or doubled."
      " For example aabbggttddiippkkss is doubled.")
word = input("What is the word you are thinking of? ")
if word[::2] == word[1::2]:
    print("All the letters are doubled")
else:
    print("Not all the letters are doubled")


# check if all the letters are tripled

if word[::3] == word[1::3] == word[2::3]:
    print("All the letters are tripled")
else:
    print("Not all the letters are tripled")

