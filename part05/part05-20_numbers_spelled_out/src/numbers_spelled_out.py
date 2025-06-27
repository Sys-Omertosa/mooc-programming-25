def dict_of_numbers():
    dictionary = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
                  6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
                  11:'eleven', 12:'twelve'}
    for key in range(13, 20):
        if key == 13:
            dictionary[key] = 'thirteen'
        elif key == 15:
            dictionary[key] = 'fifteen'
        elif key == 18:
            dictionary[key] = 'eighteen'
        else:
            dictionary[key] = dictionary[key%10] + 'teen'

    for key in range(20, 100):
        if key % 10 == 0:
            if key // 10 == 2:
                dictionary[key] = 'twenty'
            elif key // 10 == 3:
                dictionary[key] = 'thirty'
            elif key // 10 == 4:
                dictionary[key] = 'forty'
            elif key // 10 == 5:
                dictionary[key] = 'fifty'
            elif key // 10 == 8:
                dictionary[key] = 'eighty'
            else:
                dictionary[key] = dictionary[key//10] + 'ty'
            continue

        dictionary[key] = dictionary[(key//10)*10] + '-' + dictionary[key%10]

    return dictionary


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers)
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])