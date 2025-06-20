def length_of_longest(my_list : list[str]) -> int:
    longest = 0
    for string in my_list:
        if len(string) > longest:
            longest = len(string)
    return longest