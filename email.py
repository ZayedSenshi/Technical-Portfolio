# Define class with constructor outlining attributes (data).
class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False  # Default value as False
        self.inbox = []

    # Method to mark email as read.
    def mark_as_read(self):
        self.has_been_read = True

    # Method to automatically add emails to inbox.
    def populate_inbox(self):
        # Clear inbox before populating it to avoid duplicates.
        self.inbox = []
        # Store sample emails using dictionaries within a list.
        sample_emails = [
            {"email_address": "sampleone@example.com",
             "subject_line": "Welcome to Hyperion Dev!",
             "email_content": "Have you enjoyed my code?"},
            {"email_address": "sampletwo@example.com",
             "subject_line": "Great work on the bootcamp!",
             "email_content": "This is hard, but I'm enjoying it!"},
            {"email_address": "samplethree@example.com",
             "subject_line": "Your excellent marks!",
             "email_content": "Please leave a detailed review :)"}
        ]
        # iterate over sample_emails and store in a list. Append to inbox.
        for email_details in sample_emails:
            new_email = Email(email_details["email_address"],
                              email_details["subject_line"],
                              email_details["email_content"])
            self.inbox.append(new_email)

    # Method to list index and emails by iterating through inbox.
    def list_emails(self):
        print("\033[1m" + "Your emails are listed below: " + "\033[0m")
        for index, email in enumerate(self.inbox):
            # Specify that within the emails, subject_line needs to be printed.
            print(index, email.subject_line)

    # Method to allow user to read emails. While loop handles exceptions/errors.
    def read_email(self):
        while True:
            try:
                user_input = input("Please choose an email to read by entering 0"
                                   ", 1 or 2, or 'r' to return to the main menu: ")
                if user_input.lower() == 'r':
                    break
                # isdigit() crucial for checking user_input, allowing elif block to execute
                elif user_input.isdigit() and 0 <= int(user_input) < len(self.inbox):
                    # Local variable to store the email selected, sifting through inbox depending on user_input.
                    selected_email = self.inbox[int(user_input)]
                    print(f"Email Address: {selected_email.email_address}")
                    print(f"Subject Line: {selected_email.subject_line}")
                    print(f"Email Content: {selected_email.email_content}")
                    # Once printed, the selected email is marked as read by calling on the method.
                    selected_email.mark_as_read()
                    print(f"\nEmail from {selected_email.email_address} has now been marked as read.\n")
                else:
                    print("Invalid option. Please choose 0, 1, 2 or 'r' to return to the main menu.")
            except ValueError:
                print("Please ensure you enter: 0, 1, 2, or 'r'")

    # Method to calculate unread emails.
    def list_unread_email(self):
        # List comprehension iterates through inbox to check if emails have not been read.
        unread_emails = [email for email in self.inbox if not email.has_been_read]
        # 'if not' checks if unread_emails is empty meaning there are no unread emails.
        if not unread_emails:
            print("You have no unread emails")
        # If unread emails is not empty, it prints the unread emails.
        else:
            print("\033[1m" + "Your unread emails are listed below: " + "\033[0m")
            for index, email in enumerate(unread_emails):
                print(index, email.subject_line)


# Instance object to execute methods.
start_up = Email("start_up@email.com",
                 "email_running",
                 "Allows the program to run ")
start_up.populate_inbox()

# User menu utilises while loop to manage options and handle errors/exceptions.
menu = True
while menu:
    try:
        user_choice = int(input(f''' Would you like to: 
        1. Read an email
        2. View unread emails
        3. Quit application
        
        Enter selection: '''))

        if user_choice == 1:
            start_up.list_emails()
            start_up.read_email()

        elif user_choice == 2:
            start_up.list_unread_email()

        elif user_choice == 3:
            print("Exiting application")
            menu = False
        else:
            print("Oops - incorrect input. Try again")
    except ValueError:
        print("Ensure you enter '1', '2' or '3'.")
