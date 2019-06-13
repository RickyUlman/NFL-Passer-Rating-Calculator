# Program:          ch. 2, ex. 2 (2-30)
# Author:           Richard N Barnes iii
# Purpose:          Simple program that calculates passer rating of a player
# Date:             11/04/2018

# init variables
attempts = int(input("please enter the amount of attempts:   "))
c_input = int(input("Please enter the completions:   "))
y_input = int(input("Please enter the yards:   "))
t_input = int(input("Please enter the touchdowns:   "))
i_input = int(input("Please enter the interceptions:   "))

# calculate c, y, t and i
# step 1
c = float(c_input / attempts)
c = float(c - .3)
c = float(c * 5)  
# step 2
y = float(y_input / attempts)
y = float(y - 3)
y = float(y * .25)
# step 3
t = float(t_input / attempts)
t = float(t * 20)
# step 4
i = float(i_input / attempts)
i = float(i * 25)
i = float(2.375 - i)
# step 5
pass_rating = (c + y + t + i)
pass_rating = pass_rating / 6
pass_rating = pass_rating * 100

# print pass rating
print("The passer rating is:  ", pass_rating)
# print rating
if pass_rating <= 85:
    print("This Athlete had a Poor Season")
elif 90 > pass_rating >= 85:
    print("This Athlete had a Mediocre Season")
elif 90 <= pass_rating < 95:
    print("This Athlete had a Good Season")
else:
    print("This Athlete had a Great Season")