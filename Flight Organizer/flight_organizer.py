from flight import Flight
from data import get_flights, get_total_cost

class FlightOrganizer:
    def __init__(self):
        self.flights = self._load_flights()

    def _load_flights(self):
        return get_flights()

    def get_cheapest_round_trip(self):
        all_round_trip_options = []

        # Iterate through each airline's flights
        for airline, details in self.flights.items():
            outbound_flights = details["outbound"]
            inbound_flights = details["inbound"]

            # Combine outbound and inbound flights
            for outbound_flight in outbound_flights:
                for inbound_flight in inbound_flights:
                    if self._is_two_nights_stay(outbound_flight, inbound_flight):
                        total_cost = outbound_flight.price + inbound_flight.price
                        all_round_trip_options.append((airline, outbound_flight, inbound_flight, total_cost))

        # Sort round trip options by total cost
        all_round_trip_options.sort(key=lambda x: x[3])

        return all_round_trip_options

    """def get_cheapest_round_trip(self):
        # Method to find the cheapest round trip flights
        all_round_trip_options = []

        # Iterate through each airline's flights
        for airline, details in self.flights.items():
            outbound_flights = details["outbound"]
            inbound_flights = details["inbound"]

            # Combine outbound and inbound flights
            for outbound_flight in outbound_flights:
                for inbound_flight in inbound_flights:
                    # Check if the stay in Barcelona is for 2 nights
                    if self._is_two_nights_stay(outbound_flight, inbound_flight):
                        # Calculate total cost for the round trip
                        total_cost = outbound_flight.price + inbound_flight.price

                        # Print information about each round trip option
                        print(
                            f"Airlines: {airline} - Outbound Flight: {outbound_flight} - Inbound Flight: {inbound_flight} - Total Cost: {total_cost}")

                        # Append round trip option to the list
                        all_round_trip_options.append((airline, outbound_flight, inbound_flight, total_cost))

        # Sort round trip options by total cost
        all_round_trip_options.sort(key=lambda x: x[3])

        # Print the sorted round trip options
        print("\nSorted Round Trip Options:")
        for option in all_round_trip_options:
            print(option)

        # Return the sorted round trip options
        return all_round_trip_options"""

    def _is_two_nights_stay(self, outbound_flight, inbound_flight):
        outbound_date = outbound_flight.date
        inbound_date = inbound_flight.date
        return (inbound_date - outbound_date).days == 2


"""def print_flight_options(flights):
    for airline, details in flights.items():
        print(f"Airline: {airline}")
        print("-------------------------------------------------------")
        total_cost = get_total_cost(details["outbound"], details["inbound"])
        sorted_costs = sorted(total_cost.items(), key=lambda x: x[1])
        for combination, cost in sorted_costs:
            print(f"From {combination[0]} to {combination[1]}: Total Cost - {cost} PLN")
        print("\n")
"""

if __name__ == "__main__":
    organizer = FlightOrganizer()
    organizer.get_cheapest_round_trip()