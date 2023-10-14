from Admin import Admin 

class UserAuthenticator:
    def authenticate_user(self):
        print("Welcome to TWOOM ParkingLot!")
        while True:
            print("Are you:")
            print("1. Admin")
            print("2. Parking Attendant")
            print("3. Customer")

            choice = input("Enter your correspondant number : ")

            if choice == '1':
                admin = Admin()
                if admin.authenticate():
                    return admin
            elif choice == '2':
                return 'ParkingAttendant'
            elif choice == '3':
                return 'Customer'
            else:
                print("Invalid choice. Please try again.")
