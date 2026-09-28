# Address Book Application in Python

## Project Description
A menu-driven Python Address Book Application that allows users to add, view, search, update, and delete personal or professional contacts.

## Contact Details Stored
- Name
- Phone Number
- Email Address
- Postal Address
- Other Information / Notes

## Features
1. Add Contact
2. View All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Permanent data storage using JSON file handling

## Requirements
- Python 3.x
- No external libraries are required.

## How to Run

Open a terminal/command prompt in this project folder and run:

```bash
python address_book.py
```

On some systems, use:

```bash
python3 address_book.py
```

The application automatically creates `contacts.json` when the first contact is saved.

## Data Storage
All contacts are permanently stored in `contacts.json`. The file is automatically loaded when the application starts and updated after adding, modifying, or deleting contacts.

## Project Structure

```text
AddressBookProject/
│
├── address_book.py
├── contacts.json
└── README.md
```

## Educational Concepts Used
- Python functions
- Lists and dictionaries
- Loops and conditional statements
- User input
- File handling
- JSON data storage
- Exception handling
- Menu-driven programming
