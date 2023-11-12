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


# ---------------------------------- Option 1 -------------------------------------------
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


# This is created to remove repetition. I am taking two parameters in this function that are used to display different
# descriptions based on the ran code
# This will be O(N) since it depends on the len of the open_tabs
def getUserInput(action_description, options_description):
    user_input = None
    if len(open_tabs) == 1:
        user_input = input(f"There is only one tab open at index 0\ntype 0 to {action_description}: ")
    elif len(open_tabs) == 0:
        print("There are 0 open tabs\n")
    else:
        user_input = input(f"there are {len(open_tabs)} open tabs {options_description}: ")
    return user_input


# ---------------------------------- Option 2 -------------------------------------------
# This function will remove a tab after specifying the index
# This function will be O(N) since everything is O(1) except for the pop which
# When removing an element and then shifting every other element making it O(N)
def closeTab():
    # if the open tabs were 1 then it will print remove it in the action description and the rest is what will be
    # printed in the options description if the len of the open_tabs were more than 1 and remove it won't be used
    user_input = getUserInput("remove it", f"what index you want to remove from 0 -> {len(open_tabs) - 1}")

    if user_input is not None and user_input.isdigit():
        tab_index = int(user_input)
        if 0 <= tab_index < len(open_tabs):
            print(f"Removing tab at index {tab_index} \n")
            open_tabs.pop(tab_index)
        else:
            print("Index out of range, removing last index ")
            open_tabs.pop(-1)
    else:
        print("Invalid input or no tabs to close, try again \n")


# ---------------------------------- Option 3 -------------------------------------------
# This will print the HTML of the url that you specify depending on the index
# It is O(N) since it depends on the open_tabs of the user
def switchTab():
    user_input = getUserInput("display its HTML code",
                              f"what index you want to display its HTML from 0 -> {len(open_tabs) - 1}")
    # if it is a digit and not None since if it is None it means that the user entered something other than a digit,
    # and it remained None, so it will run the below
    if user_input is not None and user_input.isdigit():
        tab_index = int(user_input)

        if 0 <= tab_index < len(open_tabs):
            url = open_tabs[tab_index]["url"]
        else:
            print("Invalid index. Using the last index \n")
            url = open_tabs[-1]["url"]
    elif user_input == "":
        url = open_tabs[-1]["url"]
    else:
        print("Invalid input or no tabs to display, try again \n")
        return
    # if the response is 200 so working then it will print the HTML
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
        # This will print the status code if it was other than 200
        else:
            print(f"Web page failed to open, Reason: {response.status_code}")
    # this catches any errors that might occur since the user might type a random website link that doesn't work
    except requests.RequestException as e:
        print(f"Error in: {e}\n")


# ---------------------------------- Option 4 -------------------------------------------
# This function will display all the tabs that are open as well as all nested tabs that are present
# This is of time complexity O(N) since there is a for loop and will depend on the users input
def displayAllTabs():
    if len(open_tabs) > 0:
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
    else:
        print("There are no tabs open\n")


# ---------------------------------- Option 5 -------------------------------------------
# This will choose the index of a tab and make a nested tab inside of it
# This will be of time complexity O(1) since it is mostly if else statements
def openNestedTab():
    print(f"there are {len(open_tabs)} open tabs\n")
    if len(open_tabs) > 0:
        user_input = input("Enter index of tab starting from 0: ")

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
                    print(f"\nAdded a new tab at index {tab_index}\n")

                # If the url doesn't contain https:// this will print
                else:
                    print("Invalid URL. Make sure that the URL starts with https:// \n")
            # If the index was more than the len of the list this will print
            else:
                print("Invalid index \n")
        # If the user entered a string and not a digit this will print
        else:
            print("Wrong input, not a number \n")


# ---------------------------------- Option 6 -------------------------------------------
# This is O(1) since it is only removing all the elements in open_tabs
def clearAllTabs():
    open_tabs.clear()
    print("All tabs cleared")


# Used to remove repetition in the below two functions and to get the file name and path from the user
def fileNamePath():
    file_name = input("Enter file name: ")
    # im getting the name of the file then checking if the user already entered .json if yes then removing it
    if file_name.endswith(".json"):
        file_name = file_name.replace(".json", "")
    # get the path that the user wants to enter
    file_path = input("Enter file path: ")
    full_path = f"{file_path}\{file_name}.json"
    return full_path


# ---------------------------------- Option 7 -------------------------------------------
# got some of the code from the following link added some more modification to it from my side:
# https://ioflood.com/blog/python-write-json-to-file/
# The time complexity of this is based on what I researched it is O(N) since the .dump will depend on the number
# of open tabs hence this time complexity
def saveTab():
    if len(open_tabs) > 0:
        full_path = fileNamePath()
        try:
            # Adding the file path along with the name to create a .json file at the desired location with the
            # desired name
            with open(full_path, "w") as f:
                # this is what is being used to export it as json
                json.dump(open_tabs, f, indent=4)
            print(f"Tabs exported as JSON file.\n")
        except (ValueError, PermissionError) as e:
            print(f"error in the following:\n{e}")
    else:
        print("There are no open tabs.\n")


# ---------------------------------- Option 8 -------------------------------------------
# link for this is
# https://ioflood.com/blog/read-json-file-python/
# Same as the above it is O(N) since it depends on the amount that is getting read from the file
# This will get a json file from what the user specifies location and will be added to the open_tabs
def importTabs():
    full_path = fileNamePath()

    try:
        with open(full_path, "r") as f:
            load_json = json.load(f)
        print("Tabs successfully imported.\n")
        # .extend is used in case the user already entered some information so that they will be added to what he
        # already typed
        return open_tabs.extend(load_json)
    except (ValueError, FileNotFoundError) as e:
        print(f"Error in the following: \n{e}\n")
        return None


# ---------------------------------- Option 9 -------------------------------------------
# This will exit the program
def exitProgram():
    print("Closing program")
    exit()


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
        elif choice == "9":
            exitProgram()


main()
