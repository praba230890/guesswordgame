import random

class GuessWord(object):
    
    def __init__(self):
        word = ""
        wordlist = ["jack", "back", "cock", "luck", "bang", "tool", "dogs", "bags", "life", "kick"]
        key = True
        lastword = []

    def start_game(self):
        while key == True:
            star = 0
            exc = 0
            tmpwordlength = 0
            same = []
            #checking and grabbing the game word
            if word == "":
                while True:
                    wordno = random.randint(0,len(wordlist)-1)
                    word = wordlist[wordno]
                    if word in lastword:
                        pass
                    else:
                        break
            #grabbing the guess word and checking the word length
            while tmpwordlength != len(word):
                tmpword = raw_input("Enter your guess that must be containing "+ str(len(word)) +" letters: ")
                tmpwordlength = len(tmpword)
            #Exact word match if block
            if word == tmpword:
                newkey = int(raw_input("Congrads you've got the right word. To continue playing the game please enter 1 and to quit enter 2: \n 1. play \n 2. quit \n"))
                if newkey == 1:
                    lastword.append(word)
                    word = ""
                else:
                    star = 0
                    exc = 0
                    key = False
                    break
            #star calculation
            for i in range(len(word)):
                if tmpword[i] == word[i]:
                    same.append(tmpword[i])
                    star += 1
            #Exclamation calculation
            for i in range(len(word)):
                for j in range(len(tmpword)):
                    if i != j and tmpword[i] == word[j] and tmpword[i] not in same:
                                exc +=1
            #Guess output
            print ' '.join(['_' for i in range(len(word))]) + '\t' + ' '.join(['*' for i in range(star)]) + ' '.join([' !' for i in range(exc)])
      

