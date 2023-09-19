from french_words import list as word_list
import random
import unicodedata

word, guess = "", []

def generate_word():
  w = word_list[random.randint(0, len(word_list))]
  w = "".join(c for c in unicodedata.normalize("NFD", w) if unicodedata.category(c) != "Mn")
  return w.upper()

def ask_to_play():
  ipt = input("Do you want to play ? (y/n)")
  if ipt in ["y", "n", "d"]:
    return ipt
  return ask_to_play()

def ask_guess():
  ipt = input("Guess a letter or a word: ")
  if ipt.isalpha():
    return ipt.upper()
  
  return ask_guess()

def show_game():
  return " ".join((c if c in guess else "_") for c in word)

while True:
  play = ask_to_play()
  if play == "n":
    break
  
  word = generate_word()
  guess = []
  
  while True:
    if play == "d":
      print(word)
    
    print(show_game())
    
    if len([*filter(lambda x: x in word, guess)]) == len(word):
      print(f"You've won with {len(guess)} guesses!")
      break
    
    ipt = ask_guess()
    
    if ipt in guess:
      print("You've already guessed that")
      continue
    
    guess.append(ipt)
    if len(ipt) > 1:
      if ipt == word:
        print(f"You won with {len(guess)} guesses!")
        break
      print("Wrong!")
      continue