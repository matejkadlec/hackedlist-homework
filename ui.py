import tkinter as tk

class PhonebookApp:
    def __init__(self, phonebook):
        self.phonebook = phonebook

        # Initialize the main window and set the title to "Phonebook"
        self.root = tk.Tk()
        self.root.title("Phonebook")

        # Search box and results display
        self.name_var = tk.StringVar()
        self.number_var = tk.StringVar()
        

        # Create and pack Label with text "Search:"
        tk.Label(self.root, text="Search:").pack()

        # Create and pack Entry that calls self.update_results method on key release
        search_box = tk.Entry(self.root, textvariable=self.name_var) 
        search_box.pack()
        search_box.bind("<KeyRelease>", self.update_results)

        # Create and pack Listbox that calls self.display_number method on name selection
        self.contact_list = tk.Listbox(self.root)
        self.contact_list.pack()
        self.contact_list.bind("<<ListboxSelect>>", self.display_number)

        # Create and pack Label with text "Phone number:" 
        tk.Label(self.root, text="Phone number:").pack()

        # Create and pack Label with dynamically updated phone number based on chosen name
        tk.Label(self.root, textvariable=self.number_var).pack()

        # Initialize the listbox with all contacts
        self.sort_insert_contacts(self.phonebook.search_contact(""))

    def sort_insert_contacts(self, contacts):
        # Sort contacts alphabetically by name (A-Z) using lambda
        sorted_contacts = sorted(contacts, key=lambda c: c["name"])
        
        # Insert contacts into self.contact_list
        for contact in sorted_contacts:
            self.contact_list.insert(tk.END, contact["name"])

    def update_results(self, event):
        # Get prefix from searchbox and all contacts starting with that prefix
        prefix = self.name_var.get()
        contacts = self.phonebook.search_contact(prefix)

        # Clear the listbox
        self.contact_list.delete(0, tk.END) # Clear the listbox
        
        self.sort_insert_contacts(contacts)

    def display_number(self, event):
        # Ensure name is selected
        selected = self.contact_list.curselection()
        if not selected:
            return

        # Get selected name and look it up in contacts dictionary
        name = self.contact_list.get(selected)
        contacts = self.phonebook.search_contact(name)
        
        # Set the number variable to the selected contact's number
        self.number_var.set(contacts[0]["number"])

    def run(self):
        # Run the main loop
        self.root.mainloop()
