from collections import defaultdict

class Board:
    def __init__ (self, rows, cols):
        #A board must be initialized with the number of rows and columns
        self.rows = rows
        self.cols = cols
        self.board = []
        
        #Used for checking possible moves
        self.directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        
        #Fill board with zeroes and starting pieces
        self.init_board()
        
    def init_board(self):
        #initializes the board to the starting position
        #Start by initializing all squares to "0" 
        for row in range(self.rows):
            self.board.append([])
            for col in range(self.cols):
                self.board[row].append("0")

        # Once the board is filled with zeroes, place two white pieces 
        # and two black pieces on the center squares like so: 
        # |WB| 
        # |BW|
        start_row = int(self.rows / 2 - 1) 
        start_col = int(self.cols / 2 - 1)
        self.board[start_row][start_col] = "W"
        self.board[start_row + 1][start_col + 1] = "W"
        self.board[start_row][start_col + 1] = "B"
        self.board[start_row + 1][start_col] = "B"
        
    def set_square(self,square, color):
        self.board[square[0]][square[1]] = color
        
    def get_square(self, square):
        #returns the piece in a given square
        return self.board[square[0]][square[1]]
    
    def move_cursor(self, c, d):
        #moves the "cursor" c by one in  direction d
        c[0] += d[0]
        c[1] += d[1]
        
    def check_direction(self, square, d, color):
        #make a new list from the given tuple "square" to make it mutable
        #This will be a "cursor" of sorts by which we will check and flip squares 
        c = list(square)    
        
        #make a new list from the given tuple "square" to make it mutable
        #This will be a "cursor" of sorts by which we will check and flip squares 
        self.move_cursor(c,d)
        
        #if the next square is empty or not the opposite color, return false
        if not self.is_location_valid(c) or self.get_square(c) != self.rvrs_col(color):
            return False
        
        #Check until a square of the same color is found on the other side of the starting square.
        #If none is found, then there are no pieces that can be flipped in this direction 
        while(self.is_location_valid(c)):
            if self.get_square(c) == color:
                return True
            if self.get_square(c) == "0":
                return False
            self.move_cursor(c, d)
        return False
    
    def is_move_legal(self, square, color):
        #Checks if a move can be made on a given square
        
        #return False right away if square is not empty
        if self.get_square(square) != "0":
            return False
        
        for direction in self.directions:
            if self.check_direction(square, direction, color):
                return True
        return False
    
    def flip_square(self, square):
        #flips the piece on a given square to the opposite color
        self.set_square(square, self.rvrs_col(self.get_square(square)))
    
    def flip_direction(self, square, d, color):
        #flips all the pieces to the opposite color in a given direction from a square
        
        #make a new list from the given tuple "square" to make it mutable
        #This will be a "cursor" of sorts by which we will check and flip squares 
        c = list(square)
        
        #Move the "cursor" to the next square 
        self.move_cursor(c,d)
    
        #Keep flipping until the next piece is not a piece of the opposite color 
        while(self.get_square(c) == self.rvrs_col(color)):
            self.flip_square(c)
            self.move_cursor(c,d)

    def flip_all(self, square, color):
        #flips all the pieces in all directions where it will be valid to do so
        for d in self.directions:
            if self.check_direction(square, d, color):
                self.flip_direction(square, d, color)
        return
    
    def is_location_valid(self, square):
        #Checks if a given index in the form: [row, column] is within the borders of the board
        return True if 0 <= square[0] < self.rows and 0 <= square[1] < self.cols else False
    
    def rvrs_col(self, color):
        #returns the opposite of the given color
        return "B" if color == "W" else "W"
    
    def count_pieces(self):
        #returns a dictionary with the colors of the pieces (black and white) as the keys, and 
        #the number of pieces of that color currently on the board as values.
        d = defaultdict(int)
        for row in self.board:
            for item in row:
                d[item] += 1
        return d
    
    def check_for_legal_moves(self, color):
        #Scans the entire board for any squares that the current player can move on 
        for row in range(self.rows):
            for col in range(self.cols):
                square = (row,col)
                if self.get_square(square) =="0":
                    if self.is_move_legal(square, color):
                        return True
        return False
    
    def __str__(self):
        #Overloaded string method used for testing
        result = ""
        for row in self.board:
            for item in row:
                result += item + " "
            result += "\n"
        return result