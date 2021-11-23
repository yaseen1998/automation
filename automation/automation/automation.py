from faker import Faker
import shutil
import re 

fake = Faker('en_US')

potential_contacts = ""
existing_contacts = "" 


def phone_numbers(f):

    phone_number = fake.phone_number()

    shape_of_phone_number = "(?:(?:\(?(?:00|\+)([1-4]\d\d|[1-9]\d?)\)?)?[\-\.\ \\\/]?)?((?:\(?\d{1,}\)?[\-\.\ \\\/]?){0,})(?:[\-\.\ \\\/]?(?:#|ext\.?|extension|x)[\-\.\ \\\/]?(\d+))?"
    numbers = []

    
    with open(f,'r') as f:

        f = f.read()

        get_phone_numbers = re.findall(shape_of_phone_number, f)
        

    for phone_number in get_phone_numbers:

        if phone_number not in numbers:

            numbers.append(phone_number)
        
    with open('assets/phone_numbers.txt','w') as f:

        for phone_number in sorted(numbers):

            f.write(f"\n{str(phone_number)}\n")  

    shutil.copy('assets/phone_numbers.txt', 'assets/existing-contacts.txt')

    
    return numbers


def emails(f):

    email = fake.email()

    shape_of_email = "[A-Za-z0-9]+@[A-Za-z0-9]+.[A-Za-z]+"

    emails = []

    with open(f,'r') as f:

        f = f.read()

        get_emails = re.findall(shape_of_email, f)

    for email in get_emails:

        if email not in emails:

            emails.append(email) 
  
    with open('assets/emails.txt','w') as f:

        for email in sorted(emails):

            f.write(f"\n{str(email)}\n")

    shutil.copy('assets/emails.txt', 'assets/existing-contacts.txt')

    return emails

if __name__ == "__main__":
    print(phone_numbers("assets/potential-contacts.txt"))
    
    print(emails("assets/potential-contacts.txt"))