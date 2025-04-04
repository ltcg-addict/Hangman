import pygame # type: ignore
import random
import time
import sys

pygame.init()
pygame.font.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Hangman")

font = pygame.font.Font("font.ttf", 100)

char_eventkey_reference = {
  97: "a",
  98: "b",
  99: "c",
  100: "d",
  101: "e",
  102: "f",
  103: "g",
  104: "h",
  105: "i",
  106: "j",
  107: "k",
  108: "l",
  109: "m",
  110: "n",
  111: "o",
  112: "p",
  113: "q",
  114: "r",
  115: "s",
  116: "t",
  117: "u",
  118: "v",
  119: "w",
  120: "x",
  121: "y",
  122: "z",
}

theme = "anything"#input("Would you like the word to be about anything, programming, animals, or potatoes? ")
words = open(theme + ".txt", "r").readlines()
word = random.choice(words).lower().strip()
live = -1
lives = ["◯", "◯\n|", " ◯\n/|", " ◯\n/|arm", " ◯\n/|arm\n/", " ◯\n/|arm\n/ leg"]
underscores = list("_" * len(word))

underscores_text = font.render("".join(underscores), True, (255, 255, 255))
window.blit(underscores_text, (250 - (underscores_text.get_rect().width / 2), 400))
pygame.display.flip()
pygame.display.update()

p_word = word

while True:
  for event in pygame.event.get():
    if event.type == 256:
      sys.exit(0)
    if event.type == pygame.KEYDOWN:
      try:
        guess = char_eventkey_reference[event.key]
      except KeyError:
        print("Not a letter")
        guess = " "

      if guess in word:
        while guess in word:
          underscores[word.find(guess)] = guess
          underscores_text = font.render("".join(underscores), True, (255, 255, 255))

          word = word.replace(guess, "_", 1)
        print("".join(underscores))
        if word == "_" * len(word):
          print("You win! The word was " + "".join(underscores))
          sys.exit(0)
      else:
        window.fill((255, 0, 0))
        time.sleep(0.75)
        pygame.display.flip()
        live += 1
        print(lives[live])

        if lives[live] == " ◯\n/|arm\n/ leg":
          print("You lose. The word was " + p_word + " and the closest you got was " + "".join(underscores))
          sys.exit(0)

      window.fill((0, 0, 0))
      window.blit(underscores_text, (250 - (underscores_text.get_rect().width / 2), 400))

      pygame.display.update()
      pygame.display.update()

"""while True:
  guess = input("Guess a letter ")
  if guess in word: 
    while guess in word:
      underscores[word.find(guess)] = guess
      word = word.replace(guess, "_", 1)
    print("".join(underscores))
    if word == "_" * len(word):
      print("You win! The word was " + "".join(underscores))
      sys.exit(0)
  else:
    print("Not in word")
    live += 1
    print(lives[live])
    if lives[live] == "◯\n/|arm\n/ leg":
      print("You lose. The word was " + p_word)
      sys.exit(0)"""