def shortest(my_list : list[str]) -> str:
    shortest = my_list[0]
    for string in my_list:
        if len(string) < len(shortest):
            shortest = string
    return shortest
    # This can literally be done in one line:
    # return min(my_list, key=len)