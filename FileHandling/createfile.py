import os
def read_file(fileName): 
    if (os.path.exists(fileName)): 
        fd=open(fileName,'r') 
        data = fd.read() 
        createfile(data)  
        fd.close()
    else:
        print('file not exist')


def createfile(data):
    fd = open('demo.txt','w')
    fd.write(data)
    print('contant copy sucessfully')
    fd.close()

def main():
    print('Enter the file you want to read')
    file = input() 
    read_file(file) 
if __name__=="__main__": 

    main()