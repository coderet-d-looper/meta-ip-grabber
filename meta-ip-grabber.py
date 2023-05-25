import requests
import time


def type_writer(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
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
        print(f"IP: {ip}")
        print(f"Country: {country}")
        print(f"Region: {region}")
        print(f"City: {city}")
        print(f"ZIP Code: {zip_code}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
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
        print(f"IP: {ip}")
        print(f"Country: {country}")
        print(f"Region: {region}")
        print(f"City: {city}")
        print(f"ZIP Code: {zip_code}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    else:
        print("Failed to retrieve IP information.")


# Typewriter animation for welcome message
welcome_message = "Welcome to IP Information Bot"
type_writer(welcome_message)
time.sleep(1)
coderet_name = "Coderet D Looper"
print(f"Presented by: {coderet_name}")
print()

# Main program
print("IP Information Bot")
print("1. Get information about your own IP address.")
print("2. Get information about a targeted IP address.")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    get_own_ip_info()
elif choice == "2":
    target_ip = input("Enter the IP address you want to get information about: ")
    get_ip_info(target_ip)
else:
    print("Invalid choice. Please try again.")
