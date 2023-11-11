import requests

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


# This function is only used to have the user enter his name
def userName():
    name = input("Enter your name: ")
    print(f"Hello {name} what would you like to do: ")
    print()


# This will ask the user for title and url that will be stored in tab storage that is outside the function so that
# the items won't get deleted
def openTab():
    tab_dic = {}

    while True:
        title = input("Enter the title of the website: ")
        url = input("Enter the URL of the website: ")

        if url.startswith("https://"):
            tab_dic["title"] = title
            tab_dic["url"] = url
            break
        else:
            print("Invalid URL. Make sure that the URL starts with https://")

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
    print()

    if user_input.isdigit():
        tab_index = int(user_input)

        if 0 <= tab_index < len(open_tabs):
            # this chunk of code is from the following reference
            # https://opensource.com/article/21/9/web-scraping-python-beautiful-soup
            url = open_tabs[tab_index]["url"]
        else:
            print("Invalid index. Using the last index")
            print()
            url = open_tabs[-1]["url"]
    elif user_input == "":
        url = open_tabs[-1]["url"]
    else:
        print("Invalid input. Using the last index.")
        print()
        url = open_tabs[-1]["url"]

    # I'm using the try except in this case if the user enters a https:// with a random string then it won't
    # exit the code because of an error but then show what the error is
    try:
        response = requests.get(url)
        # Check if the URL is valid based on the response 200 means that it is valid so proceed
        if response.status_code == 200:
            print(response.text)
        else:
            print(f"Web page failed to open, Reason: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error in: {e}")


def displayAllTabs():
    print("Titles of all open tabs are: ")
    for items in open_tabs:
        print(items["title"])
    print()


def openNestedTab():
    user_input = input("Enter index of tab: ")

    nested_tab = {}
    while True:
        title = input("Enter the title of the website: ")
        url = input("Enter the URL of the website: ")

        if url.startswith("https://"):
            nested_tab["title"] = title
            nested_tab["url"] = url
            break
        else:
            print("Invalid URL. Make sure that the URL starts with https://")


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
        elif choice == "4":
            displayAllTabs()
        elif choice == "5":
            openNestedTab()


main()
