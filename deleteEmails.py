# windows install: https://www.python.org/downloads/windows/

import imaplib
import getpass

# Number of emails to delete
number_of_emails_to_delete = int(input("Enter amount of emails to delete (more than 1000 may cause issues): "))

# IMAP server details
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

print("Please be patient, this can take a while, and you will be advised when the process completes.")

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

    choice = input("Do you want to delete more emails again1? (y/n): ")
    if choice.lower() != "y":
        break
