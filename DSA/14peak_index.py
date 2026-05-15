def peak_index(arr):
    n = len(arr) 
    start = 0
    end = n -1
    result = 0
    while(start <= end):
        mid = start +(end -start)//2
        if((arr[mid] > arr[mid-1]) and  (arr[mid] > arr[mid+1])):
            result = mid
            break
        elif(arr[mid] > arr[mid-1]):
            start = mid + 1
        else:
            end = mid - 1
    return arr[result]

arr= [2,4,5,8,10,11,8,5]
print(peak_index(arr))
