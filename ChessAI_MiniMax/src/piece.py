import os

class Piece:
    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name  # Name of the piece (e.g., 'pawn', 'knight')
        self.color = color  # Color of the piece ('white' or 'black')
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign  # Value of the piece, adjusted by color
        self.moves = []  # List to store possible moves for the piece
        self.moved = False  # Flag to check if the piece has moved
        self.texture = texture  # Path to the texture image
        self.set_texture()  # Set the texture based on size and piece type
        self.texture_rect = texture_rect  # Rectangle defining the texture position

    def set_texture(self, size=80):
        """Sets the texture path based on piece size and type."""
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')

    def add_move(self, move):
        """Adds a possible move to the piece's move list."""
        self.moves.append(move)

    def clear_moves(self):
        """Clears the list of possible moves."""
        self.moves = []

class Pawn(Piece):
    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1  # Direction of movement for the pawn
        self.en_passant = False  # Flag for en passant move possibility
        super().__init__('pawn', color, 1.0)  # Initialize the base class

class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 3.0)  # Initialize the base class

class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.001)  # Initialize the base class

class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 5.0)  # Initialize the base class

class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen', color, 9.0)  # Initialize the base class

class King(Piece):
    def __init__(self, color):
        self.left_rook = None  # Reference to the left rook for castling
        self.right_rook = None  # Reference to the right rook for castling
        super().__init__('king', color, 10000.0)  # Initialize the base class
