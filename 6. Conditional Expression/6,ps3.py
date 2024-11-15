'''A spam comment is defined as a text containing following keywords: 
“ money”, “buy”, “subscribe”. Write a program 
to detect these spams'''

p1 = " money"
p2 = "buy "  
p3 = "subscribe "  


message = input("Enter your comment: ")

if(( message in p1) or ( message in p2 )or ( message in p3)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")