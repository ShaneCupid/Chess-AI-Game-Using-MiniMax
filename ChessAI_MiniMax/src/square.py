class Square:
    ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

    def __init__(self, row, col, piece=None):
        self.row = row  # Row position of the square
        self.col = col  # Column position of the square
        self.piece = piece  # Piece on the square (if any)
        self.alphacol = self.ALPHACOLS[col]  # Alphabetical representation of the column

    def __eq__(self, other):
        """Override equality to compare squares based on row and column."""
        return self.row == other.row and self.col == other.col

    def has_piece(self):
        """Check if the square has a piece."""
        return self.piece is not None

    def isempty(self):
        """Check if the square is empty."""
        return not self.has_piece()

    def has_team_piece(self, color):
        """Check if the square has a piece of the same color."""
        return self.has_piece() and self.piece.color == color

    def has_enemy_piece(self, color):
        """Check if the square has an enemy piece (different color)."""
        return self.has_piece() and self.piece.color != color

    def isempty_or_enemy(self, color):
        """Check if the square is either empty or has an enemy piece."""
        return self.isempty() or self.has_enemy_piece(color)

    @staticmethod
    def in_range(*args):
        """Check if given arguments (rows or columns) are within the board range (0-7)."""
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        return True

    @staticmethod
    def get_alphacol(col):
        """Get the alphabetical representation of a column."""
        ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        return ALPHACOLS[col]
