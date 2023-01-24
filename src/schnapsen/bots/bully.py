import random
from typing import Optional
from schnapsen.game import Bot, PlayerPerspective, Move, SchnapsenTrickScorer, RegularMove
from schnapsen.deck import Card, Suit


class BullyBot(Bot):
    def __init__(self, rng: random.Random) -> None:
        self.rng = rng

    def get_move(self, player_perspective: PlayerPerspective, leader_move: Optional[Move], ) -> Move:
        # The bully bot only plays valid moves.
        # get all valid moves
        my_valid_moves = player_perspective.valid_moves()
        trump_suit_moves: list[Move] = []

        # get the trump suit
        trump_suit: Suit = player_perspective.get_trump_suit()

        # get all my valid moves that have the same suit with trump suit.
        for move in my_valid_moves:
            cards_of_move: list[Card] = move.cards
            # get 1st of the list of cards of this move (in case of multiple -> Marriage)
            card_of_move: Card = cards_of_move[0]

            if card_of_move.suit == trump_suit:
                trump_suit_moves.append(move)

        # If you are the follower and you have cards of the same suit as the opponent, play one of these at random.
        if not player_perspective.am_i_leader():
            assert leader_move is not None
            leader_suit: Suit = leader_move.cards[0].suit
            leaders_suit_moves: list[Move] = []

            # get all my valid moves that have the same suit with leader suit.
            for move in my_valid_moves:
                cards_of_move = move.cards
                # get 1st of the list of cards of this move (in case of multiple -> Marriage)
                card_of_move = cards_of_move[0]

                if card_of_move.suit == leader_suit:
                    leaders_suit_moves.append(move)

            if len(leaders_suit_moves) > 0:
                random_leader_suit_move = self.rng.choice(leaders_suit_moves)
                return random_leader_suit_move

        # create an instance object of a SchnapsenTrickScorer Class, that allows us to get the rank of Cards.
        schnapsen_trick_scorer = SchnapsenTrickScorer()

        # we set the highest rank to something negative, forcing it to change with the first comparison, since all scores are positive
        highest_trump_card_score: int = -1
        trump_card_with_highest_score: Optional[Card] = None

        # Else, you have cards of the trump suit, play the one with the highest rank
        if len(trump_suit_moves) > 0:
            for move in trump_suit_moves:
                card_of_trump_move = move.cards[0]
                trump_card_score = schnapsen_trick_scorer.rank_to_points(card_of_trump_move.rank)
                if trump_card_score > highest_trump_card_score:
                    highest_trump_card_score = trump_card_score
                    trump_card_with_highest_score = card_of_trump_move

            # if our logic above was correct, this can never be None. We double check to make sure.
            assert trump_card_with_highest_score is not None

            # We now create a move out of this card. Note that here we do not return a move from a call to valid_moves.
            move_of_trump_card_with_highest_score = RegularMove(trump_card_with_highest_score)

            # We can double check that this is a valid move like this.
            assert move_of_trump_card_with_highest_score in my_valid_moves

            return move_of_trump_card_with_highest_score

        # Else, play a random move
        moves: list[Move] = player_perspective.valid_moves()
        random_move = self.rng.choice(list(moves))
        return random_move
