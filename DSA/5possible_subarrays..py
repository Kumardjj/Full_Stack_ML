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
