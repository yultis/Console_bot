import re

# Dictionary to store contacts:
contacts = {}

# Decorator to handle input errors:
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return str(e)
    return inner

# Function for cleaning the phone number from extra characters
def sanitize_phone_number(number):
    cleaned_number = number.replace(" ", "").replace("-", "").replace("(", "")
    normalized_number = cleaned_number.replace(")", "").replace("+", "").replace("\n", "").rstrip()
    return normalized_number


# Function to add a contact to the contacts dictionary:
@input_error
def add_contact(name, number):
    formatted_name = name.title()
    sanitized_number = sanitize_phone_number(number)  # Cleaning the phone number before storage
    contacts[formatted_name] = sanitized_number
    return f"Contact '{formatted_name}' added with number '{sanitized_number}'"

# Function to change an existing contact to the contacts dictionary:
@input_error
def change_contact(name, number):
    formatted_name = name.title()
    if formatted_name not in contacts:
        return f"This contact '{formatted_name}' doesn't exist. Please only change existing contacts or create new ones using the 'add' command"
    sanitized_number = sanitize_phone_number(number)  # Cleaning the phone number before storage
    contacts[formatted_name] = sanitized_number
    return f"Number for '{formatted_name}' updated to '{sanitized_number}'"

# Function to get a phone number from the contacts dictionary:
@input_error
def get_phone(name):
    formatted_name = name.title()
    return f"The number for '{formatted_name}' is '{contacts[formatted_name]}'"

# Function to display all contacts in the contacts dictionary:
@input_error
def show_all():
    if not contacts:
        return "No contacts available."
    formatted_contacts = {name.title(): number for name, number in contacts.items()}
    return "\n".join([f"{name}: {number}" for name, number in formatted_contacts.items()])

# Function to handle unknown commands:
@input_error
def unknown_command(action):
    return f"Command '{action}' not recognized."

# Main function to handle user input and commands:
def main():
    while True:
        command = input("Enter command: ").lower().split()
        action = command[0]

        # Handling various commands:
        if action == "hello":
            print("How can I help you?")
        elif action == "add":
            if len(command) >= 3:
                result = add_contact(command[1], command[2])
            else:
                result = "Give me name and phone please"
            print(result)
        elif action == "change":
            if len(command) >= 3:
                result = change_contact(command[1], command[2])
            else:
                result = "Give me name and phone please"
            print(result)
        elif action == "phone":
            if len(command) >= 2:
                result = get_phone(command[1])
            else:
                result = "Enter user name"
            print(result)
        elif len(command) == 1 and re.match(r'^\+?\d+$', action):
            print("Please enter command 'add' or 'change' and after that the name and the phone number")
        elif action == "show" and len(command) > 1 and command[1] == "all":
            print(show_all())
        elif action in ("close", "exit"):
            print("Good bye!")
            break
        elif action == "good" and len(command) > 1 and command[1] == "bye":
            print("Good bye!")
            break
        else:
            print(unknown_command(action))

if __name__ == "__main__":
    main()