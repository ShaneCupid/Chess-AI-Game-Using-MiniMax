import pygame
import os
from sound import Sound
from theme import Theme

class Config:
    def __init__(self):
        self.themes = []  # List of available themes
        self._add_themes()  # Add themes to the list
        self.idx = 0  # Index of the current theme
        self.theme = self.themes[self.idx]  # Set the current theme
        self.font = pygame.font.SysFont('monospace', 18, bold=True)  # Font for the game
        self.move_sound = Sound(os.path.join('assets/sounds/move.wav'))  # Sound for a move
        self.capture_sound = Sound(os.path.join('assets/sounds/capture.wav'))  # Sound for a capture

    def change_theme(self):
        """Cycle through the available themes."""
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]

    def _add_themes(self):
        """Add predefined themes to the themes list."""
        # Existing themes
        green = Theme((234, 235, 200), (119, 154, 88), (244, 247, 116), (172, 195, 51), '#C86464', '#C84646')
        brown = Theme((235, 209, 166), (165, 117, 80), (245, 234, 100), (209, 185, 59), '#C86464', '#C84646')
        blue = Theme((229, 228, 200), (60, 95, 135), (123, 187, 227), (43, 119, 191), '#C86464', '#C84646')
        gray = Theme((120, 119, 118), (86, 85, 84), (99, 126, 143), (82, 102, 128), '#C86464', '#C84646')

        # Superhero-inspired themes
        spiderman = Theme((255, 0, 0), (0, 0, 255), (255, 100, 100), (100, 100, 255), '#FF0000', '#0000FF')
        black_panther = Theme((0, 0, 0), (105, 105, 105), (50, 50, 50), (169, 169, 169), '#000000', '#696969')
        wolverine = Theme((255, 215, 0), (0, 0, 128), (255, 255, 102), (25, 25, 112), '#FFD700', '#000080')
        hulk = Theme((0, 128, 0), (128, 0, 128), (144, 238, 144), (186, 85, 211), '#008000', '#800080')
        iron_man = Theme((255, 140, 0), (178, 34, 34), (255, 165, 0), (220, 20, 60), '#FF8C00', '#B22222')

        self.themes = [blue, green, brown, gray, spiderman, black_panther, wolverine, hulk, iron_man]  # List of themes
