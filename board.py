class chessgame(object):


    def __init__(self):
        super(chessgame, self).__init__()
        self.board = [['br','bn','bb','bq','bk','bb','bn','br'],
                 ['bp','bp','bp','bp','bp','bp','bp','bp'],
                 [' ',' ',' ',' ',' ',' ',' ',' '],
                 [' ',' ',' ',' ',' ',' ',' ',' '],
                 [' ',' ',' ',' ',' ',' ',' ',' '],
                 [' ',' ',' ',' ',' ',' ',' ',' '],
                 ['wp','wp','wp','wp','wp','wp','wp','wp'],
                 ['wr','wn','wb','wq','wk','wb','wn','wr']]



    def wmove(piece,spos,epos):
        #start position and end position



        pass
    def bmove():
        pass
    def eval():
        pass

    def printboard(self):
        dictionary = {"wk":"♔",
                      "wq":"♕",
                      "wp":"♙",
                      "wr":"♖",
                      "wn":"♘",
                      "wb":"♗",
                      "bk":"♚",
                      "bq":"♛",
                      "br":"♜",
                      "bb":"♝",
                      "bp":"♟",
                      "bn":"♞",
                      " ": "  "}
        print("▟ ",end="")
        abc = ["a","b","c","d","e","f","g","h"]
        for a in range(0,8):
            print(abc[a],end='  ')
        print("")
        for i in range(0,8):
            # hint: Magic pre-row
            print(7-i+1,end='|')
            for j in range(0,8):
                piece = self.board[i][j]
                print(dictionary[piece],end='|')
            #hint : Magic post-row
            print("")
