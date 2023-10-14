from ParkingLot import ParkingLot
from ParkingFloor import ParkingFloor
from Parking import Parking

parking_lot = ParkingLot(id = 1, address='123 Twoon Street')

for i in range(4):
    parking_floor = ParkingFloor(floor_number = i + 1)
    parking_lot.add_floor(parking_floor)

#execution
parking = Parking(parking_lot)
parking.run()
