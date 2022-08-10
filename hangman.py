import sys
import random
import os

# Read in word list
with open('word_list.txt') as f:
    words = f.read().splitlines()  # readlines() adds \n


class Hangman:
    """Class to manage and run instance of a game"""

    def __init__(self):
        """Initialse resources"""
        self.words = words
        self.word = random.choice(self.words)
        self.words.remove(self.word)  # Remove word so its not selected again
        self.word = self.word.upper()
        self.guesses = []
        self.livesUsed = 0
        self.gameOver = False
        self.displayString = []
        for c in range(len(self.word)):
            self.displayString.append('*')
        self.updateDisplay(8)

    def runGame(self):
        """Star and run the game instance in a loop"""

        while self.gameOver == False:

            guess = input("Please enter your next guess: ")

            if self.verifyInput(guess):
                self.checkWord(guess.upper())
                self.updateDisplay(self.livesUsed)

            self.checkGameOver()

    def verifyInput(self, guess):
        """Ensure user input is valid"""
        if guess == "quit":
            sys.exit()

        if len(guess) != 1:
            print("Please only enter 1 character at a time or type 'quit' to quit")
            print("Your word is: " + ''.join(self.displayString))
        else:
            if guess.isalpha():
                if guess.upper() in self.guesses:
                    print(f"You have alread guesses {guess.upper()}, please try again")
                    print("Your word is: " + ''.join(self.displayString))
                    return False
                else:
                    return True
            else:
                print("You may only enter alphabetical characters, please try again or type 'quit' to exit")
                print("Your word is: " + ''.join(self.displayString))
                return False

    def checkWord(self, guess):
        """Check and update word"""
        if guess in self.word:
            self.updateDisplayString(guess)
        else:
            self.livesUsed += 1

        self.guesses.append(guess)

    def updateDisplayString(self, guess):
        """Update the value if the display string"""
        for i, char in enumerate(self.word):
            if char == guess:
                self.displayString[i] = char

    def checkGameOver(self):
        """Check if game has ended"""
        if self.livesUsed == 7:
            print(f"The answer was {self.word}")
            self.gameOver = True
            print("You Lose")

        if ('*' in self.displayString) == False:
            print("Congratualtions you win")
            self.gameOver = True

    def updateDisplay(self, i):
        """Clear and update the console screen"""

        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen

        art = (
            f"""
            ----------
            |/
            |
            |
            |
            |
            |
            |===========
    """,
            f"""
    ----------
     |/     |
     |
     |
     |
     |
     |
     |==H========
    """,
            f"""
    ----------
     |/     |
     |     (_)
     |
     |
     |
     |
     |==HA=======
    """,
            f"""
    ----------
     |/     |
     |     (_)
     |      |
     |      |
     |
     |
     |==HAN======
    """,
            f"""
    ----------
     |/     |
     |     (_)
     |     /|
     |      |
     |
     |
     |==HANG=====
    """,
            f"""
    ----------
     |/     |
     |     (_)
     |     /|\\
     |      |
     |
     |
     |==HANGM====
    """,
            f"""
    ----------
     |/     |
     |     (_)
     |     /|\\
     |      |
     |     /
     |
     |==HANGMA===
    """,
            f"""
    ----------
     |/     |
     |     (_)
     |     /|\\
     |      |
     |     / \\
     |
     |==HANGMAN==

    """,
            f"""
    =============================
         WELCOME TO HANGMAN!
    =============================
            ----------
            |/     |
            |     (_)
            |     /|\\
            |      |
            |     / \\
            |
            |==HANGMAN==
    ==============================
      HERE IS YOUR FIRST WORD...
    ==============================
    """

        )
        if i == 8:
            print(art[i])
            print(f"Your {len(self.word)} letter word is: " +
                  ''.join(self.displayString))
        else:
            #print details
            print(art[i])

            print("Your guesses have been: " +
                  ','.join(self.guesses))

            print("Your word is: " +
                  ''.join(self.displayString))


if __name__ == '__main__':
    # Make instance of game and run it
    hm = Hangman()
    hm.runGame()
