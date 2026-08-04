class Stack:
    def __init__(self):
        self.stack = []

    def insert_push(self, item):
        self.stack.append(item)
        print(item, "pushed into stack")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is Empty, Nothing to Pop")
            return None
        else:
            return self.stack.pop()

    def display(self):
        print("Stack elements are:", self.stack)


s = Stack()

while True:
    print("""
    1. Push
    2. Pop
    3. Display
    4. Exit
    """)

    choice = int(input("Enter an option: "))

    if choice == 1:
        item = input("Enter item to push: ")
        s.insert_push(item)

    elif choice == 2:
        popped = s.pop()
        if popped is not None:
            print("Popped element:", popped)

    elif choice == 3:
        s.display()

    elif choice == 4:
        print("Exit")
        break

    else:
        print("Invalid choice")