from typing import List
class Solution:
        def evalRPN(self,tokens:List[str])->int:
                q=[]
                for token in tokens:
                        if token not in "+-*/":
                                q.append(int(token))
                        else:
                                r,l=q.pop(),q.pop()
                                if token=="+":
                                        q.append(l+r)
                                elif token=='-':
                                        q.append(l-r)
                                elif token=='*':
                                        q.append(l*r)
                                else:
                                        q.append(int(float(l)/r))
                return q[-1]