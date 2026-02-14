
def binary(arr):        #Function to search an element
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

def insert_elements():                      #A functio for inserting elements into a list for searching
    arr_elements = int(input("Enter the number of elements you want to enter in the array: "))

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
        print("3. list of elements")
        print("4. Exit")
    
        choice = input("Enter the choice between(1,2,3 or 4): ")

        match choice:
            case '1':
                if not my_list:
                    print("Enter the elements first by choosing the 2 option")
                else:
                    print(binary(my_list))
            case '2':
                my_list=insert_elements()
            case '3':
                print(f"The list of elements are:{my_list}")
            case '4':
                print("Exiting the program. Goodbye!")
                break
            case '_':
                print("Invalid Number! Enter (1,2 or 3)")


main()                                      #Calling Main() for running the program
