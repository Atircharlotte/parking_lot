class ParkingLot:
    def __init__(self, id, address):
        self.id = id
        self.address = address
        self.floors = []
        #store_park_customer's id
        self.parked_space_id = []

    def add_floor(self, floor):
        self.floors.append(floor)

    #add customer's id to the list
    def add_parked_id(self,customer_id):
        self.parked_space_id.append(customer_id)
'''
parkingLot1 = ParkingLot(1234, "Pusan")
parkingLot1.add_parked_id("1b")
print(parkingLot1.parked_space_id)
'''   
