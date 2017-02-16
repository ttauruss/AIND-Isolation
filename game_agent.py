"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random
import isolation

class Timeout(Exception):
    """Subclass base exception for code clarity."""
    pass


def custom_score(game, player):
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

    if game.is_loser(player):
        return float('-inf')
    if game.is_winner(player):
        return float('inf')

    my_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))

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
    blank_size = len(game.get_blank_spaces())
    field_size = game.width * game.height
    if blank_size > field_size / 2:
        return float(opp_moves - my_moves)
    else:
        return float(my_moves - opp_moves)

class CustomPlayer:
    """Game-playing agent that chooses a move using your evaluation function
    and a depth-limited minimax algorithm with alpha-beta pruning. You must
    finish and test this player to make sure it properly uses minimax and
    alpha-beta to return a good move before the search time limit expires.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    iterative : boolean (optional)
        Flag indicating whether to perform fixed-depth search (False) or
        iterative deepening search (True).

    method : {'minimax', 'alphabeta'} (optional)
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=10.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

    def get_move(self, game, legal_moves, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        This function must perform iterative deepening if self.iterative=True,
        and it must use the search method (minimax or alphabeta) corresponding
        to the self.method value.

        **********************************************************************
        NOTE: If time_left < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            A list containing legal moves. Moves are encoded as tuples of pairs
            of ints defining the next (row, col) for the agent to occupy.

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """

        self.time_left = time_left

        # TODO: finish this function!

        # Perform any required initializations, including selecting an initial
        # move from the game board (i.e., an opening book), or returning
        # immediately if there are no legal moves
        if game.get_player_location(game.active_player) == isolation.Board.NOT_MOVED:
            legal_moves = game.get_legal_moves()
            return legal_moves[random.randint(0, len(legal_moves)-1)]

        best_move = (-1, -1)
        try:
            # The search method call (alpha beta or minimax) should happen in
            # here in order to avoid timeout. The try/except block will
            # automatically catch the exception raised by the search method
            # when the timer gets close to expiring
            if not self.iterative:
                if self.method == 'minimax':
                    score, best_move = self.minimax(game, self.search_depth)
                else:
                    score, best_move = self.alphabeta(game, self.search_depth)
            else:
                depth = 0
                while True:
                    if self.method == 'minimax':
                        score, best_move = self.minimax(game, depth)
                    else:
                        score, best_move = self.alphabeta(game, depth)
                    depth += 1

        except Timeout:
            pass

        return best_move

    def minimax(self, game, depth, maximizing_player=True):
        """Implement the minimax search algorithm as described in the lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        
        uple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        moves = game.get_legal_moves()
        if depth == 0 or moves == []:
            if maximizing_player:
                return self.score(game, game.active_player), (-1, -1)
            else:
                return self.score(game, game.inactive_player), (-1, -1)
        if maximizing_player:
            score = float('-inf')
        else:
            score = float('inf')
        best_move = (-1, -1)
        for mv in moves:
            # game_copy = game.copy()
            game_copy = game.forecast_move(mv)
            # game_copy.apply_move(mv)
            new_score, new_best_move = self.minimax(game_copy, depth - 1, not maximizing_player)
            if (maximizing_player and new_score > score) or (not maximizing_player and new_score < score):
                score = new_score
                best_move = mv
        return score, best_move



    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        """Implement minimax search with alpha-beta pruning as described in the
        lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        moves = game.get_legal_moves()
        if depth == 0 or moves == []:
            if maximizing_player:
                return self.score(game, game.active_player), (-1, -1)
            else:
                return self.score(game, game.inactive_player), (-1, -1)
        if maximizing_player:
            score = float('-inf')
        else:
            score = float('inf')
        best_move = (-1, -1)
        for mv in moves:
            game_copy = game.forecast_move(mv)
            new_score, new_best_move = self.alphabeta(game_copy, depth - 1, alpha, beta, not maximizing_player)
            if maximizing_player:
                if new_score > score:
                    score = new_score
                    best_move = mv
                if score >= beta:
                    return score, best_move
                alpha = max(alpha, score)
            else:
                if new_score < score:
                    score = new_score
                    best_move = mv
                if score <= alpha:
                    return score, best_move
                beta = min(beta, score)
        return score, best_move


