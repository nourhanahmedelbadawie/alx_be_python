def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

shopping_list = []

def main():
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            shopping_list.append(input('Enter you item: '))
            pass
        elif choice == '2':
             item = input('Enter you item: ')
             if item  in shopping_list:
              shopping_list.remove(item)

             else: print(' check you name of item')
             pass
        elif choice == '3':
            # Display the shopping list
            for x in shopping_list:
             print(x)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

display_menu()

main()
