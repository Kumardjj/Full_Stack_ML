# # majority element.
# # first appraoch should be brute force approach that if we find frequency of all the element and then will check if frequency of any element would be greater than (n//2--> hald length of array).

# l=[1,2,2,1,1]
# n=len(l)
# for i in l:
#     freq=0
#     for j in l:
#         if(i==j):
#             freq=freq+1
#     if(freq> (n//2)):
#         print(freq)
#         break




# # using dictionary O(n)
# l=[1,2,2,1,1]
# #
# major={}
# for i in l:
#     if(i not in major):
#         major[i]=1
#     else:
#         major[i]=major[i]+1
# print(major)  
# length= len(major)
# for i in major:
#     if(major[i]>length):
#         print(major[i])
#         break

# using sorting.
l=[1,2,2,1,1,3,3,3,3,3,3]
n=len(l)
l.sort()
print(l)
freq=1
ans=l[0]
for i in range(1,n):
    if l[i] == l[i-1] :
        freq=freq+1   
    else:
        freq=1
        ans=l[i]
if freq > (n//2):
    print(freq)