# Functions:


def verif_name(myName, list_users):
    # verify if name exists in dictionary
    while True:
        if myName.lower() in list_users:
            opcion = input(f"Bienvenido {myName.capitalize()}, elije una de las opciones\n 1- Listar datos guardados\n 2- Salir:\n > ")
            if opcion == "1":
                print(list_users[myName.lower()])
            elif opcion == "2":
                print("cya later")
                print("What is your name?")  # ask for their name
                myName = verif_name(input("> "), list_users)
        else:
            return myName.lower()


# This program says hello and asks for my name.
list_users = {'jorge': ['44', 'blue'], 'raul': ['47', 'red']}
while True:
    print("Hello world!")
    print("What is your name?")  # ask for their name
    myName = verif_name(input("> "), list_users)

    print("It is good to meet you, " + myName)
    print("The length of your name is:")
    print(len(myName))
    print("What is your age?")  # ask for their age
    myAge = input("> ")
    print("You will be " + str(int(myAge) + 1) + " in a year.")
    list_users[myName] = [myAge]

    # Optional: Add another item to the list, like favorite color
    print("What is your favorite color?")  # Ask for their favorite color
    favorite_color = input("> ")

    # Add data to the dictionary
    if myName not in list_users:
        list_users[myName] = [myAge]  # Create a new list with the age
    list_users[myName].append(favorite_color)  # Add favorite color to the list

    option = input("Continue? (leave blank and press ENTER to exit) > ")
    if option == "":
        print("cya later")
        break
print(list_users)
