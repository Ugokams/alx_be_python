from random import choice

shopping_list = []
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    choice = 0
    while choice != 4:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                # Prompt for and add an item
                item = input("Enter item name: ")
                shopping_list.append(item)

            elif choice == 2:
                # Prompt for and remove an item
                item = input("Enter item name: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                else:
                    print("Item not found in the shopping list.")

            elif choice == 3:
                # Display the shopping list
                for item in shopping_list:
                    print(item)
            elif choice == 4:
                print("Goodbye!")
            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

display_menu()
main()