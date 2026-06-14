# Concepts of Data Science Project

## Team Members

- Mansoor Khurram
- Muhammad Ismail

## What is this?

This is our implementation of a Bloom filter in Python for the Concepts of Data Science course. A Bloom filter is a probabilistic data structure that lets you check if something is in a set without actually storing the elements. It uses way less memory than a regular set, the trade-off being that it can sometimes say an item is in the set when it isn't (false positive). It will never say something isn't there when it actually is though (no false negatives).

## Files

- `bloom_filter.py` — the Bloom filter class
- `tests/test_bloom_filter.py` — correctness tests
- `tests/test_hash_functions.py` — hash function tests
- `analysis.ipynb` — notebook with demo, complexity discussion, and analysis
- `benchmark.py` — times insert and search for increasing dataset sizes, to be run on HPC
- `script.sh` — job script used to run the benchmark on VSC
- `benchmark_results.txt` — output from the HPC benchmark run
- `benchmark_plot.png` — plot of insert and search times
- `fp_rate_plot.png` — false positive rate vs number of inserted elements
- `compression_ratio_plot.png` — compression ratio vs capacity and fp rate
- `environment.yml` — conda environment to reproduce our setup

## Setup

```bash
conda env create -f environment.yml
conda activate bloom
```

## Running the tests

```bash
python -m pytest
```

## Benchmarks

The benchmarks were run on the VSC HPC cluster (Vlaams Supercomputer Centrum). We timed insert and search for dataset sizes ranging from 1,000 to 1,000,000 elements.

To reproduce the results on VSC:
```bash
# 1. connect to VSC
ssh <your_vsc_id>@login.hpc.ugent.be
 
# 2. upload files from your local machine (not from SSH)
scp bloom_filter.py benchmark.py script.sh <your_vsc_id>@login.hpc.ugent.be:~/
 
# 3. set up the environment on VSC
conda create -n bloom python=3.10 -y
conda activate bloom
pip install mmh3 bitarray matplotlib
 
# 4. submit the job
qsub script.sh
 
# 5. check job status
qstat
 
# 6. download results back to your local machine
scp <your_vsc_id>@login.hpc.ugent.be:~/benchmark_results.txt .
scp <your_vsc_id>@login.hpc.ugent.be:~/benchmark_plot.png .
```
 
The results are already included in this repository in `benchmark_results.txt` and `benchmark_plot.png`.

## Conclusions

**Hash functions** — we used MurmurHash3 with double hashing which gives good distribution for both natural language words and DNA strings. The positions spread well across the bit array for both data types.

**Time complexity** — insert and search both run in O(k) time where k is the number of hash functions. Since k is fixed when you create the filter, both operations are basically O(1) per element. The benchmark results confirm this — both insert and search scale linearly with n, and the times are nearly identical to each other at every size (e.g. at 1 million elements, insert took 2.11s and search took 2.13s). This makes sense since both operations do the exact same thing — compute k hash positions and read or write the bits.

**Space complexity** — O(n) space. The filter only stores bits, not the actual elements, so it's much more memory efficient than a regular set or list.

**False positive rate** — the filter stayed well below the 1% target while under capacity. Once we went past 1000 elements it crossed the target line and kept climbing, reaching around 16% at 2000 elements (2x capacity). The measured rate follows the theoretical curve closely which means our implementation matches what the math predicts.

**Compression ratio** — all four false positive rates we tested (0.1%, 1%, 5%, 10%) gave compression ratios well below 1.0, meaning the filter always uses less memory than storing the raw strings. The ratio stays flat across all capacities which makes sense since both the filter size and the raw data size scale linearly with n. A stricter false positive rate (0.1%) gave a ratio of around 0.30, while a looser one (10%) gave around 0.09 — so the less accurate you're willing to be, the more memory you save.