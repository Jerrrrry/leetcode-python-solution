class Solution:
        def cal(self,s:str)->int:
                if not s:
                        return 0
                q,num,o=[],0,'+'
                for i in range(len(s)):
                        if s[i].isdigit():
                                num=num*10+ord(s[i])-ord('0')
                        if (not s[i].isdigit() and not s[i].isspace()) or i==len(s)-1:
                                if o=="+":
                                        q.append(num)
                                elif o=="-":
                                        q.append(-num)
                                elif o=="*":
                                        q.append(q.pop()*num)
                                else:
                                        q.append(int(q.pop()/num))
                                o=s[i]
                                num=0
                return sum(q)