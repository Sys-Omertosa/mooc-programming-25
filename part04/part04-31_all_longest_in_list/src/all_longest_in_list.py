def all_the_longest(my_list : list[str]) -> list[str]:
    longest = max(my_list, key=len)
    return [string for string in my_list if len(string) == len(longest)]