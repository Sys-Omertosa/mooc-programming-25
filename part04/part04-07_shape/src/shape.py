def line(width, text):
    if not text:
        print("*" * width)
    else:
        print(text[0] * width)


def triangle(height, character):
    for i in range(1, height + 1):
        line(i, character)


def rectangle(width, height, character):
    for i in range(1, height + 1):
        line(width, character)


def shape(height, tri_char, rec_width, rec_char):
    triangle(height, tri_char)
    rectangle(height, rec_width, rec_char)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")