import os
import pickle

def _init_etc(path, data):
    with open(path, "wb") as f:
        pickle.dump(data, f)

def _remove_file_in_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

base_dir = os.path.dirname(os.path.abspath(__file__))
start_path = os.path.join(base_dir, "..", "_primes_data", "etc", "start.pkl")
start_key_path = os.path.join(base_dir, "..", "_primes_data", "etc", "start_key.pkl")
numbering_path = os.path.join(base_dir, "..", "_primes_data", "etc", "numbering.pkl")
primes_list_path = os.path.join(base_dir, "..", "_primes_data", "_primes_list")
primes_tuple_path = os.path.join(base_dir, "..", "_primes_data", "_primes_tuple")
primes_dict_path = os.path.join(base_dir, "..", "_primes_data", "_primes_dict")
primes_set_path = os.path.join(base_dir, "..", "_primes_data", "_primes_set")

_init_etc(start_path)
_init_etc(start_key_path)
_init_etc(numbering_path)
_remove_file_in_folder(primes_list_path)
_remove_file_in_folder(primes_tuple_path)
_remove_file_in_folder(primes_dict_path)
_remove_file_in_folder(primes_set_path)