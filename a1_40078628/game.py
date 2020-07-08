class game:


    def saveGame(gameInfo, gameNo, word, status, bg, ml, score):
        """
        This method is used to save the information about the game relating to a certain word
        :param gameNo: This represents the word number that user is trying to guess
        :param word: This contains the word itself
        :param status: This states whether user was able to guess the word or not
        :param bg: This represents number of bad guesses given by the user
        :param ml: This represents the no of letters were yet to be revealed at the time of a correct guess or when user gave up
        :param score: This reveals score of the user corresponding to that word
        :return gameInfo: It returns the updated dictionary
        """
        gameInfo
        info=gameNo, word, status, bg, ml, score
        tempDict={gameNo:info}
        gameInfo.update(tempDict)
        return gameInfo

    def printGame(gameInfo):
        """
        This is used to print information about all the games that user has played
        This also presents the final score of the user
        :param gameInfo This is the dictionary that contains about all the information about games played by the user

        """
        print()
        print("Game      Word      Status      Bad Guesses      Missed Letters      Score")
        print()
        print("----      ----      ------      -----------      --------------      -----")
        print()

        totalscore=0
        for x in gameInfo.values():
            a, b, c, d, e, f = x
            totalscore=totalscore+f
            print(a, "       ", b, "    ", c, "        ", d, "               ", e, "            ", f)
            print()

        print()
        print("Final Score" , totalscore)






