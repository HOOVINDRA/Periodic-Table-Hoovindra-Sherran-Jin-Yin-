import random

def main():
#start a noble gas elemant guessing game.
   print("Hello player! Guess the noble gas elemant from the periodic table.")

#list down options, clues and messages for players if they guess it correct or not
   list = ["Helium","Argon","Neon","Krypton","Xenon","Radon"]
   x = random.choice(list)
   
   if x == "Helium":
       print("Clue: This gas is used too inflate balloons")
   elif x == "Argon":
       print("Clue: In its liquid form, it is often used as the target for neutrino experiments and direct searches for dark matter.")
   elif x == "Neon":
       print("Clue: This gas is used in advertisment signs")
   elif x == "Krypton":
       print("Clue: It is used commercially as a filling gas for energy-saving fluorescent lights. It is also used in some flash lamps used for high-speed photography.")
   elif x == "Xenon":
       print("Clue: Used in car headlights as an alternative to LED headlights")
   elif x == "Radon":
       print("Clue: Used in cell damage and cancer treatments")

   guess = None
   while x != guess:
       
       guess = str(input("Pick a noble gas elemant from the periodic table:"))
       
       if x == guess:
           print("Congratulations! You Guessed it correct!")
       elif x != guess:
           print("Oh no, you got it wrong! Try again!.")
    
main()