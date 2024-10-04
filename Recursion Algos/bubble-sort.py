#un-optimized bubble sort
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubble_sor_un_o(A):
    itera = 0

    for i in A:
        for j in range(len(A)-1):
            itera += 1
            if A[j] > A[j+1]:
                swap(A, j, j+1)
    return A, itera

A = [9,8,7,6,5,4,3,2,1]
print(bubble_sor_un_o(A))




#optimized bubble sort
def bubble_sor(a):
    iteration = 0
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            iteration += 1
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1], a[j]
            
    return a, iteration

a = [9,8,7,6,5,4,3,2,1]
print(bubble_sor(a))