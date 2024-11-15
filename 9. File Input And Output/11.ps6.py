#Write a program to make a copy of a text file “this. txt”

with open("9. File Input And Output/this.txt") as f:
    content = f.read()

with open("9. File Input And Output/this_txt_ka_copy.txt" , "w") as f :
    f.write(content)