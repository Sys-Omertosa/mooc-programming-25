def find_words(search_term):
    word_list = []
    length = len(search_term)
    with open("words.txt") as file:
        for word in file:
            word = word.strip()
            if search_term[0] == "*":
                if word.endswith(search_term[1:]):
                    word_list.append(word)
            elif search_term[-1] == "*":
                if word.startswith(search_term[:-1]):
                    word_list.append(word)
            elif len(word) == length:
                    for i in range(length):
                        if search_term[i] != "." and search_term[i] != word[i]:
                            break
                    else:
                        word_list.append(word)
    return word_list

print(find_words(".a.e"))