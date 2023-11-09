import requests
from bs4 import BeautifulSoup


open_tabs = []

# This will display the menu that the user can choose from
def menu():
    print("1. Open Tab")
    print("2. Close Tab")
    print("3. Switch Tab")
    print("4. Display All Tabs")
    print("5. Open Nested Tabs")
    print("6. Clear All Tabs")
    print("7. Save Tabs")
    print("8. Import Tabs")
    print("9. Exit")
    print()


def userName():
    name = input("Enter your name: ")
    print(f"Hello {name} what would you like to do: ")
    print()


# This will ask the user for title and url that will be stored in tab storage that is outside the function so that
# the items won't get deleted
def openTab():
    tab_dic = {}
    title = input("Enter the title of the website: ")
    url = input("Enter the URL of the website: ")
    # if the title (key) is in tab storage then im adding another url (value) to it else I add one
    tab_dic["title"] = title
    tab_dic["url"] = url

    open_tabs.append(tab_dic)
    print(open_tabs)
    print()


# This function will remove a tab after specifying the index
def closeTab():
    user_input = input("Enter the index of the tab you want to close: ")
    # this will make sure that the entered is a digit if not it will then remove the last index
    if user_input.isdigit():
        tab_index = int(user_input)
        if 0 <= tab_index < len(open_tabs):
            open_tabs.pop(tab_index)
            print(open_tabs)
        else:
            print("Index out of range, removing last index ")
            open_tabs.pop(-1)
            print(open_tabs)
    # this is for the first .isdigit() where if it wasn't a digit then it will print the below.
    else:
        print("Invalid input, try again")
        print()

def switchTab():
    user_input = input("Enter the index of the tab you want to display: ")
    if user_input.isdigit():
        tab_index = int(user_input)
        if 0 <= tab_index < len(open_tabs):
            response = requests.get()

# This will contain all the function that I have created and call them depending on the users choice
def main():
    userName()

    while True:
        menu()
        choice = input("Enter your choice from 1 -> 9: ")
        print()

        if choice == "1":
            openTab()
        elif choice == "2":
            closeTab()
        elif choice == "3":
            switchTab()


main()
