f = open("9. File Input And Output/file.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("9. File Input And Output/file.txt") as f:
    print(f.read())

# You dont have to explicitly close the file