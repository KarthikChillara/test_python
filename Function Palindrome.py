def Palind():
    return


s = input("Enter the string :")
print(s[::])
Palind()
r = s[::-1]
print(s[::-1])
Palind()
if r == s:
    print("It is Palindrome")
    Palind()
else:
    print("It is not Palindrome")
    Palind()
