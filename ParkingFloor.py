class ParkingFloor:
    reserved_spots = {}

    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.capacity = 22
        self.available_spaces = {
            'Car': 14,
            'Van': 2,
            'Truck': 2,
            'Motocycle': 2,
            'Handicapped': 2
        }
        self.assign_initial_spaces()

    def get_available_space(self, vehicle_type):
        return self.available_spaces.get(vehicle_type, 0)

    def assign_initial_spaces(self):
        initial_assignments = {
            'Motocycle': [1, 2],
            'Van': [3, 4],
            'Truck': [5, 6],
            'Car': list(range(7, 21)),
            'Handicapped': [19, 20]
        }
        for vehicle_type, spots in initial_assignments.items():
            self.available_spaces[vehicle_type] = len(spots)

    def reserve_spot(self, floor_number, spot_number):
        if floor_number not in self.reserved_spots:
            self.reserved_spots[floor_number] = []
        self.reserved_spots[floor_number].append(spot_number)

    def is_spot_reserved(self, floor_number, spot_number):
        return floor_number in self.reserved_spots and spot_number in self.reserved_spots[floor_number]
