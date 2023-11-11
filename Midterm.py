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


# This will ask the user for title and url that will be stored in tab dic that is inside open tabs
# Then tab dic will be stored in a list outside of open_tabs

def openTab():
    tab_dic = {}

    while True:
        title = input("Enter the title of the website: ")
        url = input("Enter the URL of the website: ")

        # This is used to make sure that the url will start will https
        if url.startswith("https://"):
            tab_dic["title"] = title
            tab_dic["url"] = url
            break
        else:
            print("Invalid URL. Make sure that the URL starts with https://")
    open_tabs.append(tab_dic)
    print(f"\nNumber of open tabs are: {len(open_tabs)}")
    print(f"{open_tabs}\n")


# This function will remove a tab after specifying the index
def closeTab():
    user_input = None
    if len(open_tabs) == 1:
        user_input = input("There is only one tab open at index 0\ntype 0 to remove it: ")
    else:
        user_input = input(
            f"there are {len(open_tabs)} open tabs what index you want to remove from 0 -> {len(open_tabs) - 1}:  ")

    # this will make sure that the entered is a digit if not it will then remove the last index
    if user_input.isdigit():
        tab_index = int(user_input)
        # If the input is digit and is between 0 and the len of the list open_tabs then it will pop the index specified
        if 0 <= tab_index < len(open_tabs):
            open_tabs.pop(tab_index)
            print(open_tabs)
            # Else this will run and pop the last index
        else:
            print("Index out of range, removing last index ")
            open_tabs.pop(-1)
            print(open_tabs)
    # this is for the first .isdigit() where if it wasn't a digit then it will print the below.
    else:
        print("Invalid input, try again \n")


# This function will display the HTML code of the website that the user specifies
def switchTab():
    user_input = None
    if len(open_tabs) == 1:
        user_input = input("There is only one tab open at index 0\ntype 0 to display it's HTML code: ")
    else:
        user_input = input(
            f"there are {len(open_tabs)} open tabs what index you want to display it's HTML from 0 -> {len(open_tabs) - 1}:  ")

    if user_input.isdigit():
        tab_index = int(user_input)

        if 0 <= tab_index < len(open_tabs):
            # url will be taken from the list open_tabs specifying the index and taking what is under "url"
            url = open_tabs[tab_index]["url"]
        else:
            # If it was out of range then it will print the url of the last index
            print("Invalid index. Using the last index \n")
            url = open_tabs[-1]["url"]
    # The user doesn't enter anything will still display last index
    elif user_input == "":
        url = open_tabs[-1]["url"]
    else:
        print("Invalid input. Using the last index.\n")
        url = open_tabs[-1]["url"]

    # I'm using the try except in this case if the user enters a https:// with a random string then it won't
    # exit the code because of an error but then show what the error is that is caught in as e
    try:
        # this chunk of code is from the following reference
        # https://opensource.com/article/21/9/web-scraping-python-beautiful-soup
        response = requests.get(url)
        # Check if the URL is valid based on the response 200 means that it is valid so proceed
        if response.status_code == 200:
            print(response.text)
        else:
            # this will display the status code of the website if it failed and is down
            print(f"Web page failed to open, Reason: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error in: {e}")


# This function will display all the tabs that are open as well as all nested tabs that are present
def displayAllTabs():
    print("Titles of all open tabs are: ")
    # used enumerate here to keep track of the index of the title in the current item
    for i, items in enumerate(open_tabs):
        print(f"title {i + 1}: ", items["title"])
        # if items that are in open tabs have the following string then it will print the following /t is used to
        # indicate that it is a nested tab
        if "Nested Tab: " in items:
            nested = items['Nested Tab: ']['title']
            print(f"\tNested Title: {nested}")
    print()


# def tabInfo():
#

# This will choose the index of a tab and make a nested tab inside of it
def openNestedTab():
    user_input = input("Enter index of tab: ")

    # This will make sure it is index same as the above
    if user_input.isdigit():
        tab_index = int(user_input)
        # created a new dictionary names nested tab that will store a new title and url
        nested_tab = {}
        if 0 <= tab_index < len(open_tabs):
            title = input("Enter the title of the website: ")
            url = input("Enter the URL of the website: ")

            if url.startswith("https://"):
                nested_tab["title"] = title
                nested_tab["url"] = url

                open_tabs[tab_index]["Nested Tab: "] = nested_tab
                print(open_tabs)

            # If the url doesn't contain https:// this will print
            else:
                print("Invalid URL. Make sure that the URL starts with https:// \n")
        # If the index was more than the len of the list this will print
        else:
            print("Invalid index \n")
    # If the user entered a string and not a digit this will print
    else:
        print("Wrong input, not a number \n")


# This will contain all the function that I have created and call them depending on the users choice from 1 -> 9
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
