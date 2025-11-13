word_cat = {"animals" : ["dog", "cat", "tiger", "zebra", "lion",
            "pig", "giraffe", "hamster", "duck", "turtle",
            "fish", "alligator", "bear", "penguin", "bunny",
            "elephant", "squirrel", "cow", "horse", "goat"],
           "fruit" : ["apple", "orange", "strawberry", "banana", "mango",
            "passionfruit", "blueberry", "grape", "pomegranate", "dates",
            "lemon", "lime", "peach", "pear", "pineapple",
            "apricot", "cherry", "fig", "guava", "cantaloupe"],
           "streets" : ["place", "drive", "road", "street", "way",
            "boulevard", "terrace", "expressway", "parkway", "turnpike",
            "avenue", "rechov", "sderot", "broadway", "square",
            "north", "south", "east", "west", "magnolia"]}


import random


def choose_category():
   user_category = input("Choose a category (Animals, Fruit, or Streets): ").lower().strip()
   if user_category == "animals" or user_category == "fruit" or user_category == "streets":
       return user_category
   else:
       print("Please choose a valid category.")
       user_category = input("Choose a category (Animals, Fruit, or Streets): ")
       return user_category


def level_choice():
   while True:
       level = input(("Choose a level: (Easy, Medium, Hard) ")).lower().strip()
       if level == "easy":
           return 10
       elif level == "medium":
           return 8
       elif level == "hard":
           return 6
       else:
           print("Please choose a valid level.")
def word_choice(user_category):


   if user_category in word_cat:
       secret_word = random.choice(word_cat[user_category])
       print("_" * len(secret_word))
       return secret_word
   else:
       print("Please choose a valid category.")
       return None


def guess_letter(secret_word, guessed_letters, display_word):
   letter = input("Guess a letter: ").lower().strip()
   while True:
       if len(letter) != 1 or not letter.isalpha():
           print("Please enter a SINGLE letter.")
           letter = input("Guess a letter: ").lower().strip()
           continue
       if letter in guessed_letters:
           print(f"You already guessed {letter}. Try again.")
           letter = input("Guess a letter: ").lower().strip()
           continue
       break


   guessed_letters.append(letter)
   correct_guess = False
   new_display = ""


   for ch in secret_word:
       if ch == letter or ch in guessed_letters:
           new_display += ch
       else:
           new_display += "_"


   if letter in secret_word:
       correct_guess = True
       print(f"Great Job! You guessed {letter}.")
   else:
       print(f" ")
       print(f"Sorry, {letter} is not in the word.")

   print("Word: "+ " ".join(new_display))


   return new_display, correct_guess


def main():
   print("Welcome to Guess the Word!")
   wins = 0
   losses = 0


   while True:
       tries = level_choice()
       category = choose_category()
       secret_word = word_choice(category)


       guessed_letters = []
       display_word = "_" * len(secret_word)
       word_guessed = False


       print(f"Word:" + "".join(display_word))


       while tries > 0 and not word_guessed:
           print(f"You have {tries} tries left.")
           print(f" ")
           print(f"Guessed Letters: {' '.join(guessed_letters) if guessed_letters else 'None'}")


           display_word, correct = guess_letter(secret_word, guessed_letters, display_word)


           if not correct:
               tries -= 1


           if correct:
               if "_" not in display_word:
                   word_guessed = True
                   print(f"You guessed the word '{secret_word}' correctly. You win!")
                   wins += 1
                   break


       if not word_guessed:
           print(f"Game Over! Try again next time.")
           losses += 1
       else:
           wins += 1


       print(f"Score: {wins} Losses: {losses}")


       while True:
           play_again = input("Would you like to play again? (yes / no): ").lower().strip()
           if play_again == "no":
               print("Thank you for playing! Have a great day!")
               print(" ")
               print(f"Final Score: {wins} Losses: {losses}")
               return
           elif play_again == "yes":
               break
           else:
               print("Please enter 'yes' or 'no.'" )




if __name__ == "__main__":
   main()
