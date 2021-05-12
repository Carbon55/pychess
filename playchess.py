import board
import pieces

game1 = board.chessgame()
game1.printboard()
game1.wmove(1,1)
pawn1 = pieces.pawn("e","2",1)
pawn2 = pieces.pawn("e","7",-1)
pawn1.pos()
pawn2.pos()
pawn1.move(am=int(input("How many spaces do you want to move?")))
pawn1.pos()
