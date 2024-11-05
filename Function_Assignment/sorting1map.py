def people(item):
        return sorted # This function is defined but not used in the program. It takes a parameter item and returns the built-in sorted function itself, 
    # which is not meaningful in the current context since it doesn't perform any sorting.
    
    #name_list is created, containing three dictionaries. Each dictionary represents a person with their name, surname, and age.
def main():
    name_list = [
    {'name':'shreya','surname':'kakade','age':15},
    {'name':'pratiksha','surname':'rokde','age':13},
    {'name':'prerna','surname':'munde','age':15}
    ]
    
    sorted_name_list = sorted(name_list, key=lambda x: x['age'])
    print(sorted_name_list) #This line prints the sorted list of dictionaries.

#The sorted() function is used to sort name_list.
# The key parameter is a lambda function: lambda x: x['surname']. This lambda function takes each dictionary x from name_list and extracts the value of the surname key to determine the order of sorting.
# As a result, sorted_name_list will contain the dictionaries sorted in ascending order based on the surname.
    
if __name__=="__main__":
    main()

