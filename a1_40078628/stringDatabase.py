class stringDatabase:



    def inputWords(words=[]):
        """
        This method is used to store all 4 letter words from the file to a list
        :param words This is a empty list
        :return: words: This returns the list that contains all the 4 letter words
        """
        with open('four_letters.txt', 'r') as f:
            for line in f:
                for word in line.split():

                    words.append(word)
        return words








