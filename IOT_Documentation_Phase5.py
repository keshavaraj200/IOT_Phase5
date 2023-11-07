import random
class ParkingLot:
    def __init__(self, name, total_spaces):
        self.name = name
        self.total_spaces = total_spaces
        self.available_spaces = total_spaces

    def park_car(self):
        if self.available_spaces > 0:
            self.available_spaces -= 1
            return True
        else:
            return False

    def leave_car(self):
        if self.available_spaces < self.total_spaces:
            self.available_spaces += 1
            return True
        else:
            return False

class SmartParkingSystem:
    def __init__(self):
        self.parking_lots = []

    def add_parking_lot(self, parking_lot):
        self.parking_lots.append(parking_lot)

    def suggest_parking_spot(self):
        available_lots = [lot for lot in self.parking_lots if lot.available_spaces > 0]
        if not available_lots:
            return None
        else:
            random_lot = random.choice(available_lots)
            return random_lot

def simulate_smart_parking():
    smart_parking = SmartParkingSystem()

    lot1 = ParkingLot("Lot A", total_spaces=10)
    lot2 = ParkingLot("Lot B", total_spaces=5)
    smart_parking.add_parking_lot(lot1)
    smart_parking.add_parking_lot(lot2)

    for _ in range(15):
        if random.choice([True, False]):
            parking_lot = smart_parking.suggest_parking_spot()
            if parking_lot:
                if parking_lot.park_car():
                    print(f"Car parked at {parking_lot.name}.")
                else:
                    print(f"No available spaces at {parking_lot.name}.")
            else:
                print("No available parking lots.")
        else:
            parking_lot = random.choice(smart_parking.parking_lots)
            if parking_lot.leave_car():
                print(f"Car left {parking_lot.name}.")
            else:
                print(f"No cars to leave at {parking_lot.name}.")

if __name__ == "__main__":
    simulate_smart_parking()
