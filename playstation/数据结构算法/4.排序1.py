# coding:utf-8
from typing import List
# Bubble
def bubble_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return a
    for i in range(length):
        for j in range(i + 1, length):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

# 插入
def insertion_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return []
    for i in range(1, length):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


# 选择
def selection_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return []

    for i in range(length):
        min_index = i
        min_value = a[i]
        for j in range(i, length):
            if a[j] < min_value:
                min_index = j
                min_value = a[j]
        a[i], a[min_index] = a[min_index], a[i]


# test
def test_buuble_sort():
    test_array = [1, 1, 1, 1]
    bubble_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    bubble_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    bubble_sort(test_array)
    assert test_array == [1, 2, 3, 4]


def test_insertion_sort():
    test_array = [1, 1, 1, 1]
    insertion_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    insertion_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    insertion_sort(test_array)
    assert test_array == [1, 2, 3, 4]


def test_selection_sort():
    test_array = [1, 1, 1, 1]
    selection_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    selection_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    selection_sort(test_array)
    assert test_array == [1, 2, 3, 4]


if __name__ == "__main__":
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    bubble_sort(array)
    print(array)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    insertion_sort(array)
    print(array)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    selection_sort(array)
    print(array)
