from ParkingFloor import ParkingFloor 

class Admin:
    def __init__(self):
        self.authenticated = False

    def authenticate(self):
        while not self.authenticated:
            print("Admin authentication required.")
            password = input("Enter admin password (or 'q' to quit): ")

            if password == "1234":
                self.authenticated = True
            elif password == 'q':
                return False
            else:
                print("Invalid password. Try again or type 'q' to quit.")
        
        return True

    def admin_operations(self, parking_lot, user_authenticator):
        while True:
            print("\nAdmin Operations:")
            print("1. Add Floor")
            print("2. Shut Down System")
            print("3. Return to User Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_floor(parking_lot)
            elif choice == '2':
                return False
            elif choice == '3':
                user_authenticator.authenticate_user()  # Retour au menu utilisateur
                return True
            else:
                print("Invalid choice. Please try again.")

    def add_floor(self, parking_lot):
        floor_number = len(parking_lot.floors) + 1
        parking_floor = ParkingFloor(floor_number)
        parking_lot.add_floor(parking_floor)
        print(f"Added Floor {floor_number} successfully!")

    def quit_system(self):
        print("Shutting down the system...")
        # Mettez ici le code pour éteindre le système
        return True
