import pyautogui as pg
import time
import webbrowser

points = 0

# question

answer = pg.prompt(
"""
what's your favorite city?
a) Boston
b) Las Vegas
c) Los Angeles
"""

    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# question

answer = pg.prompt(
"""
who is your favorite player?
a) David Pastrnak
b) James Neal
c) Drew Doughty
"""

    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# question

answer = pg.prompt(
"""
when was the last time the Boston Bruins won the Stanley Cup?
a) 2011
b) 2016
c) 2013
"""

    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3



# question

answer = pg.prompt(
"""
When was the last time the Vegas Golden Knights won the Stanley Cup?
a) 2017
b) Never
c) 2005
"""

    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3



# question

answer = pg.prompt(
"""
When was the last time the Los Angeles Kings won the Stanley Cup?
a) 2017
b) 2012
c) 2014
"""

    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3




# END OF SURVEY


#Boston Bruins
if points < 8:
    pg.alert("You are the Boston Bruins")
    webbrowser.open("https://www.youtube.com/watch?v=glJ82m6O51U")

#Vegas Golden Knights
elif points >= 8 and points < 12:
    pg.alert("You are the Vegas Golden Knights")
    webbrowser.open("https://www.youtube.com/watch?v=UAaXPJSpwBk")

#Los Angeles Kings
elif points >= 12:
    pg.alert("You are the Los Angeles Kings")
    webbrowser.open("https://www.youtube.com/watch?v=2Qoc8vi6kws")
