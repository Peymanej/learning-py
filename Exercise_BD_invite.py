#Getting names from user:

confirmation = False
names = []
count = 0
print ('\nSay me which ones of your friends do you like to invite to your birthday?')

while confirmation == False:

    invite = True

    while invite:

        name = input ('\nPlease enter your friend\'s name: ')
        if name.lower () == 'quit' or name.lower () == 'no one' or name.lower () == 'end':
            invite = False

        else:
            names.append (name.title ())
            count += 1
            print (f'\n{count} - {name.title ()} is now in the invitation list!'\
                   '\nIs there any other friend to invite?\nIf not please type '\
                   'END.')


# Showing the final list to you after edit:
    if len (names) == 0 :
        print ('\nYou entered no one in the list!\n')
        restart_ = input ('Do you want to restart? \nY/N: ')
        if restart_.lower () not in ('yes', 'y'):
            confirmation = True
            break
        else:
            conf_validation = True        
    
    else:
        conf_validation = False
        print ('\nThe list of  your friends is:\n')

        for name in names:
            print ((names.index (name) + 1), '-', name)

# Final list confirmation:

    if conf_validation != True :  
        user_conf = input ('\nDo you confirm the list as final to invite?\n')
        
        while conf_validation == False:
            # The list is the final list!
            if user_conf.lower () == 'yes' or user_conf.lower () == 'y' :
                print ('\nThe final list of  your friends is:\n')
                conf_validation = True

                for name in names:
                    print (names.index (name) + 1 ,'-', name)
                    confirmation = True

            # The list needs to be modified
            elif user_conf.lower () in ('no', 'n'):
                
                action_ = 0
            
                while action_ not in range (1, 5):
                    print ('\nIt seems you need to modify the list!\nWhat do you need to do?\n'\
                        ' 1- I want to add another friend to the list.\n'\
                        ' 2- I want to remove one or more!\n'\
                        ' 3- I want to correct/edit one of the names!\n'\
                        ' 4- The list is OK! I confirm it.\n')

                    action_ = int (input ('Please select between 1 to 4:\n'))

                    if action_ == 1:
                        conf_validation = True
                        invite = True

                    elif action_ == 2:

                        len_count = len (names)
                    
                        while len_count  > 0:
                            print ('\nThe list of  your friends is:\n')

                            for name in names:
                                print (names.index (name) + 1 ,'-', name)
                            
                            print ((names.index (name)) + 2, '-', 'Dont remove anyone!\n') #type: ignore

                            del_ = (int (input ('Please enter the number of your choice: ')) - 1)

                            if del_ > (len (names)):
                                del_ = (int (input (f'\nPlease enter the number of your choice less than {(len (names) + 2)}: ')) - 1)
                            
                            if (del_) == (len (names)):
                                print ('\nNow your list is:')
                                for name in names:
                                    print (names.index (name) + 1 ,'-', name)
                                len_count = 0
                                action_ = 0
                            
                            else:
                                
                                answer_ = input (f'Are you sure you want to remove {names[del_]} frome list?\nY/N: ')
                                
                                while answer_ not in ('Y', 'y', 'N', 'n', (names.index (name) + 2)): #type: ignore
                                        print ('\nYour answer is not valid!\nPlease answer with YES or No:')
                                        answer_ = input (f'Are you sure you want to remove {names[del_]} frome list?\nY/N: ')


                                if answer_ in ('Y', 'y') :

                                    print (f'{names[del_]} is removed from the list!')

                                    del names [del_]

                                    len_count = len (names)

                                    cont_ = input ('\nDo you want to remove another one?\nY/N: ')

                                    while cont_ not in ('Y', 'y', 'N', 'n'):
                                        print ('\nYour answer is not valid!\nPlease answer with Y or N:')
                                        cont_ = input ('\nDo you want to remove another one?\nY/N: ')

                                    if cont_ in ('Y', 'y') :
                                        continue
                                    
                                    else:
                                        len_count = 0
                                        action_ = 0

                    elif action_ == 3:
                    
                        len_count = len (names) #type: ignore
                    
                        while len_count  > 0:
                            print ('\nThe list of  your friends is:\n')

                            for name in names:
                                print (names.index (name) + 1 ,'-', name)
                            
                            print ((names.index (name)) + 2, '-', 'Dont change anyone!\n') #type: ignore

                            edit_ = (int (input ('Please enter the number of your choice: ')) - 1)

                            if edit_ > (len (names)):
                                edit_ = (int (input (f'\nPlease enter the number of your choice less than {(len (names) + 2)}: ')) - 1)
                            
                            if (edit_) == (len (names)):
                                print ('\nNow your list is:')
                                for name in names:
                                    print (names.index (name) + 1 ,'-', name)
                                len_count = 0
                                action_ = 0

                            else:
                                
                                answer_ = input (f'Are you sure you want to change {names[edit_]} in the list?\nY/N: ')
                                
                                while answer_ not in ('Y', 'y', 'N', 'n', (names.index (name) + 2)): #type: ignore
                                        print ('\nYour answer is not valid!\nPlease answer with YES or No:')
                                        answer_ = input (f'Are you sure you want to change {names[edit_]} in the list?\nY/N: ')

                                if answer_ in ('Y', 'y') :

                                    edited_name = input ('\nPlease enter the substitute!')
                                    edited_name = edited_name.title ()
                                    print (f'\n{names[edit_]} is substituted with {edited_name} in the list!')

                                    names [edit_] = edited_name

                                    len_count = len (names)

                                    cont_ = input ('\nDo you want to edit/change another one?\nY/N: ')

                                    while cont_ not in ('Y', 'y', 'N', 'n'):
                                        print ('\nYour answer is not valid!\nPlease answer with Y or N:')
                                        cont_ = input ('\nDo you want to change/edit another one?\nY/N: ')

                                    if cont_ in ('Y', 'y') :
                                        continue
                                    
                                    else:
                                        len_count = 0
                                        action_ = 0

                    else:
                        
                        print ('\nThe final list of  your friends is:\n')
                        conf_validation = True

                        for name in names:
                            print (names.index (name) + 1 ,'-', name)
                            confirmation = True

            else:

                print ('\nThe final list of  your friends is:\n')
                conf_validation = True

                for name in names:
                    print (names.index (name) + 1 ,'-', name)
                    confirmation = True


