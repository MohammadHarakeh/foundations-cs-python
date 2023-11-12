import json

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
    name = input("Enter your name: ").strip()
    print(f"Hello {name} what would you like to do: ")
    print()


# This will ask the user for title and url that will be stored in tab dic that is inside open tabs
# Then tab dic will be stored in a list outside of open_tabs
# This function will be O(N) because of the while loop that is present inside of it
def openTab():
    tab_dic = {}

    while True:
        title = input("Enter the title of the website: ").strip()
        url = input("Enter the URL of the website: ").strip()

        # This is used to make sure that the url will start will https
        if url.startswith("https://") or url.startswith("http://"):
            tab_dic["title"] = title
            tab_dic["url"] = url
            break
        else:
            print("Invalid URL. Make sure that the URL starts with https://")
    open_tabs.append(tab_dic)
    print(f"\nNumber of open tabs are: {len(open_tabs)}")
    for i in range(len(open_tabs)):
        print(open_tabs[i]["title"])
    print()


# This function will remove a tab after specifying the index
# This function will be O(N) since everything is O(1) except for the pop which
# When removing an element and then shifting every other element making it O(N)
def closeTab():
    user_input = None
    if len(open_tabs) == 1:
        user_input = input("There is only one tab open at index 0\ntype 0 to remove it: ")
    elif len(open_tabs) == 0:
        return print("There are 0 open tabs\n")
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
# This is O(1) complexity since it only has if else and only a requests.get("url") but in general it is O(1)
def switchTab():
    user_input = None
    if len(open_tabs) == 1:
        user_input = input("There is only one tab open at index 0\ntype 0 to display it's HTML code: ")
    elif len(open_tabs) == 0:
        return print("There are 0 open tabs\n")
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
        print(f"Error in: {e}\n")


# This function will display all the tabs that are open as well as all nested tabs that are present
# This is of time complexity O(N) since there is a for loop and will depend on the users input
def displayAllTabs():
    print("Titles of all open tabs are: ")
    # used enumerate here to keep track of the index of the title in the current item
    for i, items in enumerate(open_tabs):
        print(f"{i + 1}. ", items["title"])
        # if items that are in open tabs have the following string then it will print the following /t is used to
        # indicate that it is a nested tab
        if "Nested Tab: " in items:
            nested = items['Nested Tab: ']['title']
            print(f"\tNested Title: {nested}")
    print()


# This will choose the index of a tab and make a nested tab inside of it
# This will be of time complexity O(1) since it is mostly if else statements
def openNestedTab():
    user_input = input("Enter index of tab: ")

    # This will make sure it is index same as the above
    if user_input.isdigit():
        tab_index = int(user_input)
        # created a new dictionary names nested tab that will store a new title and url
        nested_tab = {}
        if 0 <= tab_index < len(open_tabs):
            title = input("Enter the title of the website: ").strip()
            url = input("Enter the URL of the website: ").strip()

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


# This is O(1) since it is only removing all the elements in open_tabs
def clearAllTabs():
    open_tabs.clear()
    print("All tabs cleared")


# got some of the code from the following link added some more modification to it from my side:
# https://ioflood.com/blog/python-write-json-to-file/
def saveTab():
    file_name = input("Enter file name: ")

    if file_name.endswith(".json"):
        file_name = file_name.replace(".json", "")

    file_path = input("Enter file path: ")
    try:
        with open(f"{file_path}\{file_name}.json", "w") as f:
            json.dump(open_tabs, f, indent=4)
        print(f"Tabs exported as JSON file.")
    except (ValueError, PermissionError, FileNotFoundError) as e:
        print(f"error in the following:\n{e}")


def importTabs():
    file_name = input("Enter file name: ")

    if file_name.endswith(".json"):
        file_name = file_name.replace(".json", "")
    file_path = input("Enter file path: ")

    try:
        with open(f"{file_path}\{file_name}.json", "r") as f:
            load_json = json.load(f)
        print("Tabs successfully imported.")
        return open_tabs.extend(load_json)
    except (ValueError, FileNotFoundError) as e:
        print(f"Error in the following: \n{e}\n")
        return None


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
        elif choice == "6":
            clearAllTabs()
        elif choice == "7":
            saveTab()
        elif choice == "8":
            importTabs()


main()
