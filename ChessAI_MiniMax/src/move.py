class Move:
    def __init__(self, initial, final):
        """
        Initialize a move with the initial and final squares.
        
        :param initial: The initial square (instance of Square)
        :param final: The final square (instance of Square)
        """
        self.initial = initial  # Initial square of the move
        self.final = final  # Final square of the move

    def __str__(self):
        """
        Return a string representation of the move.
        
        :return: String in the format '(initial_col, initial_row) -> (final_col, final_row)'
        """
        s = ''
        s += f'({self.initial.col}, {self.initial.row})'
        s += f' -> ({self.final.col}, {self.final.row})'
        return s

    def __eq__(self, other):
        """
        Override equality to compare moves based on initial and final squares.
        
        :param other: The other move to compare with
        :return: True if both moves are the same, False otherwise
        """
        return self.initial == other.initial and self.final == other.final
