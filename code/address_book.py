class AddressBook:
    def __init__(self) -> None:
        self.book = {}

    def browse(self) -> None:
        '''Print all entries in address book.
        
        Loop through all key-value pairs in dictionary
        and output all results.
        '''
        print()
        for name, entry in self.book.items():
            print(name, '|', entry)

    def add(self) -> None:
        '''Add new entry to the address book.
        
        Get name and information of new entry and add to dictionary.
        '''
        print()
        print("Enter information of the person you want to add")
        name = input("Name : ")
        data = input("Phone/Email : ")
        self.book[name] = data

    def modify(self) -> None:
        '''Modify entry in address book.
        
        Verify entry exists in database and edit, otherwise print error.
        '''
        print()
        print("Enter name of entry you'd like to modify")
        name = input("Name : ")
        if name in self.book:
            data = input("New Phone/Email : ")
            self.book[name] = data
        else:
            print("Error: Entry does not exist")

    def delete(self) -> None:
        '''Delete entry in address book.
        '''
        print()
        print("Enter the name of the person you want to delete")
        name = input("Name : ")
        self.book.pop(name, None)
    
    def search(self) -> None:
        '''Search for entry in address book by name.
        '''
        print()
        print("Enter name of person whose information you want to find")
        try:
            name = input("Name : ")
            data = self.book[name]
            print(name, '|', data)
        except KeyError:
            print("Entry not found")

def main():
    book = AddressBook()
    running = True

    while running:
        print("\nWelcome to AddressBook")
        print("Select which operation you would like to perform or anything else to quit\n")
        print("1. Browse - Print out contents of address book.")
        print("2. Modify - Edit the contents of an existing address book entry.")
        print("3. Add - Add a new entry in the address book.")
        print("4. Delete - Remove an entry from the address book.")
        print("5. Search - Search the address book for a specific entry.\n")
        option = input("Enter your operation : ")

        if option == '1':
            book.browse()
        elif option == '2':
            book.modify()
        elif option == '3':
            book.add()
        elif option == '4':
            book.delete()
        elif option == '5':
            book.search()
        else:
            running = False


if __name__ == "__main__":
    main()