def filter_solutions():
    corr_list = []
    incorr_list = []

    with open("solutions.csv") as sols_file:
        for line in sols_file:
            parts = line.strip().split(";")
            if eval(parts[1]) == int(parts[2]):
                corr_list.append(line)
            else:
                incorr_list.append(line)

    with open("correct.csv", "w") as corr_file:
        for line in corr_list:
            corr_file.write(line)

    with open("incorrect.csv", "w") as incorr_file:
        for line in incorr_list:
            incorr_file.write(line)


if __name__ == '__main__':
    filter_solutions()