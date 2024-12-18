from __future__ import annotations

from typing import TypeVar

T = TypeVar("T", int, float)


def selection_sort(arr: list[T]) -> None:
    for i, _num in enumerate(arr):
        minimum = _num
        index = i
        for j in range(i, len(arr)):
            if minimum > arr[j]:
                index = j
                minimum = arr[j]
        arr[i], arr[index] = arr[index], _num


if __name__ == "__main__":
    arr = [1, 2, 4, 2, 1]
    selection_sort(arr)
    print(arr)
