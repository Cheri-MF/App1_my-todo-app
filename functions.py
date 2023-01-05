FILEPATH = 'todos.txt'


def get_todo_list(filepath=FILEPATH):
    """ Read a text file and return a list of to-do items """
    with open(filepath, 'r') as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def write_todo_list(to_add, filepath=FILEPATH):
    """ Write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(to_add)


if __name__ == "__main__":
    print("I am inside!")
