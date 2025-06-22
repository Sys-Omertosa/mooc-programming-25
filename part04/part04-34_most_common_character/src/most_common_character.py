def most_common_character(text : str) -> str:
    return max(text, key=text.count)

if __name__ == '__main__':
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))