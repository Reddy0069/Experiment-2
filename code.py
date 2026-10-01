# Player A
scoreA = 135
ballsA = 48
wicketA = 3
concededA = 27
overA = 2
catchA = 2

rateA = (scoreA / ballsA) * 100
runrateA = concededA / overA

print("PLAYER A")
print("Batting Rate:", rateA)
print("Bowling Rate:", runrateA)

# Fielding Assessment
if catchA >= 2:
    fieldA = "Outstanding Fielder"
elif catchA == 1:
    fieldA = "Active Fielder"
else:
    fieldA = "Needs Improvement"

# Bowling Assessment
if wicketA >= 3 and runrateA <= 6:
    bowlA = "Excellent Bowler"
elif wicketA >= 2 and runrateA <= 8:
    bowlA = "Good Bowler"
elif wicketA >= 1:
    bowlA = "Average Bowler"
else:
    bowlA = "Poor Bowler"

# Batting Assessment
if scoreA >= 50 and rateA >= 120:
    batA = "Excellent Batter"
elif scoreA >= 30 and rateA >= 100:
    batA = "Good Batter"
elif scoreA >= 20:
    batA = "Average Batter"
else:
    batA = "Poor Batter"

if batA == "Excellent Batter" and bowlA == "Excellent Bowler":
    resultA = "Star All-Rounder"
elif batA == "Good Batter" and bowlA == "Good Bowler":
    resultA = "Strong All-Rounder"
elif batA == "Good Batter" or bowlA == "Good Bowler":
    resultA = "Supporting All-Rounder"
else:
    resultA = "Needs Improvement"

print("Batting:", batA)
print("Bowling:", bowlA)
print("Fielding:", fieldA)
print("Overall:", resultA)
print()


# Player B
scoreB = 165
ballsB = 58
wicketB = 5
concededB = 30
overB = 3
catchB = 1

rateB = (scoreB / ballsB) * 100
runrateB = concededB / overB

print("PLAYER B")
print("Batting Rate:", rateB)
print("Bowling Rate:", runrateB)

# Bowling Assessment
if wicketB >= 3 and runrateB <= 6:
    bowlB = "Excellent Bowler"
elif wicketB >= 2 and runrateB <= 8:
    bowlB = "Good Bowler"
elif wicketB >= 1:
    bowlB = "Average Bowler"
else:
    bowlB = "Poor Bowler"

# Fielding Assessment
if catchB >= 2:
    fieldB = "Outstanding Fielder"
elif catchB == 1:
    fieldB = "Active Fielder"
else:
    fieldB = "Needs Improvement"

# Batting Assessment
if scoreB >= 50 and rateB >= 120:
    batB = "Excellent Batter"
elif scoreB >= 30 and rateB >= 100:
    batB = "Good Batter"
elif scoreB >= 20:
    batB = "Average Batter"
else:
    batB = "Poor Batter"

if batB == "Excellent Batter" and bowlB == "Excellent Bowler":
    resultB = "Star All-Rounder"
elif batB == "Good Batter" and bowlB == "Good Bowler":
    resultB = "Strong All-Rounder"
elif batB == "Good Batter" or bowlB == "Good Bowler":
    resultB = "Supporting All-Rounder"
else:
    resultB = "Needs Improvement"

print("Batting:", batB)
print("Bowling:", bowlB)
print("Fielding:", fieldB)
print("Overall:", resultB)
print()


# Player C
scoreC = 142
ballsC = 55
wicketC = 7
concededC = 34
overC = 4
catchC = 3

rateC = (scoreC / ballsC) * 100
runrateC = concededC / overC

print("PLAYER C")
print("Batting Rate:", rateC)
print("Bowling Rate:", runrateC)

# Batting Assessment
if scoreC >= 50 and rateC >= 120:
    batC = "Excellent Batter"
elif scoreC >= 30 and rateC >= 100:
    batC = "Good Batter"
elif scoreC >= 20:
    batC = "Average Batter"
else:
    batC = "Poor Batter"

# Fielding Assessment
if catchC >= 2:
    fieldC = "Outstanding Fielder"
elif catchC == 1:
    fieldC = "Active Fielder"
else:
    fieldC = "Needs Improvement"

# Bowling Assessment
if wicketC >= 3 and runrateC <= 6:
    bowlC = "Excellent Bowler"
elif wicketC >= 2 and runrateC <= 8:
    bowlC = "Good Bowler"
elif wicketC >= 1:
    bowlC = "Average Bowler"
else:
    bowlC = "Poor Bowler"

if batC == "Excellent Batter" and bowlC == "Excellent Bowler":
    resultC = "Star All-Rounder"
elif batC == "Good Batter" and bowlC == "Good Bowler":
    resultC = "Strong All-Rounder"
elif batC == "Good Batter" or bowlC == "Good Bowler":
    resultC = "Supporting All-Rounder"
else:
    resultC = "Needs Improvement"

print("Batting:", batC)
print("Bowling:", bowlC)
print("Fielding:", fieldC)
print("Overall:", resultC)
print()


# Player D
scoreD = 108
ballsD = 43
wicketD = 2
concededD = 25
overD = 3
catchD = 0

rateD = (scoreD / ballsD) * 100
runrateD = concededD / overD

print("PLAYER D")
print("Batting Rate:", rateD)
print("Bowling Rate:", runrateD)

# Fielding Assessment
if catchD >= 2:
    fieldD = "Outstanding Fielder"
elif catchD == 1:
    fieldD = "Active Fielder"
else:
    fieldD = "Needs Improvement"

# Batting Assessment
if scoreD >= 50 and rateD >= 120:
    batD = "Excellent Batter"
elif scoreD >= 30 and rateD >= 100:
    batD = "Good Batter"
elif scoreD >= 20:
    batD = "Average Batter"
else:
    batD = "Poor Batter"

# Bowling Assessment
if wicketD >= 3 and runrateD <= 6:
    bowlD = "Excellent Bowler"
elif wicketD >= 2 and runrateD <= 8:
    bowlD = "Good Bowler"
elif wicketD >= 1:
    bowlD = "Average Bowler"
else:
    bowlD = "Poor Bowler"

if batD == "Excellent Batter" and bowlD == "Excellent Bowler":
    resultD = "Star All-Rounder"
elif batD == "Good Batter" and bowlD == "Good Bowler":
    resultD = "Strong All-Rounder"
elif batD == "Good Batter" or bowlD == "Good Bowler":
    resultD = "Supporting All-Rounder"
else:
    resultD = "Needs Improvement"

print("Batting:", batD)
print("Bowling:", bowlD)
print("Fielding:", fieldD)
print("Overall:", resultD)
