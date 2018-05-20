class Flight:

    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError('No airline code in "{}"'.format(number))

        if not number[:2].isupper():
            raise ValueError('Invalid Airline Code {0}', number)
        if not (number[2:].isnumeric() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number {0}", number)

        self._number = number

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]



class Aircraft:
    def __init__(self, registration, model, num_rows, ):
