
Number = int(input("Enter the number:"))
for i in range(2,Number//2):
    if Number%i==0:
            print('number is prime')
else:
            print('number is not prime')   