import random

class GuessWord(object):
    
    def __init__(self):
        self.word_list = ["jack", "back", "cock", "luck", "bang", "tool", "dogs", "bags", "life", "kick"]
        # todo: should move some attributes from __init__ to start_game method (word, key & lastword)

    def start_game(self):
        self.word = ""
        self.key = True
        self.last_word = []
        while self.key == True:
            self.star = 0
            self.exc = 0
            self.tmp_word_length = 0
            self.same = []
            self.diff = []

            #checking and grabbing the game word
            if self.word == "":
                self.word = self.grab_word()

            #grabbing the guess word and checking the word length
            while self.tmp_word_length != len(self.word):
                self.tmp_word = raw_input("Enter your guess that must be containing "+ str(len(self.word)) +" letters: ")
                self.tmp_word_length = len(self.tmp_word)

            #Exact word match if block
            if self.word == self.tmp_word:
                self.new_key = int(raw_input("Congrats! you've got the right word. To continue playing the game please enter 1 and to quit enter 2: \n 1. play \n 2. quit \n"))
                if self.new_key == 1:
                    self.last_word.append(self.word)
                    self.word = ""
                else:
                    self.star = 0
                    self.exc = 0
                    self.key = False
                    break

            #star calculation
            self.calculate_star()

            #Exclamation calculation
            for i in range(len(self.word)):
                for j in range(len(self.tmp_word)):
                    if i != j and self.tmp_word[i] == self.word[j] and self.tmp_word[i] not in self.same and self.tmp_word[i] not in self.diff:
                                self.same.append(self.tmp_word[i])
                                self.exc +=1
            #Guess output
            print ' '.join(['_' for i in range(len(self.word))]) + '\t' + ' '.join(['*' for i in range(self.star)]) + ' '.join([' !' for i in range(self.exc)])
    def grab_word(self):
        while True:
            word_no = random.randint(0,len(self.word_list)-1)
            word = self.word_list[word_no]
            if word in self.last_word:
                pass
            else:
                break
        return word

    def calculate_star(self):
        for i in range(len(self.word)):
            if self.tmp_word[i] == self.word[i]:
                self.same.append(self.tmp_word[i])
                self.star += 1
