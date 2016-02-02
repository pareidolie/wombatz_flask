from itertools import combinations
from operator import itemgetter


def _quality_combinations(items):
    items.sort()
    for length in range(2, len(items) + 1):
        for combination in map(list, combinations(items, length)):
            summed = sum(combination)
            if summed >= 40:
                yield summed, tuple(combination)


def _item_equal(value):
    def inner(other):
        return other[0] == value
    return inner


def _item_len(item):
    return len(item[1])


def quality_combinations(items):
    if 20 in items:
        return 20, [20]
    all_combination = list(_quality_combinations(items))
    if not all_combination:
        return None

    best_sum = min(all_combination, key=itemgetter(0))[0]
    best_combinations = list(filter(_item_equal(best_sum), all_combination))
    best_combinations.sort(key=_item_len)
    return best_combinations[0]


if __name__ == '__main__':
    q = quality_combinations([7, 7, 7, 7, 7, 7, 5, 20, 20])
    print(q)