#positional and keyword Argument
# def FullName(fname,lname):
#     print('first arguments:',fname)
#     print('second argrument:',lname)
#     print(fname+' '+lname)

# def main():
#     FullName('suchitra','Dhakane')#positional sequence
#     FullName('dhakane','suchitra')
#     FullName(fname='suchitra',lname='dhakane') #keyword Argument
#     FullName(lname='dhakane',fname='suchitra')
# if __name__=="__main__":
    # main()

# example of positional
# def Areaofcircle(Radius,PI=3.14):
#     Result = 2*PI*Radius*Radius
#     return Result

# def main():
#     Rvalue = 10
#     Pivalue = 3.14
#     Output_1 = Areaofcircle(Rvalue,Pivalue)
#     print('positional Aregument:',Output_1)
#     Output_2 = Areaofcircle(Pivalue,Rvalue)
#     print('positional Aregument:',Output_2)
#     Output_3 = Areaofcircle(Rvalue)
#     print('first -Positional Argument and second -default argument:',Output_3)
# if __name__=="__main__":
#     main()

# def volumeOfCylinder(Radius,height,PI=3.14):
#     Result = 2*PI*Radius*Radius*height
#     return Result

# def main():
#     Rvalue = 10
#     Pivalue = 3.14
#     height = 15
#     Output_1 = volumeOfCylinder(Rvalue,Pivalue,height)
#     print('positional Aregument:',Output_1)
#     Output_2 = volumeOfCylinder(Pivalue,height,Rvalue)
#     print('positional Argument:',Output_2)
#     Output_3 = volumeOfCylinder(Rvalue,height)
#     print('fisrt and second -positional argument and third -default argument:',Output_3)
#  

# if __name__=="__main__":
#     main()

# def circle(Radius,square,PI=3.14):
#     Result = PI*Radius,square
#     return Result

# def main():
#     Pivalue =3.14
#     Radius = 10
#     square = 8
#     Output_1 = circle(Pivalue,Radius,square)
#     print('positional Argument:',Output_1)
#     Output_2 = circle(Radius,square,Pivalue)
#     print('positional Argument:',Output_2)
#     Output_3 = circle(Radius,square)
#     print('fisrt and second -positional argument and third -default argument:',Output_3)

# if __name__=="__main__":
#     main()

def Areaofcircle(Radius,PI=3.14):
    Result = 2*Radius*Radius*PI
    return  Result

def main():
    Pivalue = 3.14
    Rvalue = 10
    Output_1 = Areaofcircle(Pivalue,Rvalue)
    print('positional Argument:',Output_1)
    Output_2 = Areaofcircle(Rvalue,Pivalue)
    print('positinal Argument:',Output_2)
    Output_3 = Areaofcircle(Rvalue)
    print('first -positional argument and second -default argument:',Output_3)

if __name__=="__main__":
    main()

