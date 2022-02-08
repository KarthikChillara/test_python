s = input("Enter the string :")
print(s[::])
r = (s[::-1])
print(s[::-1])

if r == s:
    print("It is palindrome")
else:
    print("It is not palindrome")
