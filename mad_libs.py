import requests
import random

#Note from developer, this is work in progress
word_generator = "https://www.randomlists.com/random-words?dup=false&qty=100"
res = requests.get(word_generator)
getWords = res.content.splitlines()

print("Let's play some mad libs!")
word = random.choice(getWords)
print("It was a ", word, "day like any other." )
nextWord = random.choice(getWords) 
print("Joe decided that it was a day for ", nextWord)