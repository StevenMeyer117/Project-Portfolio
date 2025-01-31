# Hacking the Fender Project Description

# The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret
# passwords including your own. Your mission, should you choose to accept it, is threefold. You must acquire access to
# The Fender‘s systems, you must update his "passwords.csv" file to scramble the secret data. The last thing you need to
# do is add the signature of Slash Null, a different hacker whose nefarious deeds could be very conveniently halted by
# The Fender if they viewed Slash Null as a threat.

# Use your knowledge of working with Python files to retrieve, manipulate, obscure, and create data in your quest for
# justice. Work with CSV files and other text files in this exploration of the strength of Python file programming.


# Import the CSV and JSON modules
import csv
import json

# Create list of users who's passwords have been compromised
compromised_users = []

# Open 'passwords' CSV file. Pass 'password_file' object holder to CSV reader for parsing. Save each row to temp var
# and add each username to compromised users list
with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for password_row in password_csv:
        compromised_users.append(password_row['Username'])

# Open file 'compromised_users.txt' in write-mode and write username of each user in new file
with open('compromised_users.txt', 'w') as compromised_user_file:
    for compromised_user in compromised_users:
        compromised_user_file.write(compromised_user)


# Notify boss with encoded message in JSON
with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
    json.dump(boss_message_dict, boss_message)

# Remove passwords.csv by creating new passwords file with Slash Null's signature
with open('new_passwords.csv', 'w') as new_passwords_obj:
    slash_null_sig = """ 
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
    new_passwords_obj.write(slash_null_sig)