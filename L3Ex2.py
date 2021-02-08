name = input('Enter you name: ')
surname = input('Enter your surname: ')
birth_year = int(input('Enter your year of birth: '))
city = input('Enter your city: ')
email = input('Enter your email: ')
phone = input('Enter you phone number: ')

def contact_info (name, surname, birth_year, city, email, phone):
     return ' '.join([name, surname, birth_year, city, email, phone])

print(f'Contact information: {contact_info()}')