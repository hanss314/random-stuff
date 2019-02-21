import itertools
import random
import sys

from typing import List, Any

sys.setrecursionlimit(10000)


def perms(A: List[int]) -> List[List[int]]:
    """A! all permutations of A"""
    return list(map(list, itertools.permutations(A)))


def is_sorted(L: List[int]) -> bool:
    """Test if list is sorted for bogosort"""
    return all(L[i] <= L[i+1] for i in range(len(L) - 1))


def bogosort(L: List[int]) -> List[int]:
    """shuffles list until it's sorted"""
    L = L.copy()
    while not is_sorted(L):
        random.shuffle(L)

    return L

def list_order_sort(order: List[int], L: List[Any], k: int) -> List[Any]:
    """{...}-sort(L, k)"""
    print(order, L, k)
    L, order = L.copy(), order.copy()
    if len(order) == 1 and order[0] == 0 and k == 0:
        return bogosort(L)
    elif len(order) == 1 and k != 0:
        return list_order_sort(order, perms(L), k-1)[0]
    elif order[-1] == 0:
        return list_order_sort(order[:-1], L, k)
    elif k == 0:
        new_order = []
        for n, x in enumerate(order):
            if x == 0: new_order.append(len(L))
            else:
                new_order.append(x-1)
                new_order.extend(order[n+1:])
                break

        return list_order_sort(new_order, L, len(L))

    else:
        return list_order_sort(order, perms(L), k-1)[0]

def pessimalsort(L: List[int]) -> List[int]:
    return list_order_sort(L, L, len(L))


print(pessimalsort([2, 1]))