if len (names) == 0:
    print ('\nYou have invited no one!\n')

elif len (names) == 1:
    print ('\nYou have invited just one person!\nThe list completed\n')
   
else:
    print (f'\nYou have invited {len (names)} people.\nThe list completed\n') 

# Celebration organizing:
    # Confirmatiopn by user:
organizing_celebration = input ('Happy birthday!'\
       '\nDo you need help to organize the celebration?')
while organizing_celebration.lower() not in ('yes', 'y', 'n', 'no'):
    organizing_celebration = input ('Please answer with "Yes" or "No"!')

    # User doesnt want to organize it now:
if organizing_celebration.lower() in ('no', 'n') :
    print ('Good Luck!')
    # User wants to get help:
else :
    # Asking needed information for invitation message!
    print ('Please define the time you are going to celebrate:')
    month = input ('Type the month: ')
    day = input ('Type the day: ')
    time = input ('Which time of the day the  celebration starts? ')
    celeb_location = input ('Please write the address of the location: ')
    celeb_date = (month, day, time)

    host_name = input ('whats the name of the host? ')

    # Writing invitation message to guests:
    for name in names :
        print (f'Dear {name}\nYou are invited to {host_name}\'s birthday celabration!\nThe adress is: {celeb_location}\n'\
               f'Date: {day} of {month} at {time}')
    # Asking guests information for hosting
    drinks = ['Soft', 'Alcoholic', 'water']
    foods = ['Pizza', 'Hamburger', 'Pasta']
    guest_info = {}
    for name in names:
        print ('The list of drinks is:\n')
        for drink in drinks:
            print (f'{drinks.index (drink) + 1} - {drink}' ) #type: ignore
        fav_drink = int (input (f'What is {name}\'s favourite drink? '))
        while fav_drink - 1 not in range (0, 3):
            fav_drink = int (input ('Answer is not valid!\nPlease enter the number assigned to the drink: '))
        guest_info[f'{name}'] = drinks[fav_drink - 1]        
    for a, d in guest_info.items():
        print (f'{a.title()} likes to drink: {d}')

    for a in guest_info.keys() :
        print (f'{a} likes to drink {guest_info[a]}!')
    
    


