class Leaving:
    def __init__(self, parking_lot):
        self.parking_lot = parking_lot

    def leaving_welcome(self):
        print(f"Before leaving {self.parking_lot.address} Parking Lot, make sure you pay the bill and enter your id!")
        print("Your id number will be in this form: parkingfloor+0+parkingspotnumber.")
        print("example: 2 floor + parking space num 6 --> 206")
        

    def release_parking_space(self):
        released_id = input("Please enter your id: ")
        if(released_id in self.parking_lot.parked_space_id):
            self.parking_lot.parked_space_id.remove(released_id)
            print("The leaving procedure is done. Now you may leave.")
        else:
            print("Incorrected id. Please enter your id again.")


    def run(self):
        self.leaving_welcome()
        self.release_parking_space()