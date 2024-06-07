contact = {}

def display_contact():
    print("Name\t\t Contact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

while True:
    choice = int(input(" 1.Add new Contact \n 2.Search Contact \n 3.Display Contact \n 4.Edit Contact \n 5.Delete Contact \n 6.Exit \n Enter your Choice: "))
    if choice== 1:
        name=input("Enter the name")
        phone_no= input("Enter the mobile number")
        contact[name]=phone_no
    elif choice == 2:
        search_name=input("Enter the contact name: ")
        if search_name in contact:
            print(search_name, "'s contact number is ",contact[search_name])
        else:
            print("Name not found!")
    elif choice == 3:
        if not contact:
            print("Contact Book Empty!")
        else:
            display_contact()
    elif choice == 4:
        edit_contact =input("Enter the contact to be edited")
        if edit_contact in contact:
            phone_no=input("Enter mobile number: ")
            contact[edit_contact]=phone_no
            print("Contact Updated!")
            display_contact()
        else:
            print("Name not found!")
    elif choice == 5:
        del_contact=input("Enter the contact to be deleted ")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n?")
            if confirm=='y' or confirm=='Y' or confirm=='yes' or confirm=='Yes':
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name not found!")
    else:
        break
