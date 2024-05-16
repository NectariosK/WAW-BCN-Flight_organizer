from datetime import datetime

class Flight:
    def __init__(self, airline, direction, departure_time, arrival_time, price, date_str):
        self.airline = airline
        self.direction = direction
        self.departure_time = datetime.strptime(departure_time, "%H:%M")
        self.arrival_time = datetime.strptime(arrival_time, "%H:%M")
        self.price = price
        self.date = datetime.strptime(date_str, "%A %d %b %Y")

def get_total_cost(outbound_flights, inbound_flights, outbound_airline, inbound_airline):
    #total_cost = {}  # Initialize an empty list to store total costs

    round_trip_options = []

    # Loop through outbound and inbound flights to calculate total cost
    for outbound_flight in outbound_flights:
        for inbound_flight in inbound_flights:
            total_cost = outbound_flight.price + inbound_flight.price
            round_trip_options.append((outbound_airline, outbound_flight, inbound_airline, inbound_flight, total_cost))

    return round_trip_options

    """# Case 1: Both outbound and inbound flights are from WizzAir
    for out_flight in outbound:
        for in_flight in inbound:
            total_cost.append((out_flight.airline, out_flight, in_flight, out_flight.price + in_flight.price))

    # Case 2: Both outbound and inbound flights are from RyanAir
    for out_flight in outbound:
        for in_flight in inbound:
            total_cost.append((out_flight.airline, out_flight, in_flight, out_flight.price + in_flight.price))

    # Case 3: Outbound flight is from WizzAir and inbound flight is from RyanAir
    for out_flight in outbound:
        for in_flight in inbound:
            total_cost.append((out_flight.airline, out_flight, in_flight, out_flight.price + in_flight.price))

    # Case 4: Outbound flight is from RyanAir and inbound flight is from WizzAir
    for out_flight in outbound:
        for in_flight in inbound:
            total_cost.append((out_flight.airline, out_flight, in_flight, out_flight.price + in_flight.price))"""

    # Sort the total costs in ascending order
    #total_cost.sort()

    # Return the lowest total cost found
    #return total_cost