def search_rotated_min(arr):
    n = len(arr)
    start = 0
    end = n-1
    min_emt = arr[0]
    while(start<=end):
        mid = start + ((end - start)//2)
        if (arr[mid] > arr[0]):
            start = mid + 1
        elif(arr[mid] < arr[0]):
            min_emt = arr[mid]
            end = mid -1   
        else:
            min_emt = min(arr[mid],min_emt)
            break
    return min_emt



arr = [8,10,0,1,2,5,6]
print(search_rotated_min(arr))