from Board import Board

class GameState:
    def __init__(self, rows, cols):
        self.turn = "W"
        self.board = Board(rows, cols)
        
    def change_turn(self):
        self.turn = "W" if self.turn == "B" else "B"
        return self.turn
    
    def execute_move(self, square):
        #makes a move and edits the board if the given move is legal
        if(self.board.is_move_legal(square, self.turn)):
            self.board.set_square(square, self.turn)
            self.board.flip_all(square, self.turn)
            self.change_turn()
            return True
        return False
    
    def is_game_over(self):
        if not self.board.check_for_legal_moves(self.turn) and \
            not self.board.check_for_legal_moves(self.change_turn()):
                return True
        return False
    