def subarrays(l,n):
    for st in range(n):
        for end in range(st,n):
            for i in range ( st, end+1):
                print(l[i],end="")
            print(end=" ")
        print()

l=[1,2,3,4,5]
n=len(l)
subarrays(l,n)

# output:- 
# 1 12 123 1234 12345 
# 2 23 234 2345 
# 3 34 345 
# 4 45 
# 5 