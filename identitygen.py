import requests
from colorama import init, Fore, Back, Style
import pyfiglet

# Function to print a section with a title and details
def print_section(title, details):
    print(Style.BRIGHT + Fore.BLACK + Back.YELLOW + f' {title} ')
    for key, value in details.items():
        print(Fore.GREEN + f'{key}: ' + Fore.WHITE + f'{value}')
    print()

# Print initial header and logo
logo = pyfiglet.figlet_format("IDENTITY GEN")
print(logo)
print(Fore.MAGENTA + "> HELPS You To Generate Random Person Details")
print(Fore.BLACK + Back.MAGENTA + "> scripted by @garurprani")
print()

# Initialize colorama
init(autoreset=True)

# Print 'Generating...' message in cyan color
print(Fore.CYAN + Back.BLACK + "-> Generating... Please wait.")

# Fetching the random user data from the API
response = requests.get('https://randomuser.me/api')

# Check if request was successful
if response.status_code == 200:
    print(Fore.BLACK + Back.CYAN + "-> Data fetched successfully!\n")
    
    # Extract user details
    data = response.json()
    user = data['results'][0]

    # Extracting user details
    title = user['name']['title']
    first_name = user['name']['first']
    last_name = user['name']['last']

    gender = user['gender']
    age = user['dob']['age']
    dob = user['dob']['date']

    location_street = user['location']['street']['name']
    location_city = user['location']['city']
    location_state = user['location']['state']
    location_country = user['location']['country']
    location_postcode = user['location']['postcode']

    email = user['email']
    email_uuid = user['login']['uuid']
    email_username = user['login']['username']
    email_password = user['login']['password']
    phone = user['phone']

    # Organizing details into sections
    basic_details = {
        'Title': title,
        'First Name': first_name,
        'Last Name': last_name,
        'Gender': gender,
        'D.O.B': dob,
        'Age': age
    }

    location_details = {
        'Street': location_street,
        'City': location_city,
        'State': location_state,
        'Country': location_country,
        'PostCode': location_postcode
    }

    account_details = {
        'Email': email,
        'UUID': email_uuid,
        'Username': email_username,
        'Password': email_password,
        'Phone': phone
    }

    # Printing the sections
    print_section('BASIC DETAILS', basic_details)
    print_section('LOCATION DETAILS', location_details)
    print_section('ACCOUNT DETAILS', account_details)

else:
    print(Fore.RED + f"Failed to fetch data. Status code: {response.status_code}")
