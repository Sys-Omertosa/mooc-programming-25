def same_chars(text, i, j):
    if i < 0 or i >= len(text) or j < 0 or j >= len(text):
        return False

    if text[i] == text[j]:
        return True
    return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))