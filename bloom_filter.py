import math

class BloomFilter:
    def __init__(self, expected_items, false_positive_rate):
        self.expected_items = expected_items
        self.false_positive_rate = false_positive_rate

        self.size = math.ceil(
            -(expected_items * math.log(false_positive_rate)) / (math.log(2) ** 2)
        )

        self.number_of_hashes = math.ceil(
            (self.size / expected_items) * math.log(2)
        )

        self.bit_array = [0] * self.size
        self.items_added = 0