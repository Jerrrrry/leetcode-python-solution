class Solutuion:
        def isMatch(self,s:str,p:str)->bool:
                if not s:
                        return not p
                reg=""

                for c in p:
                        if c=='.':
                                reg+='[a-z]'
                        elif 'a'<=c<='z':
                                reg+='['+c+']'
                        else:
                                reg+=c

                return re.match('^'+reg+'$',s)