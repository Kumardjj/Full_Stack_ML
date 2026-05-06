#bubble sort :- it is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.
lst = [7,4,8,5,3]
n=len(lst)
for i in range(0,n-1):
    for j in range(0, n-i-1):
        if(lst[j+1]<lst[j]):
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)

# time complexity :- the time complexity of bubble sort is O(n^2) in the worst and average cases, and O(n) in the best case when the list is already sorted. This is because in the worst and average cases, the algorithm needs to compare each element with every other element, resulting in n*(n-1)/2 comparisons. In the best case, the algorithm only needs to make one pass through the list to confirm that it is already sorted.

# space complexity :- the space complexity of bubble sort is O(1) because it only requires a constant amount of additional space to perform the sorting. The algorithm sorts the list in place, meaning it does not require any additional data structures to hold the sorted elements. Therefore, the space complexity is constant.and it is basically the auxiliary space complexity that we are talking about here, which is O(1) for bubble sort.
