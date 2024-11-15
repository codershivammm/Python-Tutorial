#Write a program to find out whether a file is identical & matches the content of another file.

with open ("9. File Input And Output/this.txt") as f :
    content1 = f.read()
with open("9. File Input And Output/this_txt_ka_copy.txt") as f:
    content2 = f.read()

if content1 == content2 : print('Both File Contents are same')
else : print("No the contents are not same")