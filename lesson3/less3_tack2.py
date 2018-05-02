class Air_company:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def total_profit(self):
        total = 0
        for flight in self.flights:
            total += flight.profit()
        return total

class Flight:
    def __init__(self, distance):
        self.distance = distance
        self.airplane = None
        self.staff = []
        self.tickets = []

    def set_airplane(self, airplane):
        self.airplane = airplane

    def add_staff(self, staff):
        self.staff.append(staff)

    def add_ticket(self, ticket):
        if self.airplane.capasity < len(self.tickets):
            self.tickets.append(ticket)
        else:
            raise Exception("Capasity error")

    def profit(self):
        total = 0
        for ticket in self.tickets:
            total += ticket.price
        for staff in self.staff:
            total -= staff.salary
        total -= self.airplane.consumption * self.distance * self.airplane.fuel.price
        return total

class Airplane:
    def __init__(self, capasity, fuel, consumption):
        self.capasity = capasity
        self.fuel = fuel
        self.consumption = consumption

class Staff:
    def __init__(self, salary):
        self.salary = salary

class Fuel:
    def __init__(self, price):
        self.price = price

class Ticket:
    def __init__(self, price):
        self.price = price
