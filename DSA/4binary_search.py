# binary search :-
l=[3,7,11,12,17,18,23,27,29]
search_emt = int(input("enter search element: "))
n=len(l)
start = 0
end= n-1
while(start <= end):
    middle = (start + end )//2
    if(search_emt < l[middle]):
        end = middle -1
    elif(search_emt > l[middle]):
        start = middle +1
    else:
        print("element found at index: ", middle)
        break


