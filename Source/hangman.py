import pygame # type: ignore
import random
import time
import sys
from gtts import gTTS as tts
from playsound import playsound

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

theme = "anything"
words = open(theme + ".txt", "r").readlines()
word = random.choice(words).lower().strip()
live = -1
underscores = list("_" * len(word))

window.fill((255, 255, 255))
underscores_text = font.render("".join(underscores), True, (0, 0, 0))
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
        guess = " "

      if guess in word:
        while guess in word:
          underscores[word.find(guess)] = guess
          underscores_text = font.render("".join(underscores), True, (0, 0, 0))

          word = word.replace(guess, "_", 1)
        if word == "_" * len(word):
          sys.exit(0)
      else:
        window.fill((255, 0, 0))
        time.sleep(0.75)
        pygame.display.flip()
        live += 1
        lives_image = pygame.image.load(str(live) + ".png")
        lives_image = pygame.transform.scale(lives_image, (300, 300))

        if live == 7:
          speech = tts(text=p_word, lang="en", slow=False)
          speech.save("ai_word.mp3")
          playsound("ai_word.mp3")
          time.sleep(1.25)
          sys.exit(0)

      window.fill((255, 255, 255))
      window.blit(underscores_text, (250 - (underscores_text.get_rect().width / 2), 400))
      window.blit(lives_image, (250 - (lives_image.get_rect().width / 2), 100))

    pygame.display.update()
    pygame.display.update()

"""while True:
  guess = input("Guess a letter ")
  if guess in word: 
    while guess in word:
      underscores[word.find(guess)] = guess
      word = word.replace(guess, "_", 1)
    ("".join(underscores))
    if word == "_" * len(word):
      ("You win! The word was " + "".join(underscores))
      sys.exit(0)
  else:
    ("Not in word")
    live += 1
    (lives[live])
    if lives[live] == "◯\n/|arm\n/ leg":
      ("You lose. The word was " + p_word)
      sys.exit(0)"""