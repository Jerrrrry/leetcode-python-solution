class Game:
        def __init__(self):
                self.board=[[0]*7 for _ in range(6)]
                self.limit=[5]*7

                print(self.board)

        def drop(self,col:int,player:int)->bool:
                if self.limit[col]>=0:
                        res=[self.limit[col],col]
                        self.board[self.limit[col]][col]=player
                        self.limit[col]-=1
                        return res
                else:
                        return []
        def printBoard(self):
                print('this round')
                for x in self.board:
                        print(x)

        def validateWin(self,p:list):
                player=self.board[p[0]][p[1]]
                #horizental

                for r in range(6):
                        for c in range(4):
                                if self.board[r][c]==player and self.board[r][c+1]==player and self.board[r][c+2]==player and self.board[r][c+3]==player:
                                        print('Player '+str(player)+' win at horizental')
                                        return True

                for r in range(3):
                        for c in range(7):
                                if self.board[r][c]==player and self.board[r+1][c]==player and self.board[r+2][c]==player and self.board[r+3][c]==player:
                                        print('Player '+str(player)+' win at vertical')
                                        return True

                for r in range(3):
                        for c in range(4):
                                if self.board[r][c]==player and self.board[r+1][c+1]==player and self.board[r+2][c+2]==player and self.board[r+3][c+3]==player:
                                        print('Player '+str(player)+' win at d1')
                                        return True

                for r in range(3,6):
                        for c in range(4):
                                if self.board[r][c]==player and self.board[r-1][c+1]==player and self.board[r-2][c+2]==player and self.board[r-3][c+3]==player:
                                        print('Player '+str(player)+' win at d2')
                                        return True
                print('Player '+str(player)+' no win')
                return False
                        

                

g=Game()

p=1

for i in range(4):
        res=g.drop(3,p)
        if res:
                g.validateWin(res)
                g.printBoard()
        else:
                print('cant play in this col any more')
        