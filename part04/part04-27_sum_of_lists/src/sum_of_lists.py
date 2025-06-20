def list_sum(list1: list[int], list2: list[int]) -> list[int]:
    return [x + y for x, y in zip(list1, list2)]