#Repeat ps3 for a list of such words to be censored.

words = ["donkey" , "ganda" ,"shit" , "fuck"]

with open("9. File Input And Output/list_bad_remove.txt" , "r") as f:
    content = f.read()

    for word in words :
        content = content.replace(word ,  "#" * len(word))

with open("9. File Input And Output/list_bad_remove.txt" , "w") as f:
    f.write(content)
