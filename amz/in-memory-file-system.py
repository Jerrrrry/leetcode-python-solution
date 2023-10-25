class fs:
        def __init__(self):
                self.data={}

        def ls(self,path:str)->List[str]:
                ps=path.split('/')
                tmp=self.data
                for p in ps:
                        if p:
                                if p not in tmp:
                                        tmp[p]={}
                                tmp=tmp[p]

                if '$' in tmp:
                        return ps[-1]
                else:
                        return sorted(tmp.keys())

        def mkdir(self,path:str)->None:
                ps=path.split('/')
                tmp=self.data
                for p in ps:
                        if p:
                                if p not in tmp