import pickle
import os
from typing import List, Tuple, Dict, Set, Type, Union

CollectionType = Union[list, tuple, dict, set]
IntInCollectionType = Union[List[int], Tuple[int, ...], Dict[int, int], Set[int]]

def _load(filename: str) -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "..", "_primes_data", "_primes_list", filename)
    with open(path, "rb") as f:
        pickle.load(f)

def _load_range(data_box: List, load_range: Tuple[int, int], piece_of_filename: str) -> List[IntInCollectionType]:
    for i in range(load_range[0], load_range[1]):
        data_box.append(_load(f"primes_{piece_of_filename}{i}.pkl"))


def primes(data_type: Type[CollectionType], index: int) -> None:
    if data_type == list:
        _load(f"primes_list{index}.pkl")
    elif data_type == tuple:
        _load(f"primes_tuple{index}.pkl")
    elif data_type == dict:
        _load(f"primes_dict{index}.pkl")
    elif data_type == set:
        _load(f"primes_set{index}.pkl")

def primes_range(data_type: Type[CollectionType], index_range: Tuple[int, int]) -> List[IntInCollectionType]:
    all_data = []
    if data_type == list:
        _load_range(all_data, index_range, "list")
    elif data_type == tuple:
        _load_range(all_data, index_range, "tuple")
    elif data_type == dict:
        _load_range(all_data, index_range, "dict")
    elif data_type == set:
        _load_range(all_data, index_range, "set")