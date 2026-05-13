def first_last_occur(nums,target):
    n = len(nums)-1
    start = 0
    end = n-1
    first = -1
    last = -1
    while(start <= end):
        mid = start + ((end-start)//2)
        if(nums[mid] == target):
            first = mid
            end = mid - 1
        elif(nums[mid] < target):
            start = mid + 1
        else:
            end = mid - 1
    start = 0
    end = n-1
    while(start <= end):
        mid = start + ((end-start)//2)
        if(nums[mid] == target):
            last = mid
            start = mid + 1
        elif(nums[mid] < target):
            start = mid + 1
        else:
            end = mid - 1
    return [first,last]
nums = [5,7,7,8,8,10]
target = 8
print(first_last_occur(nums,target))
