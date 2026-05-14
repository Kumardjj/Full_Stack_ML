def search_insert(arr,target):
    n=len(arr)-1
    start = 0
    end= n-1
    result = n+1
    while(start<=end):
        mid = start +((end-start)//2)
        if(arr[mid] == target):
            return mid
        elif(arr[mid]>target):
            end = mid - 1
            result = mid
        else:
            start = mid + 1
    return result


arr= [1,4,6,8,10,14,16,18]
target = 17
print(search_insert(arr,target)) 