def binary(arr):        #Function to search an element
    """ Funtion that searches the element the user wants to search"""
    element = int(input("Enter the number to seach: "))
    low = 0
    high = len(arr)-1

    while low<= high:
        mid = (low+high)//2
        guess = arr[mid]
        if guess == element:
            return "Number Found!"
        elif guess > element:
            high = mid - 1
        else:
            low = mid+1
    else:
        return "Element not found!"

def insert_elements():                      #A function for inserting elements into a list for searching
    """Function takes the user input of numbers for storing them in a list"""
    arr_elements = int(input("Enter the number of elements you want to enter in the array: "))

    container = []
    for i in range(arr_elements):
        container.append(int(input(f"Enter the element at index[{i}]: ")))

    return container

def extend_list():
    """ For extending the list if the list is present otherwise it just extends the original list """
    arr_elements = int(input("Enter the number of elements you want to extend the array: "))

    container = []
    for i in range(arr_elements):
        container.append(int(input(f"Enter the element at index[{i}]: ")))

    return container

def main():                                 #Main  Functionn that gives different options to the user

    my_list=[]

    while True:
        print("\nThe Operations present in the program")
        print("1. Search")
        print("2. Inserting Elements")
        print("3. Extend the elements in the list")
        print("4. list of elements")
        print("5. Exit")
    
        choice = input("Enter the choice: ")

        match choice:
            case '1':
                if not my_list:
                    print("Enter the elements first by choosing the 2 option")
                else:
                    my_list.sort()
                    print(binary(my_list))
            case '2':
                my_list=insert_elements()
            case '3':
                if not my_list:
                    my_list = insert_elements()
                else:
                    my_list.extend(extend_list())
            case '4':
                print(f"The Elements inside the list are:{my_list}")
            case '5':
                print("Exiting the program. Goodbye!")
                break
            case '_':
                print("Invalid Number! Enter (1,2 or 3)")


main()                                      #Calling Main() for running the program
