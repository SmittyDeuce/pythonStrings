from random import random, shuffle, choice
# 1. Customer Data Sanitization
# Objective:
# The aim of this assignment is to practice string manipulation techniques by cleaning and formatting raw customer data extracted from a SaaS application's database.

# Task 1: Code Correction
# You are provided with a script that is supposed to format customer names by ensuring the first letter is uppercase and the rest are lowercase, regardless of how the data was entered. However, the script contains errors. Correct the script so that it functions as intended.

def names(firstName, lastName):
    print(firstName.capitalize() + " " + lastName.capitalize())

# names('john', 'doe')

# Task 2: Email Validation
# Write a function that checks a list of email addresses for a SaaS application's user accounts. The function should verify that each email contains an "@" symbol and a "." after it, indicating a valid email format. If an email doesn't meet this criterion, print it out for further review.

def email_validation():
    email_addresses = [
    'user123@examplecom',
    'customer456@examplecom',
    'client789@example.com',
    'saasuser321example.com',
    'businessuser789@example.com',
    'saasclient456@example.com',
    'customeruser123example.com',
    'client456@example.com',
    'business123@examplecom',
    'saasclientuser789@example.com'
    ]
     
    for email in email_addresses:
        if '@' not in email or'.' not in email:
            print(f"Invalid Email Format: {email}")
# email_validation()

# Task 3: Username Generation
# Create a script that generates a username for each new user. The username should be a combination of the first three letters of their first name and the first three letters of their last name. If the name is shorter than three letters, use the full name. Ensure all usernames are in lowercase.

def userNameGeneration():
    first = input("What is your First Name: ")
    last = input("What is your Last Name: ")

    if len(first) > 3 and len(last) > 3:
        firstThree = first[:3]
        lastThree = last[:3]
        firstThree = firstThree.lower()
        lastThree = lastThree.lower()
        print("New username is: ", firstThree + lastThree)
    
    elif len(first) < 3 and len(last) > 3:
        lastThree = last[:3]
        lastThree = lastThree.lower()
        print("New username is: ", first.lower() + lastThree)
    
    elif len(first) > 3 and len(last) < 3:
        firstThree = first[:3]
        firstThree = firstThree.lower()
        print("New username is: ", firstThree + last)
        
    else:
        firstThree = first[:3]
        lastThree = last[:3]
        firstThree = firstThree.lower()
        lastThree = lastThree.lower()
        print("New username is: ", firstThree + lastThree)


# userNameGeneration()


# 2. Product Review Analysis
# Objective:
# The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize and summarize customer feedback for a SaaS product.

# Task 1: Keyword Highlighter
# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.

def highlighter():
    keywords = ["good", "excellent", "bad", 
                "poor", "average", 'trash',
                'perfect']
    
    review = input("Leave your us a Review!: ")
    reviewList = review.split(" ")
    
    for idx in range(len(reviewList)):
        for word in keywords:
            if word in reviewList[idx]:
                reviewList[idx] = reviewList[idx].upper()
                modifiedReview = " ".join(reviewList)
    print(modifiedReview)
# highlighter()


# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.

def sentimentTally():
    badcounter = 0
    goodcounter = 0
    goodWords = ["good", "excellent", "perfect"]
    badWords = ["poor", "bad", "trash"]

    review = input("Leave your us a Review!: ")
    reviewList = review.split(" ")

    for word in reviewList:
        # print(word)
        if word in badWords:
            badcounter += 1
        elif word in goodWords:
            goodcounter += 1
    return f"There were a total of {badcounter} negative words and {goodcounter} positive words"

# print(sentimentTally())


# Task 3: Review Summary
# Implement a script that takes the first 50 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

def reviewSummary():
    review = input("leave a review: ")
    reviewList = review.split(" ")

    if len(reviewList) > 50:
        reviewList[50] = '...'  
    summary = ' '.join(reviewList[:51])
    return summary


# print(reviewSummary())

# 3. Log File Formatter
# Objective:
# The aim of this assignment is to format and extract information from raw log files generated by a SaaS application to improve readability and analysis.

