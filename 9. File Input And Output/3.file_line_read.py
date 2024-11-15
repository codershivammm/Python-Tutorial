f= open("9. File Input And Output/file.txt" , "r")

lines = f.readline()
while lines != "" :
    print(lines)
    lines = f.readline()

f.close()
