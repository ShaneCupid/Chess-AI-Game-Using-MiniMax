import pygame
from const import *

class Dragger:
    def __init__(self):
        self.piece = None  # The piece being dragged
        self.dragging = False  # Flag to indicate if a piece is being dragged
        self.mouseX = 0  # Current X position of the mouse
        self.mouseY = 0  # Current Y position of the mouse
        self.initial_row = 0  # Initial row of the piece before dragging
        self.initial_col = 0  # Initial column of the piece before dragging

    # Method to update the piece being dragged
    def update_blit(self, surface):
        # Set texture size to 128 pixels
        self.piece.set_texture(size=128)
        texture = self.piece.texture
        # Load the image
        img = pygame.image.load(texture)
        # Get the rectangle centered at the current mouse position
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        # Draw the image on the given surface
        surface.blit(img, self.piece.texture_rect)

    # Method to update the mouse position
    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos  # Update mouse coordinates (x, y)

    # Method to save the initial position of the piece
    def save_initial(self, pos):
        self.initial_row = pos[1] // SQSIZE  # Calculate the initial row
        self.initial_col = pos[0] // SQSIZE  # Calculate the initial column

    # Method to start dragging a piece
    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    # Method to stop dragging a piece
    def undrag_piece(self):
        self.piece = None
        self.dragging = False
