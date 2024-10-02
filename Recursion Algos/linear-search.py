#linear search
arr = [2,5,8,9,16,22,4,7,3,10]
target = 10

def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
print(search(arr, target))
