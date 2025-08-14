# Password Strength Analyzer
# Implement a function called analyze_password that evaluates the strength of a given password based on multiple criteria. The function should:
# Accept a password string as input.
# Return a dictionary containing:
#   length: length of the password
#   has_upper: boolean indicating uppercase letters presence
#   has_lower: boolean indicating lowercase letters presence
#   has_digit: boolean indicating digits presence
#   has_special: boolean indicating special characters presence
#   strength_score: integer score (0-5) based on met criteria
#   suggestions: list of improvement tips
# Additional Challenges (for more training):
# Add parameter min_length with default value 8
# Implement recursive checking for common password patterns
# Add a helper function to generate random strong passwords
# Create a decorator to time the password checking process
# Add type hints to the function signature
# Write docstrings following Python conventions

# Pass Request
def password_analyzer(password: str):
    """The function recieves a password and evaluates it based on containing:
     - upper case letters
     - lower case letters
     - digits
     - special characters
     - whitespaces
     - at least 8 characters
     it returns three values:
        1- A dictinary whit keys and values as:
            Has Upper case': boolean,
            'Has lower case': boolean,
            'Has digit': boolean,
            'Has Special': boolean,
            'Strength Scor': int
        2- The entered password (str)
        3- Suggestion to improve the password strength  """
    get_pass = 0
    while  get_pass == 0:
        print ("Please create a password of at least 8 characters, containing:\n"\
        "1- At least one upper case letter\n"\
        "2- At least one lower case letter\n"\
        "3- At least one digit\n"\
        "4- At least one special character\n"\
        "5- Any white spaces\n\n" )
        pass_ = input ("Enter your password: \n")
        if len (pass_) < 8 :
            print ("\nYou must enter at least 8 characters!\n")
        else:
            #White space check
            wht_ = 0
            while wht_ == 0 :
                if any (ch.isspace () for ch in pass_) :
                        print ("\nYour pass is not valid! Because it contains white space!\n")
                        wht_ = 1
                if wht_ == 0 :
                    get_pass = 1
                    wht_ = 1
            
    upper_count = 0
    lower_count = 0
    digit_count = 0
    special_count = 0  
    pass_score = 0

# Pass Evaluation
    for ch in pass_ :
        if ch.isdigit () :
            digit_count += 1
            has_digit = True
        elif not ch.isalnum () :
            special_count += 1
            has_special = True
        else:
            if ch == ch.upper () :
                upper_count += 1
                has_upper = True

            if ch == ch.lower () :
                lower_count += 1
                has_lower = True


#Strength Score Calculation
    suggestions = {"title": '\nTo improve your Password strength: '}
    if len (pass_) == 8 :
        suggestions ['Length issue:'] = 'More than 8 characters is suggested!'
    elif 8 < len (pass_) <= 10 :
        pass_score += 1
        suggestions ['Length issue:'] = "It's nice! But more than 10 characters is suggested!"
    else:
        pass_score += 1

    if upper_count > 0 :
        pass_score += 1
        has_upper = True
        
    else:
        has_upper = False
        suggestions ["upper issue"] = "Your password needs at least 1 upper case letter!"
    
    if lower_count > 0 :
        pass_score +=1
        has_lower = True
    else:
        has_lower = False
        suggestions ["lower issue"] = "Your password needs at least 1 lower case letter!"
    
    if special_count > 0 :
        pass_score += 1
        has_special = True
    else:
        has_special = False
        suggestions ["special issue"] = "Your password needs at least 1 special character!"

    if digit_count >0 :
        pass_score +=1
        has_digit = True
    else:
        has_digit = False
        suggestions ["digit issue"] = "Your password needs at least 1 digit!"

    pass_res = {
    'Has Upper case': has_upper,
    'Has lower case': has_lower,
    'Has digit': has_digit,
    'Has Special': has_special,
    'Strength Scor': pass_score
    }
    
    return {pass_res,
            pass_,
            suggestions
    }


pass_test = password_analyzer (password)

print ('\nYour Password is: ', passt)

for key, value in pass_test.items ():
    print (f"\n{key}: {value}")

if len (sugg) > 1 :
    for key, value in sugg.items ():
        print (f"\n {value}")
else:
    print ("\nGreat! Your password passed all tests and is very strong!")