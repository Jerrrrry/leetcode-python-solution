import re
class File:
    def __init__(self,name,size,type,isDirectory,files):
        self.name=name
        self.size=size
        self.type=type
        self.isDirectory=isDirectory
        self.files=files

    def getName(self):
        return self.name
    def getSize(self):
        return self.size
    def getType(self):
        return self.type
    def getIsdirectory(self):
        return self.isDirectory
    def getFiles(self):
        return self.files

class Filter:
    def apply(self,file):
        if not isinstance(file,File):
            raise TypeError

class SearchFilter(Filter):
    def __init__(self,seachstring):
        self.searchstring=seachstring

    def apply(self,file):
        super().apply(file)
        pattern='.*'+self.searchstring+'.*'
        res=re.search(pattern,file.getName())
        if res==None:
            return False
        else:
            return True

class TypeFilter(Filter):
    def __init__(self,type):
        self.type=type
    def apply(self,file):
        super().apply(file)
        if self.type!=file.getType():
            return False
        else:
            return True

class SizeFilter(Filter):
    def __init__(self,size):
        self.size=size

    def apply(self,file):
        super().apply(file)
        if file.getSize()>self.size:
            return False
        else:
            return True

class FindCommand:
    def find_all(self, curr_dir, filters):
        all_files = []
        if curr_dir.getIsdirectory():
            for file in curr_dir.files:
                if file.getIsdirectory():
                    all_files += self.find_all(file, filters)
                else:
                    score=0
                    for filter in filters:
                        if filter.apply(file):
                            score+=1
                    if score==len(filters):
                        all_files.append(file.getName())

        else:
            score=0
            for filter in filters:
                if filter.apply(curr_dir):
                    score+=1
            if score==len(filters):
                all_files.append(curr_dir.getName())
        return all_files

f=File('yubinqiu_runbook.py',600,'script',False,[])
f2=File('yubinqiu_runbook2.py',600,'python',False,[])
f3=File('yubinqiu_runbook3.py',800,'bash',False,[])
f1=File('yubinqiu',600,None,True,[f2,f3])
test=File('test',600,'folder',True,[f,f1])

cmd=FindCommand()
fa=SearchFilter('py')
fb=TypeFilter('bash')
fc=SizeFilter(1000)
print(cmd.find_all(test,[fa,fb,fc]))

    


