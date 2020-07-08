from stringDatabase import stringDatabase
from game import game
import random
class guess():
    """This class contains all the major operations of this Game """
    gameInfo = {}
    words = []
    guessWord = ''
    g = "----"
    gameNo = 1
    bg = 0
    ml = 4
    score = 0
    nl=0
    status = "Gave up"



    def main(self):
        """This is the main Function
        :param self: This is the current object
        """

        self.initialise()



    def initialise(self):
        """
        This is used to initialise all the global variables and it calls the code from StringDatabase class to store all 4-lettered words into a list
        :param self: This is the current object
        """
        global guessWord, words,g, ml, bg, score, status, gameNo,gameInfo,scoreDict,nl
        gameInfo = {}
        words = []
        guessWord = ''
        g = "----"
        gameNo = 1
        bg = 0
        ml = 4
        nl=0
        score = 0
        status = "Gave up"
        scoreDict = {'a': 4.83, 'b': 11.51, 'c': 10.22, 'd': 8.75, 'e': 0.3, 'f': 10.77, 'g': 10.98, 'h': 6.91,
                     'i': 6.03, 'j': 12.85, 'k': 12.23, 'l': 8.97, 'm': 10.59, 'n': 6.25, 'o': 5.49, 'p': 11.07,
                     'q': 12.90, 'r': 7.01, 's': 6.67, 't': 3.94, 'u': 10.24, 'v': 12.09, 'w': 10.64, 'x': 12.85,
                     'y': 11.03, 'z': 12.93}

        words = stringDatabase.inputWords()
        guessWord = words[random.randint(0, 4030)]
        score= (scoreDict.get(guessWord[0])+ scoreDict.get(guessWord[1]) + scoreDict.get(guessWord[2])+ scoreDict.get(guessWord[3]))
        self.guessGame()




    def guessGame(self):
        """
        This functions contains the main menu of the game and asks the input from the user and accordingly sends the control to the required module
        :param self: This is the current object
        """

        global guessWord, g, ml, bg, score, status, gameNo,gameInfo,nl


        print()
        print("** The great guessing game **")
        print()
        print("Current Guess: ",g)


        print()
        x = input("g= guess, t = tell me, l for a letter, and q to quit")
        if x == 'g':
            a = input("Enter your guess")
            self.Guess(a)
        elif x == 't':
            self.Tellme()
        elif x =='l':
            nl=nl+1
            a = input("Enter a letter")

            self.Letter(a)
        elif x =='q':
          game.printGame(gameInfo)
        else:
            print("Please select from the given options")
            self.guessGame()




    def Guess(self,a):
        """
        This is the module used when the user wants to guess the word. If he is able to correctly guess the word, all info about this game is stored and a new word is generated and the game continues
        :param a: This contains the guess entered by the user
        :param self: This is the current object
        """

        global guessWord, g, ml, bg, score, status, gameNo,gameInfo,nl,scoreDict
        if a == guessWord:
            status ="Success"
            print("Congrats, You have guessed correctly")
            print("A new word has been selected.")
            if nl>0:
                score = (score/nl)
            gameInfo = game.saveGame(gameInfo,gameNo, guessWord, status, bg, ml, score)
            guessWord = words[random.randint(0, 4030)]
            gameNo = gameNo + 1
            g = "----"
            status = "Gave up"
            ml = 4
            bg = 0
            nl=0
            score = (scoreDict.get(guessWord[0]) + scoreDict.get(guessWord[1]) + scoreDict.get(
                guessWord[2]) + scoreDict.get(guessWord[3]))
            self.guessGame()


        else:
            print("you have guessed incorrectly")
            score = (score - (score*0.25))
            bg=bg+1
            self.guessGame()


    def Letter(self,a):
        """
        This method is called when the user wants to guess a single character in the word
        :param a: This is the letter entered by the user
        :param self: This is the current object
        """
        global guessWord, g, ml, bg, score, status, gameNo,gameInfo,nl,scoreDict
        if guessWord[0] == a :
            if g[0] == '-':
                g = guessWord[0] + g[1:4]
                score = score - scoreDict.get(guessWord[0])
                ml=ml-1
        if guessWord[1] == a:
            if g[1] == '-':
                score = score - scoreDict.get(guessWord[1])
                g = g[0] + guessWord[1] + g[2:4]
                ml = ml - 1
        if guessWord[2] == a:
            if g[2] == '-':
                score = score - scoreDict.get(guessWord[2])
                g = g[0:2] + guessWord[2] + g[3]
                ml = ml - 1
        if guessWord[3] == a:
            if g[3] == '-':
                score = score - scoreDict.get(guessWord[3])
                g = g[0:3] + guessWord[3]
                ml = ml - 1

        if ml>0:
            self.guessGame()
        else:
            status = "Success"
            print("Congrats, You have guessed correctly")
            print("A new word has been selected.")
            score = (score / nl)
            gameInfo = game.saveGame(gameInfo, gameNo, guessWord, status, bg, ml, score)
            guessWord = words[random.randint(0, 4030)]
            gameNo = gameNo + 1
            g = "----"
            status = "Gave up"
            ml = 4
            bg = 0
            nl = 0
            score = (scoreDict.get(guessWord[0]) + scoreDict.get(guessWord[1]) + scoreDict.get(
                guessWord[2]) + scoreDict.get(guessWord[3]))
            self.guessGame()


    def Tellme(self):
        """
        This is used when user gives up and wants to know which word it is.
        This then saves the information related to this word and generates a new random word and the game continues
        """

        global guessWord, g, ml, bg, score, status, gameNo, gameInfo, nl
        print("The correct word was :" ),
        print(guessWord)
        print("A new word has been selected.")
        score = -score
        gameInfo = game.saveGame(gameInfo, gameNo, guessWord, status, bg, ml, score)
        gameNo = gameNo + 1
        g = "----"
        ml = 4
        bg = 0
        nl=0
        score= (scoreDict.get(guessWord[0])+ scoreDict.get(guessWord[1]) + scoreDict.get(guessWord[2])+ scoreDict.get(guessWord[3]))

        status = "Gave up"
        guessWord = words[random.randint(0, 4030)]
        self.guessGame()




game11 = guess()
game11.main()