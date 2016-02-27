import game.main as game
import time
import sys

def main():
    play = "--++playtheguesswordgame++--"
    if len(sys.argv) > 1 and sys.argv[1] == "tut":

        print """
        Enter your guess that must be containing 4 letters: 
            """
        time.sleep(3)
        print """
        # now the player types the word 'buff'
        
        """
        time.sleep(5)
        print """
        Enter your guess that must be containing 4 letters: buff

        _ _ _ _ **
        """
        time.sleep(6)
        print """
        # the above is the clues for the player from his word buff
        # that is, the computer is saying that there are two characters
        # in the word 'buff' that exactly exists (and buff wasn't that 
        # word) in the word the computer has in it's mind.
        # Now the player tries to find which are those two characters
        # were exactly in its place and which two aren't part of the word
        # that computer have in its mind.

        loading .......
        """

        time.sleep(20)
        print """
        # Now again the user tries the word 'lube'

        Enter your guess that must be containing 4 letters: lube

        _ _ _ _ *!!

        """

        time.sleep(6)
        print """
        # from the above clue the player gets to know that the character 'u'
        # lies exactly at the second position on the word that he has to guess
        # and 'b' should be at the first position, from the previous clue (no 'f' here).
        # The player has now only a one ! to figure out. i,e either 'l' or 'b' exists in the 
        # word but misplaced. now he is going to figure it out by trying the word 'bulk'.

        """

        time.sleep(10)

        print """
        Enter your guess that must be containing 4 letters: bulk

        _ _ _ _ ***


        """

        print """
        # Here, the player knows, one '*' for 'b', one '*' for 'u' and the last star for 'l' (from 
        # previous clue). Now, he knows first three chars and he thinks the word might be 'bulb'

        """

        print """
        Enter your guess that must be containing 4 letters: bulb
        
        Congrats! you've got the right word. To continue playing the game please enter 1 and to quit enter 2: 
        1. play 
        2. quit 
        
        # so, that's it we guess!
        """

        play = raw_input("Do you want to play the game now! (y/n) :")
        while play != 'y' and play != 'Y' and play != 'n' and play != 'N':
            print "please type either 'y' or 'n' without single quote"
            play = raw_input("Do you want to play the game now! (y/n) :")

    if play == "--++playtheguesswordgame++--" or play == 'y' or play == 'Y':
        print """
                                        Welcome to Guess Word game
            Game: Computer will think a word and you should guess it. It would be easy to win 
            the game if you apply the basic logic.

            Play the game by typing your guess word.

            For each word you type, the game will output the number of characters that exactly 
            match the word that computer have in its mind (yes! the mind) as the number
            of stars and the number of characters that exist in the word but not in the appropriate 
            position with the number of exclamation symbol.

            """
        game_mode = ""
        while game_mode not in ["1", "2"]:
            game_mode = raw_input("For single player mode enter 1 \nFor multiplayer(2) mode enter 2 \n")

        if game_mode == "1":
            player_one = raw_input("Enter the player one name: ")
            player_two = "Computer"
            guess_word = game.GuessWord(player_one, player_two)
            guess_word.start_game()
        else:
            player_one = raw_input("Enter the player one name: ")
            player_two = raw_input("Enter the player two name: ")
            guess_word = game.GuessWord(player_one, player_two)
            guess_word.start_game()

    else:
        print "Good bye!"

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print "\n Recieved Interrupt Signal. Bye...."
        import sys
        sys.exit()
