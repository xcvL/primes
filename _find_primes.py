from _find_primes_func import _primes_in_range_segmented

def better_print_set(s):
    print("{")
    for v in sorted(s):
        print(f"    {v},")
    print("}")

def better_print_dict(d):
    print("{")
    for k, v in d.items():
        print(f"    {k}: {v},")
    print("}")


start = 50000
end = start + 5000
keys_start = 4675

primes_list = _primes_in_range_segmented(start, end)
keys = list(range(keys_start + 1, len(primes_list) + keys_start + 1))

primes_dict = dict(zip(keys, primes_list))
primes_set = set(primes_list)

while True:
    cmd = input("cmd: ")
    if cmd == "d":
        better_print_dict(primes_dict)
    elif cmd == "s":
        better_print_set(primes_set)
    elif cmd == "exit":
        break
    print()