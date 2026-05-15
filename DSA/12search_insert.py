def search_insert(arr,target):
    n=len(arr)
    start = 0
    end= n-1
    result = n
    while(start<=end):
        mid = start +((end-start)//2)
        if(arr[mid] == target):
            result = mid
            break
        elif(arr[mid]>target):
            result = mid
            end = mid - 1   
        else:
            start = mid + 1
    return result


arr= [1,4,6,8,10,14,16,18]
target = 170
print(search_insert(arr,target)) 