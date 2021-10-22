import random
import string

password = []


#This loop stops the program from shutting down when done if it is run outside a code editor
while True:
    #Makes it so that the code reruns if and Error occurs
    while True:
        #Asks the user if they want letters in their password.
        dyw_ABC = input('Do you want your password to contain letters? y/n :')
        if dyw_ABC == 'y':
            #Asks the user how many lower/uppercase letters the password should contain.
            amount_ABC_upper = int(input('How many lowercase letters should the password contain? :'))
            amount_ABC_lower = int(input('How many uppercase letters should the password contain? :'))  
                
            #Adds the lowercase letter to the password if it was choosen
            for i in range(amount_ABC_lower):
                the_letters_lower = random.choice(string.ascii_lowercase)
                password.append(the_letters_lower)

            #Adds the uppercase letter to the password if it was choosen
            for i in range(amount_ABC_upper):
                the_letters_upper = random.choice(string.ascii_uppercase)
                password.append(the_letters_upper)
            break

        elif dyw_ABC == 'n':
            print('Ok! No letters will be added.')
            break

        #Error message
        else:
            print('ERROR! You can only type y or n, anything else will result in this error message.')
            print('-----------------------')

    print('-----------------------')
#Code Divider --------------------------------------------------------------------------------------------------------------------------

    #Makes it so that the code reruns if and Error occurs
    while True:
        #Asks the user if they want numbers in their password
        dyw_123 = input('Do you want your password to contain numbers 1-9? y/n :')
        if dyw_123 == 'y':
            #Asks the user how many letters the password should contain.
            amount_123 = int(input('How many numbers should the password contain? :'))
            
            #Adds the numbers to the password
            for i in range(amount_123):
                the_numbers = random.randint(0, 9)
                password.append(the_numbers)
            break
            
        elif dyw_123 == 'n':
            print('Ok! No letters will be added.')
            break

        #Error message
        else:
            print('ERROR! You can only type y or n, anything else will result in this error message.')
            print('-----------------------')

    print('-----------------------')
#Code Divider --------------------------------------------------------------------------------------------------------------------------

    #Makes it so that the code reruns if and Error occurs
    while True:
        #Asks the user if they want ! @ # $ in their password
        dyw_symbol = input('Do you want your password to contain the following symbols?   @ ! $ #   y/n :')
        if dyw_symbol == 'y':
            #Asks the user how many of the aforementioned symbols should be added to the password
            amount_symbol = int(input('How many symbols should the password contain? :'))

            #Adds the symbols to the password
            for i in range(amount_symbol):
                symbol_list = ['@', '!', '$', '#']
                rsta = random.choice(symbol_list)
                password.append(rsta)
            break

        elif dyw_symbol == 'n':
            print('Ok! No symbols will be added.')
            break

        #Error massage
        else:
            print('ERROR! You can only type y or n, anything else will result in this error message.')
            print('-----------------------')

    print('-----------------------')
#Code Divider --------------------------------------------------------------------------------------------------------------------------

    #Makes it so that the code reruns if and Error occurs
    while True:
        #Asks if the user wants to add someyhing to the password
        dyw_special = input('Do you want something specific to be in the password? y/n :')
        
        if dyw_special == 'y':
            #They write want the want to be added here
            special_add = input('Type what you want added to the password here :')
            password.append(special_add)
            break
        
        elif dyw_special == 'n':
            print('Ok! Noting special will be added.')
            break
        
        else:
            #Error message
            print('ERROR! You can only type y or n, anything else will result in this error message.')
            print('-----------------------')

    print('-----------------------')
#Code Divider --------------------------------------------------------------------------------------------------------------------------

    #Shuffles the password list and prints it
    random.shuffle(password)
    print('This is your password  ',*password, sep = '')
    print('-----------------------')

    #Stops the programm
    shutdown = input('Press enter button to shut of the program')
    if shutdown == 0:
        break
    else:
        break