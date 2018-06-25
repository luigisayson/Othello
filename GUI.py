from tkinter import *
import GameState
from ResizingCanvas import ResizingCanvas

class GUI:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.state = GameState.GameState(rows, cols)
        self.board =  self.state.board
        self.master = Tk()
        self.master.title("Othello White's Turn")
        self.frame = Frame(self.master)
        self.frame.pack(fill=BOTH, expand=YES)
        self.make_canvas()
    
    def make_canvas(self):
        self.canvas = ResizingCanvas(self.frame, width=self.cols * 75, height=self.rows * 75, bg = "green", highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=YES)
        self.row_height = self.canvas.height/self.rows
        self.col_width = self.canvas.width/ self.cols
        
        #create grid lines
        for i in range(self.rows):
            self.canvas.create_line(0, self.row_height * i, self.canvas.width, self.row_height * i, fill = "black")
        for i in range(self.cols):
            self.canvas.create_line(self.col_width * i, 0, self.col_width * i, self.canvas.height, fill = "black")
        self.update_board()
        self.canvas.bind("<Button-1>", self.onClick)     
    
    
    def start(self):
        self.master.mainloop()
        
    def onClick(self, event):
        #Handles when a player clicks on the board
        
        if self.state.is_game_over():
            return
        
        self.row_height = self.canvas.height/self.rows
        self.col_width = self.canvas.width/ self.cols
        
        #Make a move on the square the player clicked on, if valid
        #If legal move executed successfully, update the canvas
        if (self.state.execute_move([int(event.y / self.row_height), int(event.x / self.col_width)])):
            self.update_board()
            self.update_turn()

        #Display the result of the game if the game is over
        if self.state.is_game_over():
            result = self.determine_result()
            self.master.title("Othello: " + result)
            
    def determine_result(self):
        #Returns the result of the game
        piece_count = self.state.board.count_pieces()
        if piece_count["B"] == piece_count["W"]:
            return "Draw"
        return "Black Wins"  if piece_count["B"] > piece_count["W"] else "White Wins"
    
    def get_clr_name(self, color):
        return "White" if color == "W" else "Black"
    
    def update_turn(self):
        self.master.title("Othello: "+ self.get_clr_name(self.state.turn) + "'s turn")
    
    def update_board(self):
        #Updates the canvas
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                square = self.board.get_square((row, col))
                if square == "B" or square == "W":
                    x0 = self.col_width * col
                    y0 = self.row_height * row
                    x1 = x0 + self.col_width
                    y1 = y0 + self.row_height
                    self.canvas.create_oval(x0,y0,x1,y1, fill = self.get_clr_name(square))
                    
        