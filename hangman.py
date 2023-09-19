from french_words import list as word_list
import random
import unicodedata

word, guess, points = "", [], 0

def generate_word():
  w = word_list[random.randint(0, len(word_list))]
  w = "".join(c for c in unicodedata.normalize("NFD", w) if unicodedata.category(c) != "Mn")
  return w.upper()

def ask_to_play():
  ipt = input("Do you want to play ? (y/n)")
  if ipt in ["y", "n"]:
    return ipt == "y"
  return ask_to_play()

def ask_guess():
  ipt = input("Guess a letter or a word: ")
  if ipt.isalpha():
    return ipt.upper()
  
  return ask_guess()

def show_game():
  return " ".join((c if c in guess else "_") for c in word)

while True:
  if not ask_to_play():
    break
  
  word = generate_word()
  print(word)
  
  while True:
    print(show_game())
    
    print([*filter(lambda x: x in word, guess)])
    
    if len([*filter(lambda x: x in word, guess)]) == len(word):
      print(f"You've won with {points} points!")
      break
    
    ipt = ask_guess()
    
    if ipt in guess:
      print("You've already guessed that")
      continue
    
    guess.append(ipt)
    if len(ipt) > 1:
      if ipt == word:
        print(f"You won with {points} points!")
        break
      points -= 1
      print("Wrong!")
      continue
    
    if ipt not in word:
      points -= 1
      continue