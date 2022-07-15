# Types to flatten 2D list to 1D list
# Input: [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


data = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]

# method 1 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
flat_list_1 = [x for xs in data for x in xs]
print("\nFlatten by Method 1(for loop): ", flat_list_1)


# method 2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def flatten_data(xss):
    return [x for xs in xss for x in xs]  # same mtd 1, but with function


flat_list_2 = flatten_data(data)
print("\nFlatten by Method 2(function): ", flat_list_2)

# method 3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import itertools

flat_list_3 = list(itertools.chain(*data))
print("\nFlatten by Method 3(itertools 1): ", flat_list_3)

# method 4 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import itertools

flat_list_4 = list(itertools.chain.from_iterable(data))
print("\nFlatten by Method 4(itertools 2): ", flat_list_4)

# method 5 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
flat_list_5 = sum(data, [])
print("\nFlatten by Method 5(sum): ", flat_list_5)

# method 6 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import functools
import operator

flat_list_6 = functools.reduce(operator.iconcat, data, [])
print("\nFlatten by Method 6(functools): ", flat_list_6)

# method 7 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
flat_list_7 = []
for sublist in data:
    flat_list_7.extend(sublist)
print("\nFlatten by Method 7(extend): ", flat_list_7)

# method 8 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from typing import Iterable # from collections import Iterable                            # < py38


def flatten(items):
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x


flat_list_8 = list(flatten(data))

# complicated example
comp_data = [[1, [2]], (3, 4, {5, 6}, 7), 8, "9"]
flat_list_8_check = list(flatten(comp_data))
print("\nFlatten by Method 8(Iterable): ", flat_list_8)
print("Flatten by Method 8(Iterable) all kind & 3D to 1D: ", flat_list_8_check)

# method 9 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from functools import reduce
flat_list_9 = reduce(lambda xs, ys: xs + ys, data)
print("\nFlatten by Method 9(reduce): ", flat_list_9)


# method 10 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from functools import reduce
import operator
flat_list_10 = reduce(operator.concat, data)
print("\nFlatten by Method 10(operator.concat): ", flat_list_10)
