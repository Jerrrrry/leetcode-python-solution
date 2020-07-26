def minRemoveToMakeValid(self,s:str)->str:
    remove=set()
    stack=[]

    for i,c in enumerate(s):
        if c not in "()":
            continue
        if c=="(":
            stack.append(i)
        elif not stack:
            remove.add(i)
        else:
            stack.pop()
    remove=remove.union(set(stack))
    builder=[]
    for i,c in enumerate(s):
        if i not in remove:
            builder.append(c)
    return "".join(builder)