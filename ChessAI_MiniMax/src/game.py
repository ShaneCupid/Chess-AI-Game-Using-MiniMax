import pygame
import datetime
import random
import chess
from const import *
from board import Board
from dragger import Dragger
from config import Config
from square import Square
from minimax import Minimax

class Game:

    def __init__(self):
        self.next_player = 'white'
        self.hovered_sqr = None
        self.board = Board()
        self.dragger = Dragger()
        self.config = Config()
        self.mode = self.select_mode()

    # blit methods

    def show_bg(self, surface):
        theme = self.config.theme
        
        for row in range(ROWS):
            for col in range(COLS):
                # color
                color = theme.bg.light if (row + col) % 2 == 0 else theme.bg.dark
                # rect
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)

                # row coordinates
                if col == 0:
                    # color
                    color = theme.bg.dark if row % 2 == 0 else theme.bg.light
                    # label
                    lbl = self.config.font.render(str(ROWS-row), 1, color)
                    lbl_pos = (5, 5 + row * SQSIZE)
                    # blit
                    surface.blit(lbl, lbl_pos)

                # col coordinates
                if row == 7:
                    # color
                    color = theme.bg.dark if (row + col) % 2 == 0 else theme.bg.light
                    # label
                    lbl = self.config.font.render(Square.get_alphacol(col), 1, color)
                    lbl_pos = (col * SQSIZE + SQSIZE - 20, HEIGHT - 20)
                    # blit
                    surface.blit(lbl, lbl_pos)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # piece ?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    # all pieces except dragger piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface):
        theme = self.config.theme

        if self.dragger.dragging:
            piece = self.dragger.piece

            # loop all valid moves
            for move in piece.moves:
                # color
                color = theme.moves.light if (move.final.row + move.final.col) % 2 == 0 else theme.moves.dark
                # rect
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)

    def show_last_move(self, surface):
        theme = self.config.theme

        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            for pos in [initial, final]:
                # color
                color = theme.trace.light if (pos.row + pos.col) % 2 == 0 else theme.trace.dark
                # rect
                rect = (pos.col * SQSIZE, pos.row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)

    def show_hover(self, surface):
        if self.hovered_sqr:
            # color
            color = (180, 180, 180)
            # rect
            rect = (self.hovered_sqr.col * SQSIZE, self.hovered_sqr.row * SQSIZE, SQSIZE, SQSIZE)
            # blit
            pygame.draw.rect(surface, color, rect, width=3)

    # other methods

    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'

    def set_hover(self, row, col):
        self.hovered_sqr = self.board.squares[row][col]

    def change_theme(self):
        self.config.change_theme()

    def play_sound(self, captured=False):
        if captured:
            self.config.capture_sound.play()
        else:
            self.config.move_sound.play()

    def reset(self):
        self.__init__()

    def random_move(self):
        moves = list(self.board.legal_moves)
        return random.choice(moves)

    def ai_move(self):
        board_fen = self.board.get_fen()
        chess_board = chess.Board(board_fen)
        move = Minimax.minimaxRoot(chess_board, 3, True, datetime.datetime.now(), 3)
        if move:
            self.board.apply_move(move.uci())

    def player_move(self, move_uci):
        move = self.board.uci_to_move(move_uci)
        if move:
            self.board.apply_move(move_uci)
            self.next_turn()

    def select_mode(self):
        print("Select Game Mode:")
        print("1: Player vs AI")
        print("2: AI vs AI")
        print("3: Player vs Player")
        mode = input("Enter mode number: ")
        if mode == "1":
            return "Player vs AI"
        elif mode == "2":
            return "AI vs AI"
        elif mode == "3":
            return "Player vs Player"
        else:
            print("Invalid selection. Defaulting to Player vs AI.")
            return "Player vs AI"

    def play_game(self):
        pygame.init()
        surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")

        while not self.board.is_game_over():
            self.show_bg(surface)
            self.show_pieces(surface)
            self.show_moves(surface)
            self.show_last_move(surface)
            self.show_hover(surface)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            if self.mode == "Player vs AI":
                if self.next_player == 'white':
                    move = input("Enter your move in UCI format (e.g., e2e4): ")
                    self.player_move(move)
                else:
                    self.ai_move()
                    self.next_turn()
            elif self.mode == "AI vs AI":
                self.ai_move()
                self.next_turn()
            elif self.mode == "Player vs Player":
                move = input("Enter your move in UCI format (e.g., e2e4): ")
                self.player_move(move)

            pygame.display.update()

        print("Game over:", self.board.outcome())

if __name__ == "__main__":
    game = Game()
    game.play_game()
