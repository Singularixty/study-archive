things_todo = []

list = input("List #1 (e to exit): ")

while list.lower() != "e" :
    things_todo.append(list)
    todo_length = len(things_todo)
    list = input(f"List #{todo_length+1} (e to exit): ")
else:
    print("\nYour todo list:")
    for _, item in enumerate(things_todo):
        print(f"#{_+1}: {item}")