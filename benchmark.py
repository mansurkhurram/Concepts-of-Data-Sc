import time
import random
import string
import matplotlib.pyplot as plt
from bloom_filter import BloomFilter

def random_word():
    length = random.randint(4, 10)
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# number of elements to test at each step
sizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]

insert_times = []
search_times = []

for n in sizes:
    words = [random_word() for _ in range(n)]
    bf = BloomFilter(expected_items=n, false_positive_rate=0.01)

    # time how long inserting n words takes
    t0 = time.time()
    for w in words:
        bf.insert(w)
    insert_times.append(time.time() - t0)

    # time how long searching for those same words takes
    t0 = time.time()
    for w in words:
        bf.search(w)
    search_times.append(time.time() - t0)

    print(f"n={n}: insert={insert_times[-1]:.4f}s  search={search_times[-1]:.4f}s")

# write results to a file
with open("benchmark_results.txt", "w") as f:
    for n, ins, sea in zip(sizes, insert_times, search_times):
        f.write(f"n={n}  insert={ins:.4f}s  search={sea:.4f}s\n")


plt.figure(figsize=(9, 5))
plt.plot(sizes, insert_times, marker="o", label="insert", color="steelblue")
plt.plot(sizes, search_times, marker="o", label="search", color="tomato")
plt.xlabel("number of elements")
plt.ylabel("time (seconds)")
plt.title("Bloom Filter — Insert & Search Time")
plt.xscale("log")
plt.legend()
plt.tight_layout()
plt.savefig("benchmark_plot.png", dpi=150)