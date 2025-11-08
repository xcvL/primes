from prime_func import segmented_sieve_n
import pickle

n = 1_000_000

# start = 1 (initial value)
with open("_primes_data/etc/start.pkl", "rb") as f:
    start = pickle.load(f)[0]

# start_key = 1 (initial value)
with open("_primes_data/etc/start_key.pkl", "rb") as f:
    start_key = pickle.load(f)[0]

# numbering = 0 (initial value)
with open("_primes_data/etc/numbering.pkl", "rb") as f:
    numbering = pickle.load(f)[0]

primes = segmented_sieve_n(start, n)

primes_list = list(primes)
primes_tuple = tuple(primes)
primes_dict = dict(zip(list(range(start_key, start_key + n)), primes_list))
primes_set = set(primes)

with open(f"_primes_data/_primes_list/primes_list{numbering}.pkl", "wb") as f:
    pickle.dump(primes_list, f)

with open(f"_primes_data/_primes_tuple/primes_tuple{numbering}.pkl", "wb") as f:
    pickle.dump(primes_tuple, f)

with open(f"_primes_data/_primes_dict/primes_dict{numbering}.pkl", "wb") as f:
    pickle.dump(primes_dict, f)

with open(f"_primes_data/_primes_set/primes_set{numbering}.pkl", "wb") as f:
    pickle.dump(primes_set, f)

with open("_primes_data/etc/start.pkl", "wb") as f:
    pickle.dump([primes_list[-1]], f)

with open("_primes_data/etc/start_key.pkl", "wb") as f:
    pickle.dump([n + 1], f)

with open("_primes_data/etc/numbering.pkl", "wb") as f:
    pickle.dump([numbering + 1], f)