#importing  random
import random
#giving a random target of given range
target=random.randint(1,200)
print("TARGET:",target)
sum=0
#user need to guess no of balls to reach target 
balls=int(input("GUESS THE NUMBER OF BALLS TO REACH THE TARGET:"))
ones=0
dots=0
ones=0
twos=0
threes=0
fours=0
sixes=0
#giving the loop for generating the range od "balls"

for i in range(0,balls):
    number=random.choice([0,1,2,3,4,6])    
    sum=sum+number
    if number == 0:
        dots +=1
    elif number == 1:
        ones +=1
    elif number == 2:
        twos +=1
    elif number == 3:
        threes+=1
    elif number == 4:
        fours +=1
    elif number == 6:
        sixes +=1
#displaying score
print("YOUR SCORE IS",sum)
#declaring overs played
a=balls//6
b=balls%6
c,d=str(a),str(b)
print("YOU PLAYED" ,f"{c}.{d}","OVERS")
#displaying the status of match
if sum>target:
    print("YOU WON THE GAME")
elif sum<target:
    print("YOU LOST THE GAME")
    print("YOU LOST THE MATCH BY",target-sum-1,"runs")
elif sum==target:
    print("THE MATCH GOT TIED")
#counting the score per each ball
print("NO OF DOTS",dots)
print("NO OF SINGLES",ones)
print("NO OF TWOS",twos)
print("NO OF THREES",threes)
print("NO OF BOUNDARIES",fours)
print("NO OF SIXES",sixes)
