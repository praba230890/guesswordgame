import random
import collections
from getpass import getpass as get_keyword

class GuessWord(object):
    
    def __init__(self, player_one, player_two):
        self.word_list = ["jack", "back", "cock", "luck", "bang", "tool", "dogs", "bags", "life", "kick"]
        self.player_one = Player(player_one)
        self.player_two = Player(player_two)
        self.players = [self.player_one, self.player_two]
        self.player_names = [player.name for player in self.players]
        self.computer = "Computer"
        if self.computer in self.player_names:
            self.mode = 1
        else:
            self.mode = 2
        self.player_cursor = 0

    def start_game(self):
        if self.mode == 1:
            self.current_player = self.player_one
            self.other_player = self.player_two
            self.word = ""
        else:
            self.current_player = self.players[self.player_cursor%len(self.players)]
            self.other_player = self.players[(self.player_cursor+1)%len(self.players)]
            self.word = get_keyword("Player %s, please enter the word for player %s to guess: " % (self.other_player.name, self.current_player.name) )
        self.key = True
        self.last_word = []
        while self.key == True:
            self.star = 0
            self.exc = 0
            self.tmp_word_length = 0
            self.diff = []
            self.diff_index = []

            #checking and grabbing the game word
            if self.word == "":
                self.word = self.grab_word()

            #grabbing the guess word and checking the word length
            while self.tmp_word_length != len(self.word):
                self.tmp_word = raw_input("Enter your guess that must be containing "+ str(len(self.word)) +" letters: ")
                self.tmp_word_length = len(self.tmp_word)

            #Exact word match if block
            if self.word == self.tmp_word:
                self.player_one.games_played += 1
                self.player_two.games_played += 1
                self.current_player.wins += 1
                if self.mode == 2:
                    self.player_cursor += 1
                    self.current_player = self.players[(self.player_cursor)%len(self.players)]
                    self.other_player = self.players[(self.player_cursor+1)%len(self.players)]
                for player in self.players:
                    print "For player: ", player.name
                    print "Games Played: ", player.games_played
                    print "Games Won: ", player.wins
                self.new_key = int(raw_input("Congrats! you've got the right word. To continue playing the game please enter 1 and to quit enter 2: \n 1. play \n 2. quit \n"))
                if self.new_key == 1:
                    self.last_word.append(self.word)
                    if self.mode == 2:
                        self.word = get_keyword("Player %s, please enter the word for player %s to guess: " % (self.other_player.name, self.current_player.name) )
                    else:
                        self.word = ""
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
        self.new_word = ""
        self.new_tmp_word = ""
        for i, char in enumerate(self.word):
            if self.tmp_word[i] == char:
                self.star += 1
                continue
            self.new_word += char
            self.new_tmp_word += self.tmp_word[i]

    def calculate_exclamation(self):
        new_word_count = dict(collections.Counter(self.new_word))
        new_tmp_word_count = dict(collections.Counter(self.new_tmp_word))
        for char in new_word_count:
            if new_tmp_word_count.has_key(char):
                self.exc += min(new_tmp_word_count[char], new_word_count[char])

class Player(object):
    def __init__(self, name=None):
        self.name = name
        self.games_played = 0
        self.wins = 0
        self.lost = 0
