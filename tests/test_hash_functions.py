from bloom_filter import BloomFilter

def test_hash_positions_are_valid():
    bf = BloomFilter(1000, 0.01)

    positions = bf.get_hash_positions("apple")

    # every position should be inside the bit array
    for position in positions:
        assert 0 <= position < bf.size

def test_same_word_same_hashes():
    bf = BloomFilter(1000, 0.01)

    positions1 = bf.get_hash_positions("banana")
    positions2 = bf.get_hash_positions("banana")

    # hashing the same word twice should give the same result
    assert positions1 == positions2

def test_different_words_not_same_hashes():
    bf = BloomFilter(1000, 0.01)

    positions1 = bf.get_hash_positions("apple")
    positions2 = bf.get_hash_positions("orange")

    # different words should usually not give exactly the same positions
    assert positions1 != positions2

def test_hashes_for_words_and_dna():
    bf = BloomFilter(1000, 0.01)

    words = ["apple", "banana", "orange", "mango", "pear"]
    dna_sequences = ["ATCG", "GATTACA", "CCGTTA", "TTGGCA", "AACCGG"]

    all_items = words + dna_sequences

    for item in all_items:
        positions = bf.get_hash_positions(item)

        assert len(positions) == bf.number_of_hashes

        for position in positions:
            assert 0 <= position < bf.size