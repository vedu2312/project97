number = 7 
counter = 5
print("enter a number between 1 to 10")
while counter>0:
    guess=int(input("enter your number: "))
    if guess==number:
        print("you win")
        break
    elif guess<number:
        print("your number is greater")
    else:
        print("your number is less")    
    counter-=1
    
