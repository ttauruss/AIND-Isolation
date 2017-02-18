import random
import isolation

def custom_score(game, player):
    my_moves = len(game.get_legal_moves(player))
    if player == game.active_player and my_moves == 0:
        return float('-inf')
    return float(my_moves)

def custom_score3(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - opp_moves)

def custom_score2(game, player):

    # if game.move_count < 7:
        # return random.randint(1, 10) 
        # return 0.

    my_moves = len(game.get_legal_moves(player))
    if player == game.active_player and my_moves == 0:
        return float('-inf')

    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    if player == game.inactive_player and opp_moves == 0:
        return float('inf')

    # loc = game.get_player_location(player)
    # dist = abs(float(loc[0]) - 3.5) + abs(float(loc[1]) - 3.5)

    return float(my_moves - opp_moves)

    # print(game.move_count)
    # blank_size = len(game.get_blank_spaces())
    # field_size = game.width * game.height
    # if game.move_count < 20:
        # return float(opp_moves - my_moves)
    # else: # return float(2 * my_moves - opp_moves)

def custom_score_optimized(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # if game.is_loser(player):
        # return float('-inf')
    # if game.is_winner(player):
        # return float('inf')

    my_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    if player == game.active_player:
        if my_moves == 0:
            return float('-inf')
    else:
        if opp_moves == 0:
            return float('inf')
    return float(my_moves - opp_moves)

    # loc = game.get_player_location(player)
    # free_area_size = 0
    # blanks = game.get_blank_spaces()
    # for i in (loc[0]-2, loc[0]+3):
        # for j in (loc[1]-2, loc[1]+3):
            # if (i, j) in blanks:
                # free_area_size += 1

    # return float(my_moves - 2 * opp_moves + (2 * free_are_size) / 25)
    # return float(my_moves - 2 * opp_moves)
    # if game.dead_moves == None:
        # game.dead_moves = 0
    # if game.change_strategy == None:
        # game.change_strategy = False
    # print(my_moves)
    # if my_moves == 1:
        # game.dead_moves += 1
        # game.change_strategy = True
        # print(game.dead_moves)
    # if game.change_strategy:
        # return (my_moves - opp_moves)
    # else:
    # blank_size = len(game.get_blank_spaces())
    # field_size = game.width * game.height
    # if blank_size > field_size / 2:
        # return float(opp_moves - my_moves)
    # else:
        # return float(my_moves - opp_moves)

