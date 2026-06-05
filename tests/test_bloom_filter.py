from bloom_filter import BloomFilter

def test_added_words_are_found():
    bf = BloomFilter(1000, 0.01)

    words = ["apple", "banana", "orange", "mango"]

    for word in words:
        bf.add(word)

    for word in words:
        assert bf.contains(word) == True

def test_word_not_added():
    bf = BloomFilter(1000, 0.01)

    bf.add("apple")
    bf.add("banana")

    # this word was not added, so it should normally be false
    assert bf.contains("car") == False

def test_counter_works():
    bf = BloomFilter(1000, 0.01)

    bf.add("apple")
    bf.add("banana")
    bf.add("orange")

    assert bf.items_added == 3

def test_bit_array_changes():
    bf = BloomFilter(1000, 0.01)

    before = sum(bf.bit_array)

    bf.add("apple")

    after = sum(bf.bit_array)

    assert after > before

# ratio test

# invalid input test

