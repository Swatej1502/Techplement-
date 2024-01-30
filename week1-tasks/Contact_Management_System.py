import json


def IsNumber(phone):
    if(len(str(phone))==10):
       return 1
    else:
       print("\n Enter 10 digits correctly !!\n")
       return 0

def Validate():
           while(True):
               try:
                   phone=int(input("Enter the 10 digits Number :"))
               except(ValueError):
                    print("\nEnter Number not string !!\n")
               else:
                   if(IsNumber(phone)):
                       return phone


def load_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts_data = file.read()
            contacts = json.loads(contacts_data)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        json.dump(contacts, file, indent=2)

def add_contact(name, phone):
    contacts = load_contacts()
    contacts[name] = phone
    save_contacts(contacts)
    print(f"\n Contact {name} added successfully!\n")

def search_contact(name):
    dic={}
    contacts = load_contacts()
    contact = contacts.get(name)
    if contact:
        dic[name]=contact
        return dic
    else:
        return 0

def update_contact(name,phone):
    contacts = load_contacts()
    contacts[name]= phone
    save_contacts(contacts)
    print(f"\nContact {name} updated successfully!\n")
        
def update_CompleteContact(name,d_name,phone):
    contacts=load_contacts()
    if(name in contacts):
        del contacts[name]
        contacts[d_name]=phone
        save_contacts(contacts)
        print("\nNew name updated Successfully\n")
    else:
        print("\nContact not Present\n")
        
def update_ContactName(name,d_name):
    contacts=load_contacts()
    phone=contacts.get(name)
    if(name in contacts):
        del contacts[name]
        contacts[d_name]=phone
        save_contacts(contacts)
        print(f"\n Name {name} Updated to {d_name} Successfully\n")
    else:
        print("\nContact not Present\n")
        
        

def main():
    print("\n Contact Management System \n")
    while True:
        print("\n1. Add Contact\n2. Search Contact By Name\n3. Update Contact Information\n4. Exit")
        choice = input("\nEnter your choice (1/2/3/4): ")

        if choice == "1":
            while(True):
                name = input("Enter contact name: ")
                if(search_contact(name)):
                    print("\nContact name is already present.Try another Name!!\n")
                else:
                    break
            
            phone = Validate()
            add_contact(name, phone)
          

        elif choice == "2":
            name = input("\nEnter contact name to search: ")
            contact=search_contact(name)
            if(contact):
                print("\n\nContact Information\n Name  : {0}\n Phone :{1}".format(name,contact[name]))
            else:
                print("\n{0} Contact is not present.\n".format(name))

        elif choice == "3":
            while(True):
                name = input("Enter contact name you want to update: ")
                if(search_contact(name)):
                    break
                else:
                    print("\nContact name is not present.Enter name correctly!!\n")
            c=input("\nIf you want to change the name enter y.Otherwise enter n or any key:").lower()
            if(c=="y"):
                while(True):
                    duplicate_name = input("\nEnter New name: ")
                    if(search_contact(duplicate_name)):
                        print("\nContact name is already present.Enter another!!\n")
                    else:
                        break
                c=input("\nIf you want to change the number also enter y .Otherwise enter n or any key:").lower()
                if(c=="y"):
                    phone =Validate()
                    update_CompleteContact(name,duplicate_name,phone)
                else:
                    update_ContactName(name,duplicate_name)
                    
            else:
                 phone = Validate()
                 update_contact(name,phone)
                
        elif choice == "4":
            print("\nThank You!")
            break

        else:
            print("\nInvalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    main()