# Task 1: Timestamp Extraction
# Write a script that extracts the timestamp from each log entry. Assume that the timestamp is always at the beginning of each line and is enclosed in square brackets (e.g., "[2023-03-15 10:00:00]").
def extraction():
    while True:
        from datetime import datetime
        current_date = datetime.now()
        timestamp_Unix = int(current_date.timestamp())
        converted = datetime.fromtimestamp(timestamp_Unix)
        log = input("Enter Log:  (enter 'done' when finshed) ")

        if log.lower() == 'done':
            break
        else:
            print(f"[{converted}], {log}")

# extraction()


# Task 2: Error Identification
# Create a function that scans through the log file and identifies any error messages. Assume that all error messages start with the word "ERROR:". The function should print out each error message with its corresponding timestamp.

def errorIdentification ():
       while True:
        from datetime import datetime
        current_date = datetime.now()
        timestamp_Unix = int(current_date.timestamp())
        converted = datetime.fromtimestamp(timestamp_Unix)
        log = input("Enter Log:  (enter 'done' when finshed) ")
        log = log.lower()

        if log == 'done':
            break
        elif log.startswith("error"):
            print(f"[{converted}], ERROR: {log} ")

# errorIdentification()
# Task 3: Log Summary
# Develop a script that creates a summary of the log file, including the total number of entries, the number of error messages, and the number of unique timestamps in the file.

def logSummary():
    errorMessages = 0
    entries = 0
    uniqueTimeStamps = 0

    while True:
        from datetime import datetime
        current_date = datetime.now()
        timestamp_Unix = int(current_date.timestamp())
        converted = datetime.fromtimestamp(timestamp_Unix)
        log = input("Enter Log: errors must start with error, (enter 'done' when finshed) ")
        log = log.lower()

        if log == 'done':
            break
        elif log.startswith("error"):
            errorMessages += 1
        else:
            summary = reviewSummary()
        uniqueTimeStamps += 1
        entries += 1
    print(f"Summary: {summary}, Entries: {entries}, TimeStamps: {uniqueTimeStamps}, Errors: {errorMessages} ")

logSummary()



# 4. Configuration File Validator
# Objective:
# The aim of this assignment is to validate and correct a SaaS application's configuration files to ensure they adhere to the required format.

# Task 1: Property Format Checker
# You are given a configuration file where each line contains a property and its value separated by an "=" sign. Write a script that checks each line to ensure it follows this format. If a line does not contain an "=" sign or has more than one, print an error message with the line number.

# Task 2: Whitespace Remover
# Modify the script from Task 1 to remove any leading or trailing whitespace from the property names and values.

# Task 3: Duplicate Property Finder
# Extend the script to check for duplicate property names. If a duplicate is found, print out the property name and the line numbers where the duplicates are located.

# 5. User Input Data Processor
# Objective:
# The aim of this assignment is to process and format user input data for a SaaS application's registration form.

# Task 1: Input Length Validator
# Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

# Task 2: Password Complexity Checker
# Create a function that checks the complexity of a user's password. The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number. If the password does not meet these criteria, print a message explaining the complexity requirements.

# Task 3: Email Formatter
# Implement a script that ensures all user email addresses are in a standard format. Convert the entire email address to lowercase and replace any spaces with a period.

# 6. Text-Based Report Generator
# Objective:
# The aim of this assignment is to generate a formatted text-based report from raw data for a SaaS application's internal use.

# Task 1: Header Formatter
# Write a script that formats the headers of the report. Each header should be centered, in uppercase, and underlined with "=" characters.

# Task 2: Data Alignment
# Format the raw data so that each column is aligned. Assume the data is separated by commas and should be displayed in a table format with each value left-aligned in its column.

# Task 3: Report Summary
# At the end of the report, add a summary section that counts the number of data entries and calculates the average value of a numeric column.

# 7. Interactive Help Desk Bot
# Objective:
# The aim of this assignment is to create an interactive help desk bot that processes user queries and responds appropriately for a SaaS application.

# Task 1: Command Parser
# Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support"). If a command is found, print a response related to the command.

# Task 2: Issue Categorizer
# If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", etc. Print out the category of the issue for the support team.

# Task 3: Auto-Response Generator
# For general help inquiries, create a script that generates an auto-response providing links to the FAQ section, support contact information, and a link to submit a ticket.