
def StrIndexFinder(st,subst):
    if st == None or subst == None:
        raise AttributeError("String is not valid")
    if type(st) not in [str] or type(subst) not in [str]:
        raise AttributeError("Arguments should be a string not integer or float")
    #print(type(st),type(subst))
    return st.find(subst)

if __name__=="__main__":
    res=StrIndexFinder('Hello','ll')
    print(res)