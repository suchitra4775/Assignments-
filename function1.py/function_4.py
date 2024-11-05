def Areaofcircle(Radius,PI=3.14):
    Result = PI*Radius*Radius
    return Result

def FullName(fname,lname):
    print('first arguments:',fname)
    print('second arguments:',lname)
    print(fname+' '+lname)

def main():
    FullName('kasturi','chaware') #positional -> sequence
    FullName('Chaware','Kasturi') # positional
    FullName(fname='Shreya',lname='Bagde')#Keyword Arguments
    FullName(lname='Bagde',fname='Prajakta')#Keyword Arguments

    Rvalue = 10
    Pivalue = 3.14
    Output_1 = Areaofcircle(Rvalue,Pivalue) #3.14*10*10
    print('Positional Argument:',Output_1)
    Output_2 = Areaofcircle(Pivalue,Rvalue) #Radius=Pivalue Rvalue=PI 3.14*3.14*10
    print('Positional Argument:',Output_2)
    Output_3 = Areaofcircle(Rvalue)
    print('first -Positional Argument and second -default argument:',Output_3)

    Output_1 = Areaofcircle(PI=Pivalue,Radius=Rvalue) 
    print('Keyword Argument:',Output_1)
    Output_1 = Areaofcircle(Radius=Rvalue) 
    print('first Keyword Argument and second default argument:',Output_1)


if __name__ =="__main__":
    main()