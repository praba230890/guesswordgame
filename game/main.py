import random
import collections
from getpass import getpass as get_keyword

class GuessWord(object):
    
    def __init__(self):
        self.word_list = ["jack", "back", "cock", "luck", "bang", "tool", "dogs", "bags", "life", "kick"]
        self.key = True
        self.last_word = []
        self.word = self.grab_word()

    def start_game(self):
        while self.key == True:
            self.star = 0
            self.exc = 0
            self.guess_word_length = 0

            #grabbing the guess word from user and checking the word length
            while self.guess_word_length != len(self.word):
                if self.guess_word_length != 0:
                    print ("Please enter a %d letter word" % len(self.word))
                self.guess_word = input(
                    "Enter your guess that must be containing "+ str(len(self.word)) +" letters: "
                    )
                self.guess_word_length = len(self.guess_word)

            #Exact word match if block
            if self.word == self.guess_word:
                self.new_key = int(input("Congrats! you've got the right word. To continue playing the game please enter 1 and to quit enter 2: \n 1. play \n 2. quit \n"))
                if self.new_key == 1:
                    self.last_word.append(self.word)
                    self.word = self.grab_word()
                    continue
                else:
                    self.star = 0
                    self.exc = 0
                    self.key = False
                    break

            #star calculation
            self.calculate_star()

            #Exclamation calculation
            self.calculate_exclamation()

            #Guess output
            print( ' '.join(['_' for i in range(len(self.word))]) + '\t' + ' '.join(['*' for i in range(self.star)]) + ' '.join([' !' for i in range(self.exc)]))

    def grab_word(self):
        while True:
            word_no = random.randint(0, len(self.word_list)-1)
            word = self.word_list[word_no]
            if word not in self.last_word:
                return word

    def calculate_star(self):
        self.new_word = ""
        self.new_guess_word = ""
        for i, char in enumerate(self.word):
            if self.guess_word[i] == char:
                self.star += 1
                continue
            self.new_word += char
            self.new_guess_word += self.guess_word[i]

    def calculate_exclamation(self):
        new_word_count = dict(collections.Counter(self.new_word))
        new_guess_word_count = dict(collections.Counter(self.new_guess_word))
        for char in new_word_count:
            if char in new_guess_word_count:
                self.exc += min(new_guess_word_count[char], new_word_count[char])


