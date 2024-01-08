"""I'm stuck in CREATE PLATER CLASSES THAT REMEMBER"""
"""The class created is ReflectPlayer(Player)"""
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

class Player:
    """
    Parent class with 2 methods. 
    """    
    def move(self):
        pass

    def learn(self, my_move, their_move):
        self.player_move = my_move
        self.opponent_move = their_move


def beats(one, two):
    """
    Function to check who won. If return is 1, player wins, if return is 2, computer wins.
    """
    print(f"In beats function... Who will win? Computer has choosen {two}, player {one}")
    if ( one == 'rock' and two == 'scissors' ) or ( one == 'scissors' and two == 'paper' ) or ( one == 'paper' and two == 'rock' ):
        return 1
    elif ( two == 'rock' and one == 'scissors' ) or ( two == 'scissors' and one == 'paper' ) or ( two == 'paper' and one == 'rock' ):
        return 2
    elif (one == 'rock' and two == 'rock') or (one == 'scissors' and two == 'scissors') or (one == 'paper' and two == 'paper'):
        return 0
    else : 
        print("ERROR in beats")


class RandomPlayer(Player):
    def move(self):
        value = random.randint(0, 2)
        #print(f"Value {value}")
        if value == 0:
            return 'rock'
        elif value == 1:
            return 'paper'
        else:
            return 'scissors'
        
class HumanPlayer(Player):
    def move(self):
        while True:
            try:
                number = int(input("What will you go for? 1 is rock, 2 is paper and 3 is scissors"))
                if number in (1,2,3):
                    break
                else:
                    print("You didn't select anything")
            except ValueError:
                print("Invalid input")

        if number == 1: return 'rock'
        elif number == 2: return 'paper'
        elif number == 3: return 'scissors'
        else: return moves[random.randint(0,2)]


class ReflectPlayer(Player):
    
    def reactive_move(self,opponent_move):
        if self.opponent_move == moves[0]: return moves[1]
        elif self.opponent_move == moves[1]: return moves[2]
        elif self.opponent_move == moves[2]: return moves [0]
        else: return moves[random.randint(0,2)]
        


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.scorePlayer1 = 0
        self.scorePlayer2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.reactive_move(move1)
        print(f"You: {move1}  Computer: {move2}")
        result = beats(move1,move2)
        if result == 1:
            self.scorePlayer1 += 1
        elif result == 2:
            self.scorePlayer2 += 1
        else:
            return 0 
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print("=====================================================")
            print(f"Round {round}:")
            self.play_round()
        
        if self.scorePlayer1 > self.scorePlayer2:
            print("YOU WINS")
        elif self.scorePlayer1 < self.scorePlayer2:
            print("COMPUTER WINS")
        else:
            print("DRAW")
        print("Game over!")


if __name__ == '__main__':
    player1 = HumanPlayer()
    player2 = ReflectPlayer()
    game = Game(player1, player2)
    game.play_game()
