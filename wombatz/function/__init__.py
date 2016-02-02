def has_negative(seq):
    for i in seq:
        if i < 0:
            return True
    return False


def has_larger_than(value, seq):
    for i in seq:
        if i > value:
            return True
    return False
