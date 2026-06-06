# Concepts of Data Science Project

## Team Members

- Mansoor Khurram
- Muhammad Ismail

## Project Description

The goal of this project is to implement a Bloom filter in Python. A Bloom filter is a probabilistic data structure for checking set membership. It can tell you whether an item is definitely not in a set, or possibly in it.

The trade-off is false positives: occasionally an item that was never added will appear to be present. But it won't produce false negatives which means if you added something, the filter will always recognize it.

## Repository Structure

```text
.
├── bloom_filter.py
├── tests/
│   └── test_bloom_filter.py
├── README.md
└── .gitignore
```

## Running the Tests

The tests are written using `pytest`.

To run the tests, first make sure you are in the main project folder:

Then run:

```bash
python -m pytest
```

This command runs all tests inside the `tests/` folder.

## Hash Function Tests

The Bloom filter uses SHA-256 to create hash positions. Different numbers are added to the item before hashing, so one item can give several hash positions.

The hash function tests check that:

- the positions are inside the bit array
- the same item gives the same positions every time
- different items usually do not give the exact same positions
- the hash function works for normal words and DNA-like strings

