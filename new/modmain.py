import random

class GuessWord(object):
    
    def __init__(self):
        self.wordlist = ["jack", "back", "cock", "luck", "bang", "tool", "dogs", "bags", "life", "kick"]
	# todo: should move some attributes from __init__ to start_game method (word, key & lastword)

    def start_game(self):
        self.word = ""
        self.key = True
        self.lastword = []
        while self.key == True:
            star = 0
            exc = 0
            tmpwordlength = 0
            same = []
            #checking and grabbing the game word
            if self.word == "":
                while True:
                    wordno = random.randint(0,len(self.wordlist)-1)
                    self.word = self.wordlist[wordno]
                    if self.word in self.lastword:
                        pass
                    else:
                        break
            #grabbing the guess word and checking the word length
            while tmpwordlength != len(self.word):
                tmpword = raw_input("Enter your guess that must be containing "+ str(len(self.word)) +" letters: ")
                tmpwordlength = len(tmpword)
            #Exact word match if block
            if self.word == tmpword:
                newkey = int(raw_input("Congrads you've got the right word. To continue playing the game please enter 1 and to quit enter 2: \n 1. play \n 2. quit \n"))
                if newkey == 1:
                    self.lastword.append(self.word)
                    self.word = ""
                else:
                    star = 0
                    exc = 0
                    self.key = False
                    break
            #star calculation
            for i in range(len(self.word)):
                if tmpword[i] == self.word[i]:
                    same.append(tmpword[i])
                    star += 1
            #Exclamation calculation
            for i in range(len(self.word)):
                for j in range(len(tmpword)):
                    if i != j and tmpword[i] == self.word[j] and tmpword[i] not in same:
                                exc +=1
            #Guess output
            print ' '.join(['_' for i in range(len(self.word))]) + '\t' + ' '.join(['*' for i in range(star)]) + ' '.join([' !' for i in range(exc)])
      

