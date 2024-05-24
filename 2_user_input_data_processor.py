#Task 1 Input Length Validator

def length_validator():
    while True:
        first_name = input("Please enter your first name: ")
        if len(first_name) < 2:
            print("Error: Name's are traditionally longer than a single character")
            continue
        else:
            first_name_length = len(first_name)
            break
    while True:
        last_name = input("Please enter your last name: ")
        if len(last_name) < 2:
            print("Error: Name's are traditionally longer than a single character")
            continue
        else:
            last_name_length = len(last_name)
            break
    return last_name_length + first_name_length

print("Your name is", str(length_validator()), "characters long")

'''
I stored my name length checker in a function called length validator. I used a user input within a while loop, instead of globally
so that it would continue to ask for an acceptable name until one of a valid length was given. If there wasn't a name requiement I could have had the input outside of the function
and passed those inputs through the function as arguments matched to parameters. I then formatted the output inside a print statement as I
used return to end my function. I converted my function output back to string inside that print statement to ensure that python does not return an integer.
'''

#Task 2 Password complexity check

def password_validator():
    while True:
        password = input("What is your password?: ")
        upper_case_letters = []
        lower_case_letters = []
        digits = []
        for letter in password:
            if letter.isupper():
                upper_case_letters.append(letter)
            if letter.islower():
                lower_case_letters.append(letter)
            if letter.isdigit():
                digits.append(letter)
        if len(upper_case_letters) == 0:
            print("Your password needs at least one upper case letter, please try again")
            continue
        if len(lower_case_letters) == 0:
            print("Your password needs at least one lower case letter, please try again")
            continue
        if len(digits) == 0:
            print("Your password needs at least one number, please try again")
            continue
        if len(password) < 8:
            print("Your password must be at least 8 characters long, please try again")
            continue
        else:
            break
    return password

print("Your password is ", password_validator())

'''
In this function I'm running fur separate if tests to check if it is a valid password.
I am checking if the length of the password is over 8 characters and if inside those 8 characters
there is at least one each of a lower case letter, upper case letter, and digit.
As the isupper, isdigit, and islower functions only work on strings and not lists I
ran those booleans and appended them to empty appropriately named lists based off of which test
was passed. If one of our 4 criterias was not met an appropriate error message was printed and a continue
statement was executed to get a new attempt. If all four tests passed the while loop where the input was housed
is broken and the fucntion returns the user input password. I then call that function alongside a print statement that says what the password is.
'''
#Task3 Email formatter

def email_input(username, domain_name):
    email_template = "{}@{}"
    email_address = email_template.format(username, domain_name)
    print("Your email address is", email_address)

username_input = input("What is your username: ").lower()
domain_name_input = input("What domain do you use (i.e. gmail.com, yahoo.com): ").lower()
email_input(username_input, domain_name_input)

'''
When thinking about the approach to this question I initially was going to index the last three characters
to ensure the top level domain was in an appropriate format but then I realized the list of acceptable domain names
has expanded past the traditional 3 letter .com's, .edu's, .org's, and .net's of years past
I did not want a user getting an error message for inputting say a .io email address.
Thus I used no test for validity and just took two inputs globally, one for username, and one for domain name and fed that as arguments into a function
that formatted those two pieces of information into an email address where they are split by the appropriate @ symbol.
I accomplished this with a user template variable that used {} as placeholders until the .format() built in function
filled them out with our users input. I also made both user inputs .lower() as urls and email addresses are not case sensitive
'''
