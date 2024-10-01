#Last-In-First-Out

#factorial
def iterative_factorial(n):
    fact = 1 #multiplicative identity
    for i in range (2,n+1):
        fact*=i 
    return(fact)

print(iterative_factorial(5))
print("---------------------")


#permutation

def permute(string, pock=""):
    if len(string) == 0:
        print(pock)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter+pock)

print(permute("ABC", ""))