# square root of a fucntion.
def square_root(n):
    start = 1
    end = n
    store = -1
    while(start <= end):
        mid = start + ((end-start)//2)
        if(mid == (n//mid)):
            store = mid
            break
        elif(mid > (n//mid)):
            end = mid -1
        else:
            store = mid
            start = mid + 1 
    return store    
target = 120
print(square_root(target))
