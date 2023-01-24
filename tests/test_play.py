import random

from schnapsen.bots import SchnapsenServer
from schnapsen.game import SchnapsenGamePlayEngine

from schnapsen.bots import RdeepBot, BullyBotTheSecond, MLDataBot, RandBot, BullyBotTheFirst

import pathlib


def play() -> None:
    """Play a game between the two bots"""
    engine = SchnapsenGamePlayEngine()
    bot1 = MLDataBot(BullyBotTheSecond(random.Random()), pathlib.Path('E:\MLBOT\MLDATA.txt'))
    #bot2 = RdeepBot(10, 10, random.Random())
    bot2 = RandBot(56)
    winner, points, score = engine.play_game(bot1, bot2, random.Random())
    print(f"Winner is: {winner}, card score was {score} and  {points} gamepoints!")


def interactive() -> None:
    """Run the GUI."""
    engine = SchnapsenGamePlayEngine()
    bot1 = BullyBot(rng=random.Random(46764))
    with SchnapsenServer() as s:
        bot2 = s.make_gui_bot(name="mybot2")
        engine.play_game(bot1, bot2, random.Random(100))


def play_test() -> None:
    """Play multiple games between the two bots"""
    for i in range(10):
        play()


if __name__ == "__main__":
    play_test()


