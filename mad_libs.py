import random

#Note from developer, this is work in progress
adjectives = ['beautiful', 'awful', 'strange', 'mysterious', 'hot', 'funny']
activities = ['jog', 'swim', 'play chess', 'read', 'write']

print("Let's play some mad libs!")
getAdjPosition = random.randrange(len(adjectives))
getAdjective = adjectives[getAdjPosition]
print("It was a ", getAdjective, "day like any other." )
getActPosition = random.randrange(len(activities)) 
getActivity = activities[getActPosition]
print("Joe decided that it was a day for ",getActivity)
getActPosition = random.randrange(len(activities)) 
getActivity = activities[getActPosition]
print("And afterwards, he would ", getActivity)