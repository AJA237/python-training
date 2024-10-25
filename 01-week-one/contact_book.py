import os
import re

class ContactBook:
    def __init__(self):
        self.contacts = []
        if (os.path.exists("contacts.csv")):
            self.load_from_file("contacts.csv")
    
    def add_contact(self, name, phone_number, email):
        self.contacts.append({
            "name": name,
            "phone_number": phone_number,
            "email": email
        })
    
    def search_contact(self, name):
        for contact in self.contacts:
            if contact["name"].lower() == name:
                return contact
        return None
    
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                self.contacts.remove(contact)
                self.save_to_file("contacts.csv")
                return True
        return False
    
    def update_contact(self, name, phone_number=None, email=None):
        for contact in self.contacts:
            if contact["name"] == name:
                if phone_number:
                    contact["phone_number"] = phone_number
                if email:
                    contact["email"] = email
                self.save_to_file("contacts.csv")
                return True
        return False
    
    def print_all_contacts(self):
        for contact in self.contacts:
            print(contact)

    def save_to_file(self, file_path):
        with open(file_path, "w") as file:
            for contact in self.contacts:
                file.write(f"{contact['name']},{contact['phone_number']},{contact['email']}\n")
    
    def load_from_file(self, file_path):
        with open(file_path, "r") as file:
            for line in file:
                name, phone_number, email = line.strip().split(",")
                self.add_contact(name, phone_number, email)

    def email_validator(self, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email)

    def run(self):
        print("Welcome to the Contact Book!")
        while True:
            operation = input("Enter operation (add, search, delete, update, view, exit): ").strip()
            if operation == "add":
                name = input("Enter name: ").strip().title()
                phone_number = input("Enter phone number: ").strip()
                email = input("Enter email: ").strip()
                if (email and not self.email_validator(email)):
                    print("Invalid email format.")
                    continue
                self.add_contact(name, phone_number, email)
                print("Contact added successfully!")
                continue
            elif operation == "search":
                name = input("Enter name: ").strip().lower()
                contact = self.search_contact(name)
                if contact:
                    print(contact)
                else:
                    print("Contact not found.")
                continue
            elif operation == "delete":
                name = input("Enter name: ").strip()
                if self.delete_contact(name):
                    print("Contact deleted successfully!")
                else:
                    print("Contact not found.")
                continue
            elif operation == "update":
                name = input("Enter name: ").strip()
                phone_number = input("Enter phone number (press enter to skip): ").strip()
                email = input("Enter email (press enter to skip): ").strip()
                if self.update_contact(name, phone_number, email):
                    print("Contact updated successfully!")
                else:
                    print("Contact not found.")
                continue
            elif operation == "view":
                self.print_all_contacts()
                continue
            elif operation == "exit":
                break
            else:
                print("Invalid operation.")


