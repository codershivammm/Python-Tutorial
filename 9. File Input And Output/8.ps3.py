'''A file contains a word “Donkey” multiple times. You need to write a program 
which replace this word with ##### by updating the same file. '''

word = "donkey"

with open("9. File Input And Output/donkey.txt", "r") as f:
    content = f.read()
    contentnew = content.replace(word, "####")

with open ("9. File Input And Output/donkey.txt" , "w") as  f:
    f.write(contentnew)

f.close()
