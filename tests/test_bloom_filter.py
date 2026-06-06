from bloom_filter import BloomFilter

def test_added_words_are_found():
    bf = BloomFilter(1000, 0.01)

    words = ["apple", "banana", "orange", "mango"]

    for word in words:
        bf.insert(word)

    for word in words:
        assert bf.search(word) == True

def test_word_not_added():
    bf = BloomFilter(1000, 0.01)

    bf.insert("apple")
    bf.insert("banana")

    # this word was not added, so it should normally be false
    assert bf.search("car") == False

def test_counter_works():
    bf = BloomFilter(1000, 0.01)

    bf.insert("apple")
    bf.insert("banana")
    bf.insert("orange")

    assert bf.count == 3

def test_bit_array_changes():
    bf = BloomFilter(1000, 0.01)

    before = sum(bf.bit_array)

    bf.insert("apple")

    after = sum(bf.bit_array)

    assert after > before

def test_fill_ratio():
    bf = BloomFilter(1000, 0.01)

    bf.insert("apple")
    bf.insert("banana")

    ratio = bf.fill_ratio()

    assert ratio > 0
    assert ratio < 1

def test_wrong_inputs():
    try:
        BloomFilter(0, 0.01)
        assert False
    except ValueError:
        assert True

    try:
        BloomFilter(1000, 2)
        assert False
    except ValueError:
        assert True

