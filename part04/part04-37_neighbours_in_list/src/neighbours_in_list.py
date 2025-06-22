def longest_series_of_neighbours(my_list : list[int]) -> int:
    max_longest = 0
    longest = 0
    for i in range(len(my_list)-1):
        if abs(my_list[i] - my_list[i+1]) != 1:
            longest = 0
            continue
        longest += 1
        if max_longest < longest:
            max_longest = longest
    return max_longest+1

if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))