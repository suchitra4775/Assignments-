#Positional and keyword Argument
def FullName(fname,lname):
    print('first arguments:',fname)
    print('second arguments:',lname)
    print(fname+' '+lname)

def main():
    FullName('kasturi','chaware') #positional -> sequence
    FullName('Chaware','Kasturi') # positional
    FullName(fname='Shreya',lname='Bagde')#Keyword Arguments
    FullName(lname='Bagde',fname='Prajakta')#Keyword Arguments
#Subtraction 
if __name__=="__main__": #1 True
    main()

