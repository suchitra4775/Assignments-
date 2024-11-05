#variable length argument it is one of the features of function
#which allows any number of argument
#type 1 => non-keyword argument (*)
#type 2=> keyword argument(**)

# def additon(*values):
#     sum = 0
#     for numbers in values:
#         sum = sum + numbers
#     return sum

# def multiplication(*values):
#     mul = 1
#     for numbers in values:
#         mul = mul * numbers
#     return mul

# def subtraction(*values):
#     sub = 1
#     for numbers in values:
#         sub = sub - numbers
#     return sub


# def main():
#     ans = additon(1,2,3,4)
#     print('Addition = ',ans)

#     ans = multiplication(12,5)
#     print('multiplication =',ans)

    
#     ans = subtraction(12,5)
#     print('subtraction =',ans)

# if __name__=="__main__":
#     main()

def my_func(part1,part2,*args):
    print("the first parameter = ",part1)
    print("the second parameter= ",part2)
    for i in args:
        print(i)

my_func("let","us","study","python","today")

#keywors Arguments
def my_keyword_func(**kasturi):
    print("keyword arguments = ",kasturi)

my_keyword_func(a_key="python",b_key="django",c_key="java")

def my_function(*args,**kasturi):
    print("non-keyword arguments = ",args)
    print("keyword argument = ",kasturi)

my_function("python","java",a_key=23,b_key=44,c_key=55)

