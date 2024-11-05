import os
import filecmp

def Comparefile(fileName1,fileName2):
    if (not os.path.exists(fileName1)):
        print('file not exist:',fileName1)
    elif  (not os.path.exists(fileName2)):
        print('file not exist:',fileName2)
    else:
        compare = filecmp.cmp(fileName1,fileName2)
        if compare == True:
            print('files are same')
        else:
            print('files are different')
def main():
    file1 = input('enter first file')
    file2 = input('enter second file')
    Comparefile(file1,file2)

if __name__=="__main__":
    main()

