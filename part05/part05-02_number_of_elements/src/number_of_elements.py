def count_matching_elements(my_matrix, element):
    return sum(1 for row in my_matrix for col in row if col == element)