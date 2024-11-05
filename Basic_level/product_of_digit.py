number = int(input('enter the product of digit:'))
sum = 0 
while(number!=0):
    digit = number % 10
    sum = sum + digit
    number = number //10
print("product of the digit:",sum)