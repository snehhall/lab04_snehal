
class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        result = [flight for flight in self.flights if flight.source == city or flight.destination == city]
        return result

    def search_from_city(self, source_city):
        result = [flight for flight in self.flights if flight.source == source_city]
        return result

    def search_between_cities(self, source_city, destination_city):
        result = [flight for flight in self.flights if flight.source == source_city and flight.destination == destination_city]
        return result

def main():
    flight_table = FlightTable()

    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]

    for data in flight_data:
        flight = Flight(data[0], data[1], data[2], data[3])
        flight_table.add_flight(flight)

    city_mapping = {
        "BLR": "Bengaluru",
        "BOM": "Mumbai",
        "BBI": "Bhubaneswar",
        "HYD": "Hyderabad",
        "JLR": "Jabalpur"
    }

    while True:
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            city_code = input("Enter the city code: ")
            city_name = city_mapping.get(city_code, "Unknown City")
            result = flight_table.search_by_city(city_code)
            if result:
                print(f"Flights for {city_name}:")
                for flight in result:
                    print(f"Flight ID: {flight.flight_id}, To: {flight.destination}, Price: {flight.price}")
            else:
                print(f"No flights found for {city_name}")
                
        elif choice == 2:
            source_city = input("Enter the source city code: ")
            source_name = city_mapping.get(source_city, "Unknown City")
            result = flight_table.search_from_city(source_city)
            if result:
                print(f"Flights from {source_name}:")
                for flight in result:
                    print(f"Flight ID: {flight.flight_id}, To: {flight.destination}, Price: {flight.price}")
            else:
                print(f"No flights found from {source_name}")
        
        elif choice == 3:
            source_city = input("Enter the source city code: ")
            destination_city = input("Enter the destination city code: ")
            source_name = city_mapping.get(source_city, "Unknown City")
            destination_name = city_mapping.get(destination_city, "Unknown City")
            result = flight_table.search_between_cities(source_city, destination_city)
            if result:
                print(f"Flights from {source_name} to {destination_name}:")
                for flight in result:
                    print(f"Flight ID: {flight.flight_id}, Price: {flight.price}")
            else:
                print(f"No flights found from {source_name} to {destination_name}")
        
        elif choice == 4:
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
