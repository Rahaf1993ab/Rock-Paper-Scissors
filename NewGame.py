import random

moves = ['rock', 'paper', 'scissors']


class Player():

    def __init__(self):

        self.score = 0

    def move(self):

        return 'rock'

    def learn(self, learn_move):

        pass


class HumanPlayer(Player):

    def move(self):

        move = input('rock, paper, scissors? >').lower()
        while move != 'rock' and move != 'paper' and move != 'scissors':
            print('Try again')
            move = input('rock, paper, scissors? >').lower()
        return (move)


class RandomPlayer(Player):
    def move(self):
        move = random.choice(moves)
        return (move)


class ReflectPlayer(Player):

    def __init__(self):

        Player.__init__(self)
        self.learn_move = None

    def move(self):
        if self.learn_move is None:
            move = moves[0]
            return (move)
        else:
            move = self.learn_move
            return (move)

    def learn(self, learn_move):
        self.learn_move = learn_move


class Cycles(Player):

    def __init__(self):
        Player.__init__(self)
        self.phase = 0

    def move(self):
        move = {
            "rock": "paper",
            "paper": "scissors",
            "scissors": "rock"
        }
        return move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game():

    def __init__(self, p2):
        self.p1 = HumanPlayer()
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        score = Game.play(move1, move2)
        self.p1.learn(move2)
        self.p2.learn(move1)

    def play_game(self):

        print("Start the game!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print('Player 1 won!')
        elif self.p1.score < self.p2.score:
            print('Player 2 won!')
        else:
            print('The game was a tie!')
        print(str(self.p1.score) + '-' + str(self.p2.score))

    def play_single(self):
        print("Start the game!")
        self.play_round()
        if self.p1.score > self.p2.score:
            print('Player 1 won!')
        elif self.p1.score < self.p2.score:
            print('Player 2 won!')
        else:
            print('The game was a tie!')
        print(str(self.p1.score) + '-' + str(self.p2.score))

    def play(self, move1, move2):

            if beats(move1, move2):
                print("Player 1 wins")
                self.p1.score += 1
                return 1
            elif beats(move2, move1):
                print("Player 2 wins")
                self.p2.score += 1
                return 2
            else:
                print("It's a tie")
                return 0


if __name__ == '__main__':
    p2 = input('Select the mood of game: (1)Rock, (2)Random,\
(3)Reflective, or (4)Cycles: >')
    while True:
        if p2 == '1':
            p2 = Player()
            break
        elif p2 == '2':
            p2 = RandomPlayer()
            break
        elif p2 == '3':
            p2 = ReflectPlayer()
            break
        elif p2 == '4':
            p2 = Cycles()
            break
        else:
            print("Try again")
            p2 = input('Select the mood of game: (1)Rock, (2)Random,\
(3)Reflective, or (4)Cycles: >')

    rounds = input('Choose One game (1) or Multiple game (2): >')
    Game = Game(p2)
    while True:
        if rounds == '1':
            Game.play_single()
            break
        elif rounds == '2':
            Game.play_game()
            break
        else:
            print('try again')
            rounds = input('Choose One game (1) or Multiple game (2):')
