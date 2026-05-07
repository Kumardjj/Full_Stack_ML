# Selection sort :- it is a simple sorting algorithm. It works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and swapping it with the first unsorted element until the entire list is sorted.
lst = [3,4,1,2,6] 
n=len(lst)
for i in range(0,n-1):
    min_index=i
    for j in range(i+1,n):
        if(lst[j]<lst[min_index]):
            min_index=j
    lst[i],lst[min_index]=lst[min_index],lst[i]
print(lst)


# time complexity :- so when we calculate the time complexity of selection sort, we can see that it has two nested loops. The outer loop runs n-1 times, and the inner loop runs n-i-1 times. Therefore, the total number of comparisons made by selection sort is (n-1) + (n-2) + ... + 1 + 0, which is equal to n(n-1)/2. This gives us a time complexity of O(n^2) for selection sort.

# space complexity :- the space complexity of selection sort is O(1) because it only requires a constant amount of additional space to perform the sorting. The algorithm sorts the list in place, meaning it does not require any additional data structures to hold the sorted elements. Therefore, the space complexity is constant.and it is basically the auxiliary space complexity that we are talking about here, which is O(1) for selection sort.
