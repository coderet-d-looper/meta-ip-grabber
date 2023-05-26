import requests
import time
import os
from colorama import init, Fore, Style

init()  # Initialize colorama


def clear_terminal():
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For Linux and Mac
        os.system("clear")


def type_writer(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def get_own_ip_info():
    url = "http://ip-api.com/json"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        ip = data["query"]
        country = data["country"]
        region = data["region"]
        city = data["city"]
        zip_code = data["zip"]
        latitude = data["lat"]
        longitude = data["lon"]

        print(f"{Fore.GREEN}IP: {ip}")
        print(f"Country: {country}")
        print(f"Region: {region}")
        print(f"City: {city}")
        print(f"ZIP Code: {zip_code}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}{Style.RESET_ALL}")
    else:
        print("Failed to retrieve IP information.")


def get_ip_info(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        ip = data["query"]
        country = data["country"]
        region = data["region"]
        city = data["city"]
        zip_code = data["zip"]
        latitude = data["lat"]
        longitude = data["lon"]

        print(f"{Fore.GREEN}IP: {ip}")
        print(f"Country: {country}")
        print(f"Region: {region}")
        print(f"City: {city}")
        print(f"ZIP Code: {zip_code}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}{Style.RESET_ALL}")
    else:
        print("Failed to retrieve IP information.")


# Clear terminal and set color for welcome message
clear_terminal()
print(f"{Fore.CYAN}")
type_writer("░█████╗░░█████╗░██████╗░███████╗██████╗░███████╗████████╗")
type_writer("██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝")
type_writer("██║░░╚═╝██║░░██║██║░░██║█████╗░░██████╔╝█████╗░░░░░██║░░░")
type_writer("██║░░██╗██║░░██║██║░░██║██╔══╝░░██╔══██╗██╔══╝░░░░░██║░░░")
type_writer("╚█████╔╝╚█████╔╝██████╔╝███████╗██║░░██║███████╗░░░██║░░░")
type_writer("░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░")
print(f"{Style.RESET_ALL}")

# Main program
print(f"{Fore.YELLOW}IP Information Bot")
type_writer("1. Get information about your own IP address.", delay=0.03)
type_writer("2. Get information about a targeted IP address.", delay=0.03)
print(Style.RESET_ALL)
choice = input(f"{Fore.YELLOW}Enter your choice (1 or 2): ")

if choice == "1":
    clear_terminal()
    print("Retrieving information...\n")
    time.sleep(1)
    get_own_ip_info()
elif choice == "2":
    target_ip = input("Enter the IP address you want to get information about: ")
    clear_terminal()
    print("Retrieving information...\n")
    time.sleep(1)
    get_ip_info(target_ip)
else:
    print("Invalid choice. Please try again.")

print(f"{Fore.MAGENTA}")
type_writer("Thank you for using IP Information Bot!", delay=0.03)
type_writer("Goodbye!", delay=0.03)
print(Style.RESET_ALL)
