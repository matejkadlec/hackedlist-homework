from database.database import get_session
from database.crud import insert_contact, get_all_contacts
from ui import PhonebookApp


class Phonebook:
    def __init__(self):
        self.session = get_session()
        self.contacts = get_all_contacts(self.session)

    # Add new contact to the database and append it to the dictionary (in case it's added while app is running)
    def add_contact(self, name: str, number: str) -> bool:
        if insert_contact(self.session, name, number):
            self.contacts.append({"name": name, "number": number})
            return True
        return False

    # Look up contact from self.contacts based on prefix (if the prefix equals the name, it returns one record)
    def search_contact(self, prefix: str):
        return [c for c in self.contacts if c["name"].lower().startswith(prefix.lower())]


if __name__ == "__main__":
    pb = Phonebook()

    # Test add_contact method
    # print(pb.add_contact("Alice", "123456789")) # False
    # print(pb.add_contact("Joe", "123456789")) # True
    # print(pb.add_contact(123, "123456789")) # ValueError
    # print(pb.add_contact("Joe", "12345678")) # ValueError
    # print(pb.add_contact("Joe", "a12345678")) # ValueError

    # Create PhonebookApp and run it
    app = PhonebookApp(Phonebook())
    app.run()
