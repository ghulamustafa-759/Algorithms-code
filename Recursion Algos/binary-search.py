#iterative binary search
#hard coded list

def binary_itr(arr,start,end,target):
    while start <= end:
        mid = (start+end)//2

        if arr[mid] < target:
            start = mid +1 
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid
    return start

arr = [2,5,8,10,16,22,24]
target = 10

result = binary_itr(arr, 0, len(arr)- 1, target)
print(f"Target is present at index {result}")


#dynamic/runtime


import random
def ite_bin(arrr, startt, endd, targett):
    while startt <= endd:
        midl = (startt+endd)//2 
        if arrr[midl] < targett:
            startt = midl + 1
        elif arrr[midl] > targett:
            endd = midl - 1
        else:
            return midl
    return startt

lis = []
for i in range(1,26):
    lis.append(i)
    
print(lis)

targett = random.randint(0,26)
print(f"Target is {targett}")

resultt = ite_bin(lis, 0, len(lis)-1, targett)

print(f"Target is present at index {resultt}")