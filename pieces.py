
class pawn:

    def __init__(self,icol,irow,color):
        self.firstmove = True
        self.column = icol
        self.row = irow
        self.color = color
    def move(self,am=1):
        if am > 2:
            print("Error: Invalid Move")
        elif am ==2:
            if self.firstmove == True:
                self.firstmove = False
                #implement move
                start = self.row
                end = int(start) + 2 * self.color
                self.row=str(end)
            else:
                print("Error: Invalid Move")
        else:
            self.firstmove = False
            #implement move
            start = self.row
            end = int(start) + self.color
            self.row=str(end)



    def pos(self):
        print(f"my position is   :   {self.column}{self.row} \n first move =   {self.firstmove}")
        pass
