def invert(dictionary):
    keys = list(dictionary.keys())

    for key in keys:
        dictionary[dictionary[key]] = key
        del dictionary[key]