'''Write a program to read the text from a given file ‘poems.txt’ and find out 
whether it contains the word ‘twinkle’.'''

with open("9. File Input And Output/poems.txt" ,"r") as f :
    content = f.read()
    if "Twinkle" in content:
        print("The word TWINKLE is Present")
    else : print("Sorry No Such Word Present")

