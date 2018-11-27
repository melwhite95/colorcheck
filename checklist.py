
# list() is a method that can be called to store list items
check_list = []


check_list.append('Blue')
print(check_list)
check_list.append('Orange')
print(check_list)


def create(item):
    check_list.append(item)


def read(index):
    return check_list[index]


check_list = ['Hello', 'World']
check_list[1] = 'Cats'
check_list.pop(1)
print(check_list)


def update(index, item):
    check_list[index] = item


def destroy(index):
    check_list.pop(index)


def list_all_items():
    for list_item in check_list:
        print("{} {}".format(index, list_item))
        index += 1


def mark_completed(index):
    check_list.append(index)


def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our       program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")
        return True


def user_input(prompt):
    user_input = input(prompt)
    return user_input


running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list")
    runnning = select(selection)


check_list('Check')


def test():
    create('purple sox')
    create('res cloak')

    print(read(0))
    print(read(1))

    update(0,  'purple socks')
    destroy(1)
    select('C')
    list_all_items()
    select('R')
    list_all_items()
    print(read(0))
    print(read(1))
    list_all_items()
    user_value = user_input("Please enter a value:")
    print(user_value)


print(test())
