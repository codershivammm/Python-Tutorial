marks= {
    "Shivam" : 88,
    "Rohan": 78,
    "rahul" : 38,
    "ritik": 79
}
print(marks.keys())
print(marks.values())
print(marks.items())
marks.update({"Shivam" : 98, "soumya" : 88})
print(marks)

print(marks.get("Shivam"))
#or
print(marks["Shivam"])