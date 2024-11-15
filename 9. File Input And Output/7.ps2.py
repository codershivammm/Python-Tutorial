'''Write a program to generate multiplication tables from 2 to 20 and write it to the 
different files. Place these files in a folder for a 13 – year old.'''

def generatetabe(n):
    tabel = ""
    for i in range ( 1, 11):
        tabel += f"{n} X {i} = {n * i}\n"
        

    with open(f"9. File Input And Output/tables/table_{n}.txt" , "w") as f:
        f.write(tabel)

for i in range (2 , 21) :
    generatetabe(i)

