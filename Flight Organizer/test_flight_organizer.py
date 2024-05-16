import unittest
from flight import Flight
from flight_organizer import FlightOrganizer

class TestFlightOrganizer(unittest.TestCase):
    def setUp(self):
        self.organizer = FlightOrganizer()

    def test_2_nights_in_Barcelona(self):
        options = self.organizer.get_cheapest_round_trip()
        for option in options:
            airline, outbound_flight, inbound_flight, total_cost = option
            # Check if the stay in Barcelona is for 2 nights
            self.assertTrue(self.organizer._is_two_nights_stay(outbound_flight, inbound_flight))

    def test_combining_flights(self):
        options = self.organizer.get_cheapest_round_trip()

        # Variables to track if each scenario is covered
        wizzair_outbound = False
        wizzair_inbound = False
        ryanair_outbound = False
        ryanair_inbound = False

        for option in options:
            airline, outbound_flight, inbound_flight, total_cost = option

            # Check if WizzAir is used for both outbound and inbound flights
            if airline == "WizzAir":
                wizzair_outbound = True
                wizzair_inbound = True

            # Check if RyanAir is used for both outbound and inbound flights
            elif airline == "RyanAir":
                ryanair_outbound = True
                ryanair_inbound = True

            # Check if WizzAir is used for outbound and RyanAir for inbound
            elif airline == ("WizzAir", "RyanAir"):
                wizzair_outbound = True
                ryanair_inbound = True

            # Check if RyanAir is used for outbound and WizzAir for inbound
            elif airline == ("RyanAir", "WizzAir"):
                ryanair_outbound = True
                wizzair_inbound = True

        # Check if all scenarios are covered
        self.assertTrue(wizzair_outbound and wizzair_inbound)
        self.assertTrue(ryanair_outbound and ryanair_inbound)
        self.assertTrue(wizzair_outbound and ryanair_inbound)
        self.assertTrue(ryanair_outbound and wizzair_inbound)
        """options = self.organizer.get_cheapest_round_trip()
        for option in options:
            airline, outbound_flight, inbound_flight, total_cost = option
            # Check if outbound and inbound flights are from different airlines
            self.assertNotEqual(outbound_flight.airline, inbound_flight.airline)"""

    def test_cheapest_total_flight(self):
        # Initialize FlightOrganizer object
        flight_organizer = FlightOrganizer()

        # Run the flight organizer to get all options
        options = flight_organizer.get_cheapest_round_trip()

        # Find the lowest cost option
        lowest_cost_option = min(options, key=lambda x: x[3])

        # Check if the total cost is less than the lowest cost option
        self.assertLessEqual(options[0][3], lowest_cost_option[3])

if __name__ == '__main__':
    unittest.main()