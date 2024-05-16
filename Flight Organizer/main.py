from flight_organizer import FlightOrganizer
from data import get_flights
from flight import get_total_cost
def main():
    # obtain the flight's data directory in data.py
    flights_data = get_flights()
    flight_organizer = FlightOrganizer(flights_data)

    # Extract outbound and inbound flights separately for each airline
    wizzair_outbound = flight_organizer.get_outbound_flights("WizzAir")
    wizzair_inbound = flight_organizer.get_inbound_flights("WizzAir")
    ryanair_outbound = flight_organizer.get_outbound_flights("RyanAir")
    ryanair_inbound = flight_organizer.get_inbound_flights("RyanAir")

    # Generate round trip options for each combination of outbound and inbound flights
    round_trip_options = []

    # Case 1: Both outbound and inbound flights are from WizzAir
    round_trip_options += get_total_cost(wizzair_outbound, wizzair_inbound, "WizzAir", "WizzAir")

    # Case 2: Both outbound and inbound flights are from RyanAir
    round_trip_options += get_total_cost(ryanair_outbound, ryanair_inbound, "RyanAir", "RyanAir")

    # Case 3: Outbound flight is from WizzAir and inbound flight is from RyanAir
    round_trip_options += get_total_cost(wizzair_outbound, ryanair_inbound, "WizzAir", "RyanAir")

    # Case 4: Outbound flight is from RyanAir and inbound flight is from WizzAir
    round_trip_options += get_total_cost(ryanair_outbound, wizzair_inbound, "RyanAir", "WizzAir")

    # Filter options to include only those with a two-night stay in Barcelona
    round_trip_options = [option for option in round_trip_options if
                          flight_organizer._is_two_nights_stay(option[1], option[3])]

    # Sort options by total cost
    round_trip_options.sort(key=lambda x: x[4])

    # Print round trip options
    print("Round trip options from cheapest to most expensive:")
    for option in round_trip_options:
        outbound_airline, outbound_flight, inbound_airline, inbound_flight, total_cost = option
        print(f"Outbound Airline: {outbound_airline}, Outbound: {outbound_flight.date} - {outbound_flight.price}")
        print(f"Inbound Airline: {inbound_airline}, Inbound: {inbound_flight.date} - {inbound_flight.price}")
        print(f"Total cost: {total_cost}")


if __name__ == "__main__":
    main()
