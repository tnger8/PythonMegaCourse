while True:
    user_action = input("Type add, show, complete, edit or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)


        case 'show' | 'display':

            with open("todos.txt", 'r') as file:
                file.readlines()

            new_todos = []

            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)

            for index, item in enumerate(new_todos):
                row = f"{index}-{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit : "))
            number = number - 1

            with open("todos.txt", 'r') as file:
                todos = file.readlines()
            print('Here is the todos existing', todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo to complete:  "))

            with open("todos.txt", 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)
            with open("todos.txt", 'w') as file:
                file.writelines(todos)

            message = f"To do {todo_to_remove} was removed from the list."
            print(message)

        case 'exit':
            break
        case _:
            print("Invalid command!")

print("Bye")
