import random
import sys

# Attempt to get file name passed as command line argument
try:
    file_name =  sys.argv[1]
# Raise an error if file name is not provided
except IndexError:
    print("Missing command-line argument.")
    quit()

# Set the domain name for the email addresses
last_email = "@poppleton.ac.uk"

# Try to open and read the file
try:
    with open(file_name,"r") as profile:
        for line in profile:
            # Initialize variables for storing student's last name and email
            last_name = ''
            student_id = line[:7]
            temp_last_name =  line[9:].split(', ')[0]
            first_name = line[9:].split(', ')[1].replace('\n', '')
            
            # Iterate over each character of the last name to get only the capital letters
            for i in temp_last_name.upper():
                if i.isupper():
                    last_name =  last_name + i.lower()
           
            
            # Extract the first letter of each word from the first name
            temp = ''
            for i in first_name.split(" "):
                temp =  temp + i[0].lower() +'.' 
            
            # Generate random number between 1000 and 9999
            random_number = random.randint(1000,9999)  
            
            # Create email address using the student name and random number
            email = temp +  last_name +str(random_number) + last_email
            
            # Open a new file and write the student ID and email address
            with open("email_write.txt",'a+') as ewrite:
                 ewrite.write(student_id + " " + email +"\n")
# Catch the error if file is not found
except FileNotFoundError:
    print(f''' Cannot open "{file_name}". Sorry about that.''')