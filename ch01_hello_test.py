# This program says hello and asks for my name.
list_users = {}
while True:
    print('Hello world!')
    print('What is your name?')    # ask for their name
    myName = input()
    # verify if name in dictionary
    if myName in list_users:
        myName = input("Nombre usuario existente, escriba otro: ")
    print('It is good to meet you, ' + myName)
    print('The length of your name is:')
    print(len(myName))
    print('What is your age?')    # ask for their age
    myAge = input()
    print('You will be ' + str(int(myAge) + 1) + ' in a year.')
    list_users[myName] = [myAge]

    # Optional: Add another item to the list, like favorite color
    print('What is your favorite color?')  # Ask for their favorite color
    favorite_color = input()

    # Add data to the dictionary
    if myName not in list_users:
        list_users[myName] = [myAge]  # Create a new list with the age
    list_users[myName].append(favorite_color)  # Add favorite color to the list

    option = input("Continue? (leave blank and press ENTER to exit)")
    if option == "":
        print("cya later")
        break
print(list_users)
