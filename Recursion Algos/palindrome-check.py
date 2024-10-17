#12321

no = input("Enter the number you want to check for palindrome : ")
x = str(no)
y = str(no)[::-1]

if x == y:
    print(f"The number {no} is palindrome")
else:
    print("The number is not palindrome")