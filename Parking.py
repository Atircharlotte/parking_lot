from UserAuthenticator import UserAuthenticator 
from Admin import Admin
from Customer import Customer

class Parking:
    def __init__(self, parking_lot):
        self.parking_lot = parking_lot
        self.user_authenticator = UserAuthenticator()
        self.user_type = None

    def welcome(self):
        print(f"Welcome to {self.parking_lot.address} Parking Lot!")

    def choose_entry(self):
        print("Choose an entry:")
        print("1. Entry 1")
        print("2. Entry 2")
        print("3. Entry 3")

        choice = input("Enter your choice: ")

        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Please enter a valid number (1, 2, or 3).\n")
            return self.choose_entry()

    def ask_vehicle_type(self):
        while True:
            print("Choose the type of your vehicle :")
            print("1. Car")
            print("2. Van")
            print("3. Truck")
            print("4. Motocycle")
            print("5. Handicapped")

            choice = input("Enter your correspondant number : \n")

            if choice in ['1', '2', '3', '4', '5']:
                return int(choice)
            else:
                print("Please enter a valid number (1, 2, 3, 4, or 5).\n")

    def get_vehicle_type(self):
        get_vehicle_type = self.ask_vehicle_type()

        if get_vehicle_type == 1:
            return 'Car'
        elif get_vehicle_type == 2:
            return 'Van'
        elif get_vehicle_type == 3:
            return 'Truck'
        elif get_vehicle_type == 4:
            return 'Motocycle'
        elif get_vehicle_type == 5:
            return 'Handicapped'

    def show_available_spots(self, vehicle_type, floor_number):
        floor = self.parking_lot.floors[floor_number - 1]
        available_spots = floor.get_available_space(vehicle_type)
        print(f"On floor {floor.floor_number}, there are {available_spots} available {vehicle_type} spots.")

    def choisir_place(self, vehicle_type, floor_number, spot_number):
        floor = self.parking_lot.floors[floor_number - 1]

        if floor.is_spot_reserved(floor_number, spot_number):
            print(f"The spot {spot_number} on floor {floor_number} is already taken.")
            available_spots = floor.get_available_space(vehicle_type)
            print(f"On floor {floor.floor_number}, there are {available_spots} available {vehicle_type} spots.")
            new_spot_number = int(input("Enter a different spot number: "))
            return self.choisir_place(vehicle_type, floor_number, new_spot_number)

        if floor.available_spaces[vehicle_type] > 0:
            floor.available_spaces[vehicle_type] -= 1
            floor.reserve_spot(floor_number, spot_number)
            return f"You have parked your {vehicle_type} on floor {floor.floor_number}, spot {spot_number}."
        else:
            return f"Sorry, there are no available spaces for {vehicle_type} on floor {floor.floor_number}."
    
    def run(self):
        #while True:
            self.welcome()
            user = self.user_authenticator.authenticate_user()


            if isinstance(user, Admin):
                while True:
                    print("\nAdmin Menu:")
                    print("1. Admin Operations")
                    print("2. Quit")

                    admin_choice = input("Enter your choice: ")

                    if admin_choice == '1':
                        if not user.admin_operations(self.parking_lot, self.user_authenticator):
                            return
                    elif admin_choice == '2':
                        if user.quit_system():
                            print("Goodbye! Have a great day.")
                            return 
                    else:
                        print("Invalid choice. Please try again.")
            elif user == 'Customer':
                entry_choice = self.choose_entry()
                type_vehicle = self.get_vehicle_type()
                floor_number = int(input("Enter the floor number where you want to park: "))

                while floor_number < 1 or floor_number > len(self.parking_lot.floors):
                    print(f"Invalid floor number. Please choose a floor between 1 and {len(self.parking_lot.floors)}.")
                    floor_number = int(input("Enter the floor number where you want to park: "))


                self.show_available_spots(type_vehicle, floor_number)
                spot_number = int(input("Enter the spot number where you want to park: "))
                # customer will get id for corresponding parking space 
                #floor numebr and spot number are saparated by '0'
                parking_space_id = f"{floor_number}0{spot_number}"
                #park at the corresponding space
                if (parking_space_id in self.parking_lot.parked_space_id):
                    print("Sorry, this place is taken.")
                else:
                    self.parking_lot.add_parked_id(parking_space_id)
                    #print(parking_space_id)
                    #print(self.parking_lot.parked_space_id)
                

                message = self.choisir_place(type_vehicle, floor_number, spot_number)
                print(message)
                

            else:
                print(f"Sorry, {user} functionality will be added later.")
