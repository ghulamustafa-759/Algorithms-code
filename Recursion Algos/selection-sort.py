
def selection_sort(arr):
    for i in range(0,len(arr)-1): #last will be sorted automatically
        cur_min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[cur_min]:
                cur_min = j
        arr[i] , arr[cur_min] = arr[cur_min], arr[i] 
    

arr = [2,10,34,22,4,3]

selection_sort(arr)
print(arr)