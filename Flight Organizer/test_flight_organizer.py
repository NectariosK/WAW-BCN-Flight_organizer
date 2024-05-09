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

    def test_combining_flights_from_different_airlines(self):
        options = self.organizer.get_cheapest_round_trip()
        for option in options:
            airline, outbound_flight, inbound_flight, total_cost = option
            # Check if flights are from different airlines
            self.assertNotEqual(outbound_flight.airline, inbound_flight.airline)

    def test_cheapest_total_flight(self):
        options = self.organizer.get_cheapest_round_trip()
        lowest_cost_option = min(options, key=lambda x: x[3])
        for option in options:
            airline, outbound_flight, inbound_flight, total_cost = option
            # Ensure all options are cheaper than the lowest cost option
            self.assertLess(total_cost, lowest_cost_option[3])

    """def test_get_cheapest_flights(self):
        expected_result = [("WizzAir", "RyanAir", 425.98), ("RyanAir", "WizzAir", 420.52)]
        result = self.organizer.get_cheapest_round_trip()
        self.assertEqual(result, expected_result)

    def test_get_flights_with_layover(self):
        expected_result = [("WizzAir", "RyanAir", "15:50-18:55", "10:50-14:10", 675.98),
                           ("RyanAir", "WizzAir", "18:25-21:30", "06:15-09:20", 420.52)]
        result = self.organizer.get_flights_with_layover()
        self.assertEqual(result, expected_result)"""

if __name__ == '__main__':
    unittest.main()