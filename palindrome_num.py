num = (input("Enter a number:"))
reverse = ""
for i in num:
    reverse = i + reverse
if num == reverse:
    print(num,"this number is palindrome")
else:
    print(num,"is not a palindrome")
