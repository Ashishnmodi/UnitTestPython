import numpy as np
def arr_pos(k,*args):
    if len(args) == 1:
        args = args[0]
    if type(args) not in [list,tuple]:
        raise TypeError("Please enter in List or Tuple only")
    ls = list(args)
    for i in range(len(ls)):
        if ls[i] < 0:
            raise ValueError("Please Enter Positive Numbers only as part of array")
    if k <= 0:
        raise ValueError("Please Enter Positive Non Zero Number only")
    elif k > len(ls):
        raise ValueError("Entered value is more than length of array")
    arr = np.array(ls)
    summ=[sum(arr[i:i+k]) for i in range(len(arr)) if i < (len(arr)-2)]
    return max(summ)

if __name__=="__main__":
    max_val=arr_pos(2,(3,4,5,6,7,8,9))
    print(max_val)