class Flight:
    """A flight with a particular passenger aircraft"""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError('No airline code in "{}"'.format(number))

        if not number[:2].isupper():
            raise ValueError('Invalid Airline Code {0}', number)
        if not (number[2:].isnumeric() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number {0}", number)

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter:None for letter in seats} for _ in rows ]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger

        Args:
            seat: A seat designator auch as '12C' or '21F'

        Raises:
            ValueError ; If the seat is unavailable
        """
        """
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {0}", letter)

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {0}", row_text)

        if row not in rows:
            raise ValueError('Invalid row number {0}.', row)
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError('Seat {0} is already occupied.', seat)

        self._seating[row][letter] = passenger

    def _parse_seat(self, seat):
        """ Parse a sear designator into a valid row and letter
        Args:
            seat: A seat designator such as 12F
        Returns :
            A tuple containing an integer and a string for row and seat.
        """
        row_numbers, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}", letter)
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError('Invalid Seat Row {}', row_text)

        if row not in row_numbers:
            raise ValueError('Invalid row number {}', row)

        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError('No passenger to relocate in seat {}', from_seat)

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError('Seat {} already occupied', to_seat)
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_pass(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, '{}{}'.format(row, letter))


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                'ABCDEFGHJK'[:self._num_seats_per_row])


def make_flight():
    f = Flight('BA758', Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_seats_per_row=6))
    f.allocate_seat('12A', 'Dipangshu banik')
    f.allocate_seat('15F', 'Roina banik')
    f.allocate_seat('1A', 'Dipanjan banik')
    f.allocate_seat('12B', 'Dipak Banik')
    f.allocate_seat('12C', 'Arpita banik')
    f.allocate_seat('12D', 'Kabita banik')
    return f


def console_card_printer(passenger, seat, flight_number, aircraft):
    output= '| Name: {0}'       \
            '   Flight: {1}'    \
            '   Seat: {2}'      \
            '   Aircraft; {3}'  \
            '   |'.format(passenger, flight_number, seat, aircraft)
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()
