from heapq import  heappush, heappop


def heap_sort(data: list[int]) -> list[int]:
    heap: list[int] = []
    for elem in data:
        heappush(heap, elem)
    result: list[int] = []
    while heap:
        result.append(heappop(heap))
    return result


if __name__ == '__main__':
    print(heap_sort([7, 1, 0, 6, 2, 8, 5, 9, 3, 4, 5]))
