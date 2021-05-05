import pieces
class chessgame(object):


    def __init__(self):
        super(chessgame, self).__init__()
        wp1 = pieces.pawn("a","2",1)
        wp2 = pieces.pawn("b","2",1)
        wp3 = pieces.pawn("c","2",1)
        wp4 = pieces.pawn("d","2",1)
        wp5 = pieces.pawn("e","2",1)
        wp6 = pieces.pawn("f","2",1)
        wp7 = pieces.pawn("g","2",1)
        wp8 = pieces.pawn("h","2",1)

        bp1 = pieces.pawn("a","7",-1)
        bp2 = pieces.pawn("b","7",-1)
        bp3 = pieces.pawn("c","7",-1)
        bp4 = pieces.pawn("d","7",-1)
        bp5 = pieces.pawn("e","7",-1)
        bp6 = pieces.pawn("f","7",-1)
        bp7 = pieces.pawn("g","7",-1)
        bp8 = pieces.pawn("h","7",-1)


        self.board = [
                 ['br','bn','bb','bq','bk','bb','bn','br'],
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
