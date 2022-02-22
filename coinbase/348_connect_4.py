
import random
class Game:
        def __init__(self,n:int):
                self.r=[0]*n
                self.c=[0]*n
                self.d1=0
                self.d2=0
                self.n=n
                self.ps=[]

                for i in range(n):
                        for j in range(n):
                                self.ps.append((i,j))

        def play(self,s:int):
                num=self.n

                while self.ps:
                        r=random.randrange(0,len(self.ps))
                        step=self.ps[r]
                        self.ps.remove(step)
                        res=self.move(step[0],step[1],s)
                        if res!=0:
                                return res
                        if s==1:
                                s=2
                        else:
                                s=1
                return 0

        
        def move(self,row:int,col:int,player:int):
                if player==1:
                        o=1
                else:
                        o=-1
                
                self.r[row]+=o
                self.c[col]+=o

                if col==row:
                        self.d1+=o
                if col+row==self.n-1:
                        self.d2+=o
                
                d=[self.r[row],self.c[col],self.d1,self.d2]

                if self.n in d or -self.n in d:
                        return player
                return 0

game=Game(6)

print(game.play(1))