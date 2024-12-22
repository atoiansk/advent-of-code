import math

class MonkeyMarket:
    def __init__(self, number, n_numbers):
        self.number = number
        self.n_numbers = n_numbers

    def get_secret_number(self):
        secret_number = self.number

        for i in range(self.n_numbers):
            secret_number = self.prune(self.mix(secret_number * 64, secret_number))
            secret_number = self.prune(self.mix(secret_number // 32, secret_number))
            secret_number = self.prune(self.mix(secret_number * 2048, secret_number))

        return secret_number

    def mix(self, value, secret_number):
        return value ^ secret_number

    def prune(self, secret_number):
        return secret_number % 16777216

