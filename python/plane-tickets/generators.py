"""Functions to automate Conda airlines ticketing system."""


SEATS = ["A", "B", "C", "D"]

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    current_seat = 0
    while current_seat < number:
        yield SEATS[current_seat % len(SEATS)]
        current_seat += 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seat_letters = generate_seat_letters(number)
    row = 0
    while number > 0:
        seat_letter = next(seat_letters)
        if seat_letter == SEATS[0]:
            row += 1
            if row == 13:
                row += 1

        yield f"{row}{seat_letter}"
        number -= 1


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seats = list(generate_seats(len(passengers)))
    return dict(zip(passengers, seats))


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        seat_flight = f"{seat}{flight_id}"
        yield f"{seat_flight:0<12}"
