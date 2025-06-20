def distinct_numbers(my_list : list[int]) -> list[int]:
    distinct_list = []
    for x in my_list:
        if not x in distinct_list:
            distinct_list.append(x)
    return sorted(distinct_list)
    # Or just use a set:
    # return sorted(set(my_list))