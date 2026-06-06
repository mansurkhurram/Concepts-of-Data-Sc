import mmh3
from bitarray import bitarray
import math

class BloomFilter:
    def __init__(self, expected_items, false_positive_rate):
        if expected_items <= 0:
            raise ValueError("expected_items must be positive")

        if false_positive_rate <= 0 or false_positive_rate >= 1:
            raise ValueError("false_positive_rate must be between 0 and 1")

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

        self.count = 0

    def get_hash_positions(self, item):
        if not isinstance(item, (str, bytes)):
            item = str(item)
            
        h1 = mmh3.hash(item, seed=0, signed=False)
        h2 = mmh3.hash(item, seed=1, signed=False)
        
        return [(h1 + i * h2) % self.size for i in range(self.number_of_hashes)]

    def insert(self, item):
        positions = self.get_hash_positions(item)

        # set all hash positions to 1
        for position in positions:
            self.bit_array[position] = 1

        self.count += 1

    def search(self, item):
        positions = self.get_hash_positions(item)

        # if one position is still 0, the item was not added
        for position in positions:
            if self.bit_array[position] == 0:
                return False

        # if all positions are 1, the item is probably there
        return True

    def fill_ratio(self):
        # tells us how full the bit array is
        return sum(self.bit_array) / self.size

    @property
    def current_fp_rate(self):
        k = self.number_of_hashes
        n = self.count
        m = self.size

        return (1 - math.exp((-k * n) / m)) ** k

    def memory_usage_bytes(self):
        # bit array size is in bits, so divide by 8 for bytes
        return self.size / 8
    
    @property
    def compression_ratio(self):
        if self.count == 0:
            return 0.0
        return (self.size / 8) / (self.count * 6)