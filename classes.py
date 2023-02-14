class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


p1 = Point(2, 2)
print(p1.x)


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)
people = ["Harry", "Ron", "Chros", "Turro"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight succesfully")
    else:
        print(f"Not available space for {person} in flight.")

