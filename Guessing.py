from random import randint
R_num= randint(1,100)
count = 0
user=int(input("Input a number 1 to 100:"))
count+=1
while R_num!=user:
    if user>R_num:
        print("Too High!")
        user=int(input("Try again! \n Input a number 1 to 100:"))
        count+=1
    elif user<R_num:
        print("Too Low!")
        user=int(input("Try again! \n Input a number 1 to 100:"))
        count+=1
    elif user==R_num:
        break
print("Finally matched.\n You tried ",count," Times","\n AI chosen ",R_num)
        
    