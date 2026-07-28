#phone book directory

class PhoneBook:
    phone_directory = []
    phone_map = {}

    def __init__(self,name,phonenumber):
        self.name=name
        self.phone=phonenumber
        # store contact as a dict entry and in a map for quick lookup
        PhoneBook.phone_directory.append(self.phone)
        self.phone_map[self.name]=self.phone

    def show_contact(self):
        return f"Name : {self.name} , Contact Number: {self.phone}"

    @classmethod
    def show_all_contact(classs):
        if(len(classs.phone_directory))==0:
            print("No contact found in the directory")
        else:
            for contact in classs.phone_directory:
                print(contact)

    @classmethod
    def searchcontact(cls,searchname):
        b=True
        for contact in cls.phone_map:
            if(contact.lower()==searchname.lower()):
                print(f"The {searchname} is present in the book ans the contact no is {cls.phone_map[contact]}")
                b=False
                break;

        if(b):
            print("Not found the contact")

   



phone1=PhoneBook("John1",1111111111)
phone2=PhoneBook("John2",2222222222)
phone3=PhoneBook("John3",3333333333)
phone4=PhoneBook("John4",4444444444)
phone5=PhoneBook("John5",5555555555)
phone6=PhoneBook("John6",6666666666)
phone7=PhoneBook("John7",7777777777)
phone8=PhoneBook("John8",8888888888)
phone9=PhoneBook("John9",9999999999)

print(phone1.show_contact())
print(phone2.show_contact())
print(phone3.show_contact())
print(phone4.show_contact())
print(phone5.show_contact())
print(phone6.show_contact())
print(phone7.show_contact())
print(phone8.show_contact())
print(phone9.show_contact())

PhoneBook.show_all_contact()
print(phone9.phone_map)

PhoneBook.searchcontact("John8")
PhoneBook.searchcontact("Mark")