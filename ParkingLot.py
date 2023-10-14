class ParkingLot:
    def __init__(self, id, address):
        self.id = id
        self.address = address
        self.floors = []

    def add_floor(self, floor):
        self.floors.append(floor)
