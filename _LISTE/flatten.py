import numpy as np


def flatten_any(input_list: list) -> list:
    np_list = np.array(input_list)
    flattened = np_list.flatten()
    return list(flattened)


list_2d = [[1, 2], [3, 4]]
list_3d = [[[1, 2], [3, 4], [5, 6]]]
list_4d = [
    [
        [
            [1, 2], [3, 4], [5, 6], [7, 8]
        ]
    ]
]


print(np.array(list_4d))
print(flatten_any(list_4d))
