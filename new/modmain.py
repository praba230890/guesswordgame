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
            star = 0
            exc = 0
            tmp_word_length = 0
            same = []
            #checking and grabbing the game word
            if self.word == "":
                while True:
                    word_no = random.randint(0,len(self.word_list)-1)
                    self.word = self.word_list[word_no]
                    if self.word in self.last_word:
                        pass
                    else:
                        break
            #grabbing the guess word and checking the word length
            while tmp_word_length != len(self.word):
                tmp_word = raw_input("Enter your guess that must be containing "+ str(len(self.word)) +" letters: ")
                tmp_word_length = len(tmp_word)
            #Exact word match if block
            if self.word == tmp_word:
                new_key = int(raw_input("Congrats! you've got the right word. To continue playing the game please enter 1 and to quit enter 2: \n 1. play \n 2. quit \n"))
                if new_key == 1:
                    self.last_word.append(self.word)
                    self.word = ""
                else:
                    star = 0
                    exc = 0
                    self.key = False
                    break
            #star calculation
            for i in range(len(self.word)):
                if tmp_word[i] == self.word[i]:
                    same.append(tmp_word[i])
                    star += 1
            #Exclamation calculation
            for i in range(len(self.word)):
                for j in range(len(tmp_word)):
                    if i != j and tmp_word[i] == self.word[j] and tmp_word[i] not in same:
                                exc +=1
            #Guess output
            print ' '.join(['_' for i in range(len(self.word))]) + '\t' + ' '.join(['*' for i in range(star)]) + ' '.join([' !' for i in range(exc)])

