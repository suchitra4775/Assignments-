def Add(addfruit):
    addfruit.append('cheri')
    print('append Method:',addfruit)

def display_list(display_listfruit):
    display_listfruit.display(fruits)
    print('display method:',display_listfruit)

def delete(deletefruit):
    delete_fruit = input('enter the delete fruit:')
    deletefruit.remove(delete_fruit)
    print('remove Method:',deletefruit)

def change(changefruit):
    changefruit = input('enter the update fruit:')
    changefruit ={'grapesa'}
    changefruit.update(changefruit)
    print('Updates method:',changefruit)
    
def main():
    fruits = ['mango','banana','apple']
    print('Fruits Available:',fruits)
    Add(fruits)
    delete(fruits)
    change(fruits)

if __name__=="__main__":
     main()

