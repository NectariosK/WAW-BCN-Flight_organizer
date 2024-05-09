from datetime import datetime

class Flight:
    def __init__(self, airline, direction, departure_time, arrival_time, price, date_str):
        self.airline = airline
        self.direction = direction
        self.departure_time = datetime.strptime(departure_time, "%H:%M")
        self.arrival_time = datetime.strptime(arrival_time, "%H:%M")
        self.price = price
        self.date = datetime.strptime(date_str, "%A %d %b %Y")

def get_total_cost(outbound, inbound):
    total_cost = {}
    for out_flight in outbound:
        for in_flight in inbound:
            if out_flight.airline != in_flight.airline:
                total_cost[(out_flight.airline, in_flight.airline)] = out_flight.price + in_flight.price
    return total_cost

def get_flights():
    flights = {
        "WizzAir": {
            "outbound": [
                Flight("WizzAir", "outbound", "15:50", "18:55", 220, "Friday 7 Jun 2024"),
                Flight("WizzAir", "outbound", "15:50", "18:55", 200, "Saturday 7 Jun 2024"),
                Flight("WizzAir", "outbound", "07:05", "10:10", 470, "Sunday 9 Jun 2024"),
                Flight("WizzAir", "outbound", "15:50", "18:55", 270, "Sunday 9 Jun 2024"),
                Flight("WizzAir", "outbound", "06:30", "09:40", 310, "Monday 10 Jun 2024"),
                Flight("WizzAir", "outbound", "15:50", "18:55", 270, "Monday 10 Jun 2024"),
                Flight("WizzAir", "outbound", "15:50", "18:55", 200, "Tuesday 11 Jun 2024"),
                Flight("WizzAir", "outbound", "06:30", "09:40", 180, "Wednesday 12 Jun 2024"),
                Flight("WizzAir", "outbound", "15:50", "18:55", 160, "Wednesday 12 Jun 2024"),
                Flight("WizzAir", "outbound", "07:10", "10:15", 250, "Thursday 13 Jun 2024"),
                Flight("WizzAir", "outbound", "15:50", "18:55", 270, "Thursday 13 Jun 2024"),
                Flight("WizzAir", "outbound", "06:15", "09:20", 310, "Friday 14 Jun 2024"),
                Flight("WizzAir", "outbound", "15:50", "18:55", 360, "Friday 14 Jun 2024"),
                Flight("WizzAir", "outbound", "15:50", "18:55", 270, "Saturday 15 Jun 2024"),
                Flight("WizzAir", "outbound", "06:10", "09:15", 310, "Sunday 16 Jun 2024"),
                Flight("WizzAir", "outbound", "15:50", "18:55", 270, "Sunday 16 Jun 2024"),
                Flight("WizzAir", "outbound", "15:50", "18:55", 360, "Monday 17 Jun 2024"),
                Flight("WizzAir", "outbound", "15:50", "18:55", 310, "Tuesday 18 Jun 2024"),
                Flight("WizzAir", "outbound", "15:50", "18:55", 200, "Wednesday 19 Jun 2024"),
                Flight("WizzAir", "outbound", "07:10", "10:15", 360, "Thursday 20 Jun 2024"),
                Flight("WizzAir", "outbound", "15:50", "18:55", 310, "Thursday 20 Jun 2024"),
            ],
            "inbound": [
                Flight("WizzAir", "inbound", "10:50", "14:10", 250, "Sunday 9 Jun 2024"),
                Flight("WizzAir", "inbound", "19:40", "22:45", 270, "Sunday 9 Jun 2024"),
                Flight("WizzAir", "inbound", "10:30", "13:30", 250, "Monday 10 Jun 2024"),
                Flight("WizzAir", "inbound", "19:40", "22:45", 270, "Monday 10 Jun 2024"),
                Flight("WizzAir", "inbound", "19:40", "22:45", 630, "Tuesday 11 Jun 2024"),
                Flight("WizzAir", "inbound", "10:50", "14:10", 220, "Wednesday 12 Jun 2024"),
                Flight("WizzAir", "inbound", "19:40", "22:45", 310, "Wednesday 12 Jun 2024"),
                Flight("WizzAir", "inbound", "10:55", "13:50", 250, "Thursday 13 Jun 2024"),
                Flight("WizzAir", "inbound", "19:40", "22:45", 220, "Thursday 13 Jun 2024"),
                Flight("WizzAir", "inbound", "10:10", "13:15", 250, "Friday 14 Jun 2024"),
                Flight("WizzAir", "inbound", "19:40", "22:45", 270, "Friday 14 Jun 2024"),
                Flight("WizzAir", "inbound", "19:40", "22:45", 310, "Saturday 15 Jun 2024"),
                Flight("WizzAir", "inbound", "09:55", "13:00", 470, "Sunday 16 Jun 2024"),
                Flight("WizzAir", "inbound", "19:40", "22:45", 630, "Sunday 16 Jun 2024"),
                Flight("WizzAir", "inbound", "19:40", "22:45", 400, "Monday 17 Jun 2024"),
                Flight("WizzAir", "inbound", "19:40", "22:45", 270, "Tuesday 18 Jun 2024"),
                Flight("WizzAir", "inbound", "19:40", "22:45", 270, "Wednesday 19 Jun 2024"),
                Flight("WizzAir", "inbound", "10:55", "13:50", 310, "Thursday 20 Jun 2024"),
                Flight("WizzAir", "inbound", "19:40", "22:45", 270, "Thursday 20 Jun 2024"),
            ]
        },
        "RyanAir": {
            "outbound": [
                Flight("RyanAir", "outbound", "18:25", "21:30", 205.98, "Friday 7 Jun 2024"),
                Flight("RyanAir", "outbound", "16:10", "19:15", 245.72, "Saturday 7 Jun 2024"),
                Flight("RyanAir", "outbound", "09:45", "12:50", 319.02, "Sunday 9 Jun 2024"),
                Flight("RyanAir", "outbound", "18:20", "21:25", 250.03, "Tuesday 11 Jun 2024"),
                Flight("RyanAir", "outbound", "17:15", "20:20", 176.38, "Wednesday 12 Jun 2024"),
                Flight("RyanAir", "outbound", "18:25", "21:30", 177.71, "Friday 14 Jun 2024"),
                Flight("RyanAir", "outbound", "16:10", "19:15", 293.15, "Saturday 15 Jun 2024"),
                Flight("RyanAir", "outbound", "09:45", "12:50", 213, "Sunday 16 Jun 2024"),
                Flight("RyanAir", "outbound", "18:25", "21:30", 258.65, "Tuesday 18 Jun 2024"),
            ],
            "inbound": [
                Flight("RyanAir", "inbound", "06:15", "09:20", 215.54, "Sunday 9 Jun 2024"),
                Flight("RyanAir", "inbound", "14:50", "17:55", 222.26, "Tuesday 11 Jun 2024"),
                Flight("RyanAir", "inbound", "13:45", "16:50", 310.39, "Wednesday 12 Jun 2024"),
                Flight("RyanAir", "inbound", "14:55", "18:00", 327.64, "Friday 14 Jun 2024"),
                Flight("RyanAir", "inbound", "12:40", "15:45", 363.32, "Saturday 15 Jun 2024"),
                Flight("RyanAir", "inbound", "06:15", "09:20", 259.33, "Sunday 16 Jun 2024"),
                Flight("RyanAir", "inbound", "14:50", "17:55", 448.36, "Tuesday 18 Jun 2024"),
                Flight("RyanAir", "inbound", "13:45", "16:50", 330.96, "Wednesday 19 Jun 2024"),
            ]
        }
    }
    return flights
