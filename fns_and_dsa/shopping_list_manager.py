def display_menu():
    """Fuction to display available menu, return nothing"""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Function to add, remove or return the item in a cart"""
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            choice_input = input("Enter the item to add: ")
            shopping_list.append(choice_input)
        elif choice == '2':
            choice_input = input("Enter the item to remove: ")
            shopping_list.remove(choice_input)
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
