import hashlib
import math


class BloomFilter:
    def __init__(self, expected_items, false_positive_rate):
        self.expected_items = expected_items
        self.false_positive_rate = false_positive_rate

        # size of the bit array
        self.size = math.ceil(
            -(expected_items * math.log(false_positive_rate)) / (math.log(2) ** 2)
        )

        # number of hash functions
        self.number_of_hashes = math.ceil(
            (self.size / expected_items) * math.log(2)
        )

        # start with all bits set to 0
        self.bit_array = [0] * self.size

        self.items_added = 0

    def get_hash_positions(self, item):
        positions = []

        # same item, but slightly changed each time using i
        # this gives us different hash positions
        for i in range(self.number_of_hashes):
            text = str(item) + str(i)
            hash_result = hashlib.sha256(text.encode()).hexdigest()
            position = int(hash_result, 16) % self.size

            positions.append(position)

        return positions

    def add(self, item):
        positions = self.get_hash_positions(item)

        # set all hash positions to 1
        for position in positions:
            self.bit_array[position] = 1

        self.items_added += 1

    def contains(self, item):
        positions = self.get_hash_positions(item)

        # if one position is still 0, the item was not added
        for position in positions:
            if self.bit_array[position] == 0:
                return False

        # if all positions are 1, the item is probably there
        return True