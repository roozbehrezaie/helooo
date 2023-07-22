import random
rand_num = random.randint(1 , 6)
vr=int(input("Enter your number: "))
w=1
while w == 0 :
    if rand_num != vr :
        print("you lost")
        print("Exit the program")
        i = 1
        if rand_num ==vr  :
            print("It is true")
        print("You have another chance")
        rand_num = random.randint(1 , 6)
        num =int( input ("Enter your number : "))