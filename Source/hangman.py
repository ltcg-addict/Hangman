import sys
import random

theme = input("Would you like the word to be about anything, programming, animals, or potatoes? ")
words = open(theme + ".txt", "r").readlines()
word = random.choice(words).lower().strip()
live = -1
lives = ["◯", "◯\n|", "◯\n/|", "◯\n/|arm", "◯\n/|arm\n/", "◯\n/|arm\n/ leg"]
underscores = list("_" * len(word))
p_word = word

while True:
  guess = input("Guess a letter ")
  if guess in word: 
    while guess in word:
      underscores[word.find(guess)] = guess
      word = word.replace(guess, "_", 1)
    print("".join(underscores))
    if word == "_" * len(word):
      print("You win! The word was " + "".join(underscores))
      sys.exit(1)
  else:
    print("Not in word")
    live += 1
    print(lives[live])
    if lives[live] == "◯\n/|arm\n/ leg":
      print("You lose. The word was " + p_word)
      sys.exit(0)