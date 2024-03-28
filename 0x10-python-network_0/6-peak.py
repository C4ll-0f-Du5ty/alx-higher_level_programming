#!/usr/bin/python3
def find_peak(list_of_integers):
    """Finding The Peak Number"""
    if not list_of_integers:
        return None

    k = len(list_of_integers) - 1
    start, end = 0, k
    while start <= end:
        mid = start + (end - start) // 2
        if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            end = mid - 1
        elif mid < k and list_of_integers[mid] < list_of_integers[mid + 1]:
            start = mid + 1
        else:
            return list_of_integers[mid]
