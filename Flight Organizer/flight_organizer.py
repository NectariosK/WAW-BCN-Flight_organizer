from data import get_flights


class FlightOrganizer:
    def __init__(self, flights_data):
        self.flights_data = flights_data
        #self.flights = self._load_flights()

    def get_cheapest_round_trip(self):
        all_round_trip_options = []

        # Scenario 1: WizzAir for both outbound and inbound flights
        self._add_round_trip_options("WizzAir", "WizzAir", all_round_trip_options)

        # Scenario 2: RyanAir for both outbound and inbound flights
        self._add_round_trip_options("RyanAir", "RyanAir", all_round_trip_options)

        # Scenario 3: WizzAir outbound, RyanAir inbound
        self._add_round_trip_options("WizzAir", "RyanAir", all_round_trip_options)

        # Scenario 4: RyanAir outbound, WizzAir inbound
        self._add_round_trip_options("RyanAir", "WizzAir", all_round_trip_options)

        # Sort round trip options by total cost
        all_round_trip_options.sort(key=lambda x: x[3])

        return all_round_trip_options

    def get_outbound_flights(self, airline):
        if airline in self.flights_data:
            return self.flights_data[airline]["outbound"]
        else:
            return []

    def get_inbound_flights(self, airline):
        if airline in self.flights_data:
            return self.flights_data[airline]["inbound"]
        else:
            return []

    def get_total_cost(self, outbound_flight, inbound_flight):
        return outbound_flight.cost + inbound_flight.cost

    def _add_round_trip_options(self, outbound_airline, inbound_airline, options_list):
        outbound_flights = self.flights_data[outbound_airline]["outbound"]
        inbound_flights = self.flights_data[inbound_airline]["inbound"]

        for outbound_flight in outbound_flights:
            for inbound_flight in inbound_flights:
                if self._is_two_nights_stay(outbound_flight, inbound_flight):
                    total_cost = self.get_total_cost(outbound_flight, inbound_flight)
                    options_list.append((outbound_airline, outbound_flight, inbound_airline, inbound_flight, total_cost))

    def _is_two_nights_stay(self, outbound_flight, inbound_flight):
        outbound_date = outbound_flight.date
        inbound_date = inbound_flight.date
        return (inbound_date - outbound_date).days == 2