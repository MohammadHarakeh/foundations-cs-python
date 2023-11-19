def menu():
    print("1. Singly Linked List")
    print("2. Check if Palindrome")
    print("3. Priority Queue")
    print("4. Evaluate an Infix Expression")
    print("5. Graph")
    print("6. Exit")


def singlyLinkedListMenu():
    print("a. Add Node")
    print("b. Display Nodes")
    print("c. Search for & Delete Node")
    print("d. Return to main menu")


class Node:

    def __init__(self, info):
        self.info = info
        self.next = None


class singlyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, info):
        new_node = Node(info)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def addNodeUserInput(self):
        user_input = int(input("Enter number: "))
        if user_input == -999:
            return self.displayNodes()
        else:
            self.addNode(user_input)
            self.displayNodes()
            self.addNodeUserInput()  # Recursive call to add another node

    def displayNodes(self):
        current = self.head
        while current != None:
            print(current.info, end=" ")
            current = current.next
        print("Current List: ")
        print()


def main():
    menu()
    ll = singlyLinkedList()

    node1 = Node(20)
    node2 = Node(10)
    node3 = Node(15)
    node4 = Node(7)

    ll.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    choice = input("\nEnter choice 1 -> 6: ")

    if choice == "1":
        singlyLinkedListMenu()
        sub_choice = input("\nEnter choice a -> d: ")
        if sub_choice == "a":
            ll.addNodeUserInput()
        elif sub_choice == "b":
            ll.displayNodes()


main()
