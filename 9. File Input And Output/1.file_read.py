'''Python has an open() function for opening files. It takes 2 parameters:  filename and 
mode. 
# open("filename", "mode of opening(read mode by default)") 
open("this.txt", "r")''' 

f = open("9. File Input And Output/file.txt", "r")
data = f.read()
print(data)
f.close()