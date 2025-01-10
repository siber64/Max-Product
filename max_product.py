from functools import reduce
from typing import Iterable


def max_product(numbers:Iterable[int], target:int):

    s = sorted(numbers, key=lambda n: abs(n), reverse=True)
    p = reduce(lambda x, y: x * y, s[:target]) if s else None

    if not p or p >= 0 or target == len(numbers):
        return p
    else:
        max_negative_used = next((x for x in reversed(s[:target]) if x < 0), None)
        max_positive_unused = next((x for x in s[target:] if x > 0), None)
        min_positive_unused = next((x for x in s[:target] if x > 0), None)
        min_negative_unused = next((x for x in s[target:] if x < 0), None)

        new_p_1 = None if max_positive_unused is None\
            else (p // max_negative_used) * max_positive_unused

        new_p_2 = None if min_positive_unused is None\
            else (p // min_positive_unused) * min_negative_unused

        if new_p_1 is None and new_p_2 is None:
            return reduce(lambda x, y: x * y, s[len(s)-target:])
        elif new_p_1 is None:
            return new_p_2
        elif new_p_2 is None:
            return new_p_1
        else:
            return max(new_p_1, new_p_2)

calls = (((-10, -6, -5, 4, -2, -1), 3, 240),
         ((-10, -6, -5, 4, 3,-2, -1), 4, 720),
         ((-10, -6, -5, -2, -1), 3, -10),
         ((5, 3, 3), 3, 45),
         ((5, 3, 2, 0), 4, 0),
         ((5, 3, 2, 0), 3, 30),
         ((5,), 1, 5),
         ((-5,), 1, -5),
         ((), 0, None),
         )

for call in calls:
    print (f"Calculated: {max_product(call[0], call[1])}, Expected: {call[2]}")

