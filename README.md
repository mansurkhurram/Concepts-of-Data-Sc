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

