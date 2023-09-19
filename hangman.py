from french_words import list as word_list
import random
import unicodedata

word, guess = "", []

def generate_word():
  w = word_list[random.randint(0, len(word_list))]
  return normalize(w)

def normalize(str):
  return "".join(c for c in unicodedata.normalize("NFD", str) if unicodedata.category(c) != "Mn").upper()

def ask_to_play():
  ipt = input("Do you want to play ? (y/n)")
  if ipt in ["y", "n", "d"]:
    return ipt
  return ask_to_play()

def ask_guess():
  ipt = input("Guess a letter or a word: ")
  if ipt.isalpha():
    return normalize(ipt)
  
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
    
    if not False in [(c in guess) for c in word]:
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