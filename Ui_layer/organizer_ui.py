from validation.player_validation import ValidatePlayer
from logic.player_logic import PlayerLogic
from Error.player_error import *


class OrganizerUI:
    def __init__(self):
        self.validate_player = ValidatePlayer()    
        
    def __str__(self):
        return (
            "Organiser\n\n"
            "1. View Teams\n"
            "2. See Tournament\n"
            "3. See match schedule\n"
            "4. Create a player\n"
            "5. Create a tournament\n"
            "6. Create a club\n\n"
            "9. Change role\n\n"
        )

    def get_choice(self):
        """Ask user and return a validated choice."""
        while True:
            print(self)
            choice = input("Enter number for action: ").strip()

            if choice in {"1", "2", "3", "4", "5", "6" "9"}:
                return choice
        
            print("Invalid choice. Try again.\n")
    
        

     
   

    def create_player(self):
        '''Creating a player by asking one information at a time and checking it in Validate Player class'''

        #Name
        state = False 
        while state == False: 
            name = input("Name: ") 
            try: 
                state = self.validate_player.validate_name(name) 

            except EmptyInput: 
                print("Player needs to have a name") 


        #Age
        state = False 
        while state == False: 
            age = input("Age: ") 
            try: 
                state = self.validate_player.validate_age(age) 
            except WrongAgeException: 
                print("Age has to be a number") 
            except InvalidAgeException: 
                print("Player is too old or too young") 

        #Home address 

        state = False 
        while state == False: 
            address = input("Address: ") 
            try: 
                state = self.validate_player.validate_home_adress(address) 
            except EmptyInput: 
                print("Player needs a home address") 
        

        #Phone 

        state = False 
        while state == False: 
            number = "354" + input("Phone number: +354 ") 
            try: 
                state = self.validate_player.validate_number(number) 
            except EmptyInput: 
                print("Player needs a phone number") 
            except invalidNumberException: 
                print("Number is invalid, try again") 


        #Email 

        state = False 
        while state == False: 
            email = input("Email: ") 
            try: 
                state = self.validate_player.validate_email(email) 
            except EmptyInput: 
                print("Player needs to have an email") 
            except InvalidEmailException: 
                print("Email is invalid, try again") 
        

        #Link 

        state = False 
        while state == False: 
            link = input("Link: ") 
            try: 
                state = self.validate_player.validate_link(link) 
            except EmptyInput: 
                print("Player neeeds to have a link") 



        #Handle 

        state = False 
        while state == False: 
            handle = input("Handle: ") 
            try: 
                state = self.validate_player.validate_handle(handle) 
            except EmptyInput: 
                print("Player needs to have a link") 
            except InvalidCharacterHandle: 
                print("Link is invalid, try again") 
            except HandleExistsException: 
                print("Handle already exists") 







        #Tournamnet

        
        #name
        name = input("Name: ")
        validation: tuple = self.validate_player.validate_name(name) #returns a tuple: (False, "What is wrong") if input is invalid
            
        while validation[0] == False: #while the input is invalid it aks again
            print(validation[1])
            name = input("Name: ")
            validation = self.validate_player.validate_name(name)
        
        #Age
        age = input("Age: ")
        validation = self.validate_player.validate_age(age) 
        while validation[0] == False:
            print(validation[1])
            age = input("Age: ")
            validation = self.validate_player.validate_age(age)

        #Home address
        address = input("Home address: ")
        validation = self.validate_player.validate_home_adress(address)
        while validation[0] == False:
            print (validation[1])
            address = input("Home address: ")
            validation = self.validate_player.validate_home_adress(address)
        
        #Phone
        phone = "354" + input("Phone number: +354 ")
        validation = self.validate_player.validate_phone(phone)
        while validation[0] == False:
            print (validation[1])
            phone = "354" + input("Phone number: +354 ")
            validation = self.validate_player.validate_phone(phone)
        

        #Email
        email = input("Email: ")
        validation = self.validate_player.validate_email(email)
        while validation[0] == False:
            print(validation[1])
            email = input("Email: ")
            validation = self.validate_player.validate_email(email)

        #Link
        link = input("Link: ")
        validation = self.validate_player.validate_link(link)
        while validation[0] == False:
            print(validation[1])
            link = input("Link: ")
            validation = self.validate_player.validate_link(link)

        #Handle
        handle = input("Handle: ")
        validation = self.validate_player.validate_handle(handle)
        while validation[0] == False:
            print(validation[1])
            handle = input("Handle: ")
            validation = self.validate_player.validate_handle(handle)

        PlayerLogic.create_player(name, age, address, phone, email, link, handle)
        return 
    