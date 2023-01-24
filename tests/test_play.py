import random

from schnapsen.bots import SchnapsenServer
from schnapsen.game import SchnapsenGamePlayEngine

from schnapsen.bots import RdeepBot, BullyBot, MLDataBot

import pathlib


def play() -> None:
    """Play a game between the two bots"""
    engine = SchnapsenGamePlayEngine()
    bot1 = MLDataBot(BullyBot(random.Random(12)), pathlib.Path('E:\MLBOT'))
    bot2 = RdeepBot(10, 10, random.Random(15))
    winner, points, score = engine.play_game(bot1, bot2, random.Random(1))
    print(f"Winner is: {winner}, card score was {score} and  {points} gamepoints!")


def interactive() -> None:
    """Run the GUI."""
    engine = SchnapsenGamePlayEngine()
    bot1 = BullyBot(rng=random.Random(46764))
    with SchnapsenServer() as s:
        bot2 = s.make_gui_bot(name="mybot2")
        engine.play_game(bot1, bot2, random.Random(100))


if __name__ == "__main__":
    play()
    interactive()


def play_test() -> None:
    """Play multiple games between the two bots"""
    for i in range(1):
        play()
