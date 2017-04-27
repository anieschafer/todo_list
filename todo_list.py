"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""


my_list = []


def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""

    todo = raw_input ("please type your item or if done type 'done' ")
    if todo == 'done':
        return 
    else:
        my_list.append(todo)
        return my_list

def view_list(my_list):
    """Print each item in the list."""

    for item in my_list:
        print item

def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = raw_input("""
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Quit the program
     """)
    while True:
        if user_options == 'A':
            print add_to_list(my_list)
        elif user_options == 'B':
            print view_list(my_list)
        elif user_options == 'C':
            break
        else: 
            print "please select A B or C"

        user_options = raw_input("""
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Quit the program
     """)
        



        # Collect input and include your if/elif/else statements here.
     

#-------------------------------------------------

my_list = []
display_main_menu(my_list)

