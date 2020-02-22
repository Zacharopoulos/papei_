num = int(input("Enter a number"))
result = 0

while num>9:
    num = num*3
    num = num+1
    digit = num%10
    result = result + digit
    num=num//10
