# Encode a text by replacing each letter with another letter.
# The rule is: current letter is replaced by the letter at the current position + a random number between 1 and 10.
# Example:
#   if the random number is 4: a is replaced with e, e is replaced with i,
#   z is replaced with d (circular after the end of the alphabet)
# You will use the same random generated number
# The English alphabet is: abcdefghijklmnopqrstuvwxyz
# characters that are not letters remain unencoded
import random
seed = random.randint(1, 10)
alphabet = "abcdefghijklmnopqrstuvwxyz"
text = input("What is the text to encode? ")
text = text.lower()
encoded = ""
for c in text:
    pos = alphabet.find(c)
    if pos == -1:
        encoded = encoded + c
        continue
    new_pos = (pos + seed) % 26  # circular addition to account for going over the end of the alphabet
    encoded = encoded + alphabet[new_pos]
print("The encoded text is:", encoded)


# decode the text back to the original value!

decoded = ""
for c in encoded:
    encoded_pos = alphabet.find(c)
    if encoded_pos == -1:
        decoded = decoded + c
        continue
    old_pos = (encoded_pos - seed) % 26
    decoded = decoded + alphabet[old_pos]
print("The decoded text is:", decoded)
