import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

print("\nConnecting to Google Cloud API...")

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "Login Database-8839018be547.json", scope)

client = gspread.authorize(credentials)

sheet = client.open("Login Database").sheet1

print("Connected, welcome to the: ")


def create_unique_id():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    while True:
        unique_id = ""
        for x in range(4):
            unique_id = unique_id + random.choice(characters)

        with open("used_ids", "r") as ids:
            if unique_id in ids.read():
                print(f"ID: {unique_id} already in use.")
                continue

            else:
                with open("used_ids", "a") as ids:
                    ids.write("\n" + unique_id)
                print(f"Creating ID: {unique_id}...")
                return unique_id


def retrieve_all_data():
    try:
        data = sheet.get_all_records()
        print(f"\n{data}")
    except:
        print("Unable to retrieve all data.")


def insert_data():
    website = str(input("\nEnter the website name or URL: ")).lower()
    username = str(input("Enter the username: "))
    password = str(input("Enter the password: "))

    data = [website, username, password,
            create_unique_id()]

    try:
        sheet.insert_row(data, 2)
        print(f"Entry ID: {data[3]} created.")
    except:
        print("Unable to insert data.")


def authenticate():
    keys = ["N1G-HTW-1NG", "R3D-H00D", "ST4R-F1R3", "B34S-TB0Y"]
    while True:
        authentication = str(input("\nEnter your authentication key: "))
        if authentication in keys:
            print("Logged in.")
            return True
        else:
            print("Invalid authentication key.")
            continue


def menu():
    print("\n===================\nLOGIN DATABASE v1.1\n===================")

    if authenticate():
        while True:
            ask = int(input(
                "\n[View All = 1]\n[New Entry = 2]\n[Exit = 3]\nWhat would you like to do? "))

            if ask == 1:
                retrieve_all_data()
                continue
            elif ask == 2:
                insert_data()
                continue
            elif ask == 3:
                break
            else:
                print(f"Invalid action selector {ask}.")
                continue


menu()
