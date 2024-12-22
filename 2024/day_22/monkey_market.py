import math

class MonkeyMarket:
    def __init__(self, number, n_numbers):
        self.number = number
        self.n_numbers = n_numbers

    def get_last_secret_number(self):
        secret_number = self.number

        for i in range(self.n_numbers):
            secret_number = self.get_secret_number(secret_number)

        return secret_number

    def get_change_sequences(self):
        secret_number = self.number
        price_changes = []
        price_changes_sequence = {}
        last_price = 0

        for i in range(self.n_numbers):
            secret_number = self.get_secret_number(secret_number)
            price = secret_number % 10

            price_changes.append(price - last_price)

            if i >= 4:
                key = ((price_changes[i-3],price_changes[i-2]), (price_changes[i-1],price_changes[i]))

                if key not in price_changes_sequence:
                    price_changes_sequence[key] = price

            last_price = price

        return price_changes_sequence

    def get_secret_number(self, number):
        number = self.prune(self.mix(number * 64, number))
        number = self.prune(self.mix(number // 32, number))
        number = self.prune(self.mix(number * 2048, number))

        return number

    def mix(self, value, secret_number):
        return value ^ secret_number

    def prune(self, secret_number):
        return secret_number % 16777216

