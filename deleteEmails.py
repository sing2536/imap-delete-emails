# install Python: https://www.python.org/downloads/

import imaplib
import getpass

# Number of emails to delete
while True:
        number_of_emails_to_delete = int(input("Enter the amount of emails to delete (can't be more than 1000): "))
        if number_of_emails_to_delete < 1:
             print("Number of emails should be greater than 1. Please enter a valid value.")
        elif number_of_emails_to_delete > 1000:
            print("Number of emails exceeds the limit. Please enter a value less than or equal to 1000.")
        else:
            break

# IMAP server details
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

print("Please be patient as this can take a while, you will be advised when the process completes.")

def delete_emails():


    # Connect to the IMAP server
    imap_connection = imaplib.IMAP4_SSL("imap.telstra.com", 993)
    imap_connection.login(username, password)

    # Select the mailbox/folder you want to delete emails from
    imap_connection.select("INBOX")

    # Search for the most recent emails
    _, message_numbers = imap_connection.search(None, "ALL")
    message_numbers = message_numbers[0].split()

    # Determine the range of emails to delete
    range_start = 0
    range_end = min(number_of_emails_to_delete, len(message_numbers))

    # Delete each email within the specified range
    for i in range(range_start, range_end):
        imap_connection.store(message_numbers[i], "+FLAGS", "\\Deleted")

    # Permanently delete the marked emails
    imap_connection.expunge()

    # Disconnect from the IMAP server
    imap_connection.logout()
    print(f"{number_of_emails_to_delete} emails deleted successfully.")

# Loop to delete emails
while True:
    delete_emails()

    choice = input(f"Do you want to delete {number_of_emails_to_delete} more emails? (y/n): ")
    if choice.lower() != "y":
        break
