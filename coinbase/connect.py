
import random
import copy
class Game:
        def __init__(self):
                self.board=[[0]*7 for _ in range(6)]
                self.limit=[5]*7
                self.gg=False


        def drop(self,col:int,player:int)->list:
                if self.limit[col]>=0:
                        res=[self.limit[col],col]
                        self.board[self.limit[col]][col]=player
                        self.limit[col]-=1
                        return res
                else:
                        return []
        def positionScore(self,fakeboard:list,player:int):
                score=0
                ##check center line
                # center_col=[]
                # for i in range(6):
                #         center_col.append(fakeboard[i][3])
                # score+=center_col.count(player)*3
                #check horizental 
                for r in range(6):
                        for c in range(7-3):
                                w=fakeboard[r][c:c+4]
                                score+=self.evaluateWindow(w,player)

                #check vertical

                for c in range(7):
                        row=[]
                        for r in range(6):
                                row.append(fakeboard[r][c])
                        for i in range(3):
                                w=row[i:i+4]
                                score+=self.evaluateWindow(w,player)

                #d1
                for r in range(3):
                        for c in range(4):
                                w=[fakeboard[r+i][c+i] for i in range(4)]
                                score+=self.evaluateWindow(w,player)
                #d2

                for r in range(3,6):
                        for c in range(4):
                                w=[fakeboard[r-i][c+i] for i in range(4)]
                                score+=self.evaluateWindow(w,player)


                return score

        def evaluateWindow(self,window:list,player:int):
                score=0
                if player==1:
                        opp=2
                else:
                        opp=1
                if window.count(player)==4:
                        score+=100
                if window.count(player)==3 and window.count(0)==1:
                        score+=5
                if window.count(player)==2 and window.count(0)==2:
                        score+=2
                if window.count(opp)==3 and window.count(0)==1:
                        score-=4
                
                
                return score

        def fakeDrop(self,board:list,position:list,col:int,player:int):
                row=position[col]
                board[row][col]=player

        def printBoard(self):
                print('this round')
                for x in self.board:
                        print(x)

        def validateWin(self,player):
                
                #horizental

                for r in range(6):
                        for c in range(4):
                                if self.board[r][c]==player and self.board[r][c+1]==player and self.board[r][c+2]==player and self.board[r][c+3]==player:
                                        print('Player '+str(player)+' win at horizental')
                                        self.gg=True
                                        return True

                for r in range(3):
                        for c in range(7):
                                if self.board[r][c]==player and self.board[r+1][c]==player and self.board[r+2][c]==player and self.board[r+3][c]==player:
                                        print('Player '+str(player)+' win at vertical')
                                        self.gg=True
                                        return True

                for r in range(3):
                        for c in range(4):
                                if self.board[r][c]==player and self.board[r+1][c+1]==player and self.board[r+2][c+2]==player and self.board[r+3][c+3]==player:
                                        print('Player '+str(player)+' win at d1')
                                        self.gg=True
                                        return True

                for r in range(3,6):
                        for c in range(4):
                                if self.board[r][c]==player and self.board[r-1][c+1]==player and self.board[r-2][c+2]==player and self.board[r-3][c+3]==player:
                                        print('Player '+str(player)+' win at d2')
                                        self.gg=True
                                        return True
                print('Player '+str(player)+' no win')
                return False
                        
        def getBoard(self):
                res=self.board.copy()
                return res
        def getLimit(self):
                return self.limit

        def randomDrop(self,player:int):
                drops=self.availableCols()
                self.drop(random.choice(drops),player)

        def availableCols(self):
                res=[]
                for i in range(len(self.limit)):
                        if self.limit[i]>=0:
                                res.append(i)
                return res

        def isGame(self):
                return self.gg

        def minimax(board, depth, alpha, beta, maximizingPlayer):
                valid_locations = get_valid_locations(board)
                is_terminal = is_terminal_node(board)
                if depth == 0 or is_terminal:
                        if is_terminal:
                                if winning_move(board, AI_PIECE):
                                        return (None, 100000000000000)
                                elif winning_move(board, PLAYER_PIECE):
                                        return (None, -10000000000000)
                                else: # Game is over, no more valid moves
                                        return (None, 0)
                        else: # Depth is zero
                                return (None, score_position(board, AI_PIECE))
                if maximizingPlayer:
                        value = -math.inf
                        column = random.choice(valid_locations)
                        for col in valid_locations:
                                row = get_next_open_row(board, col)
                                b_copy = board.copy()
                                drop_piece(b_copy, row, col, AI_PIECE)
                                new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
                                if new_score > value:
                                        value = new_score
                                        column = col
                                alpha = max(alpha, value)
                                if alpha >= beta:
                                        break
                        return column, value

                else: # Minimizing player
                        value = math.inf
                        column = random.choice(valid_locations)
                        for col in valid_locations:
                                row = get_next_open_row(board, col)
                                b_copy = board.copy()
                                drop_piece(b_copy, row, col, PLAYER_PIECE)
                                new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
                                if new_score < value:
                                        value = new_score
                                        column = col
                                beta = min(beta, value)
                                if alpha >= beta:
                                        break
                        return column, value


                
import collections
g=Game()
p=1
steps=collections.defaultdict(int)
while not g.isGame() and len(g.availableCols())>0:
        g.randomDrop(p)
        g.validateWin(p)
        g.printBoard()
        steps[p]+=1
        print(steps)
        if p==1:
                p=2
        else:
                p=1

# p=1

# for i in range(4):
#         res=g.drop(3,p)
#         if res:
#                 g.validateWin(p)
#                 g.printBoard()
#                 g.positionScore(g.getBoard(),p)
#         else:
#                 print('cant play in this col any more')

# board=g.getBoard()
# fakeboard=board.copy()
# g.fakeDrop(fakeboard,g.getLimit(),0,1)
# print(fakeboard)
# p=1
# while not g.isGame() and len(g.availableCols())>0:
#         if p==1:
#                 g.randomDrop(p)
#                 g.validateWin(p)
#                 p=2
#                 g.printBoard()
#         else:
#                 curboard=copy.deepcopy(g.getBoard())
#                 print(curboard)
#                 mv=-1
#                 c=random.choice(g.availableCols())

#                 for col in g.availableCols():
#                         fakeboard=copy.deepcopy(curboard)
#                         g.fakeDrop(fakeboard,g.getLimit(),col,p)
#                         score=g.positionScore(fakeboard,p)
#                         if score>mv:
#                                 mv=score
#                                 c=col
#                 print(c)
#                 g.drop(c,p)

#                 g.validateWin(p)
#                 p=1
#                 g.printBoard()


        