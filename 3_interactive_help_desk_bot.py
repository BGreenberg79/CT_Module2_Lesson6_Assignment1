#Task 1 Command Parser

def tech_support_bot():
    global bot_activate
    bot_activate = input("How can I assist you today?: ").lower()
    if "help" in bot_activate:
        print("Certainly, help is on the way!")
    elif "issue" in bot_activate:
        print("I can find someone to assist you with your issue!")
    elif "contact support" in bot_activate:
        print("Thank you for reaching out to technical support, allow us to find somone who may assist you.")
    else:
        print("I'm sorry we could not identify the challenge you are experiencing, allow me to find an agent who can be of better assistance.")

tech_support_bot()

#Task 2 Issue Categorizer

def issue_ticket():
    global bot_activate
    if "issue" in bot_activate:
        issue_category = input("What type of issue are you experiencing so we can quickly find you appropriate support?: ").lower()
        if "login" == issue_category or "log in" == issue_category or "log-in" == issue_category:
            print("issue category: login".title())
        elif "performance" == issue_category:
            print("issue category: performance".title())
        elif "error" == issue_category:
            print("issue category: error".title())
        else:
            print("No keyword identified".title())
issue_ticket()

'''
The key to this assignment was making the input from the function in Task 1 global in both that function, tech_support_bot(), and
the task 2 function issue_ticket(). I was careful in the inputs taken from both functions to be case sensitive by making both lower case conversions.
I used an if/elif/else chain in the tech_support_bot function to evaluate if any of the keywords identified in the task wre in the user input and used in statements to catch the keyword in a bigger request.
When I went to task 2 and wanted to apply a similar logic to task 1 I was getting a logic error where the ticket printed would list both login and performance issues or login and error issues.
This might be happening because I used an or statement in line 23 to catch a user entering login with a space or hyphen. When this started producing an error I switched the syntax to == (evaluate to)
as Task 2 just asked for categorization and print a ticket for support instead of catching if a predefined command is in a larger response.
After defining each function I called both to ensure they both worked properly.
'''