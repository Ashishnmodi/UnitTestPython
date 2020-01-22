#Factor Table
def factors(num):
    fact=[]
    if num==0:
        raise ValueError("Every Integer is factor of 0")
    elif num<0:
        for i in range(num,0):
            if num%(i)==0:
                fact.append(i)
            else:
                continue
        return fact
    else:
        for i in range(num):
            if num%(i+1)==0:
                fact.append(i+1)
            else:
                continue
        return fact

if __name__ =="__main__":
    fact1=factors(4)
    print(fact1)