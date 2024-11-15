def gd(name , ending):
    print(f"GoodDay {name} !")
    print(ending)
    return "OK"

a = gd("Shivam" , 'Thank You !\n')

#The return Value "OK" will only show Up when You Print the variable in which You assigned functioon call
a = gd("Shivam" , 'Thank You !')
print(a)