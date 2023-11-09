# This will display the menu that the user can choose from

tab_storage = {}


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


# This will ask the user for title and url that will be stored in tab storage that is outside the function so that the items won't get deleted
def openTab():
    title = input("Enter the title of the website: ")
    url = input("Enter the URL of the website: ")
    # if the title (key) is in tab storage then im adding another url (value) to it else I add one
    if title in tab_storage:
        tab_storage[title].append(url)
    else:
        tab_storage[title] = [url]
    print(tab_storage)
    print()


def main():
    name = input("Enter your name: ")
    print(f"Hello {name} what would you like to do: ")
    print()

    while True:
        menu()
        choice = input("Enter your choice from 1 -> 9: ")
        print()

        if choice == "1":
            openTab()


main()
