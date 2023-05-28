# this line take input from user
def num_format(n):
    n_list = list(str(n))
    num_len = len(n_list)
    if num_len == 4 or num_len == 5:
        n_list.insert(-3, ',')
        print("".join(n_list))
    elif num_len == 6 or num_len == 7:
        n_list.insert(-3, ",")
        n_list.insert(-6, ",")
        print("".join(n_list))
    elif num_len == 8 or num_len == 9:
        n_list.insert(-3, ",")
        n_list.insert(-6, ",")
        n_list.insert(-9, ",")
        print("".join(n_list))
    elif num_len == 10 or num_len == 11:
        n_list.insert(-3, ",")
        n_list.insert(-6, ",")
        n_list.insert(-9, ",")
        n_list.insert(-12, ",")
        print("".join(n_list))
    elif num_len == 12 or num_len == 13:
        n_list.insert(-3, ",")
        n_list.insert(-6, ",")
        n_list.insert(-9, ",")
        n_list.insert(-12, ",")
        n_list.insert(-15,",")
        print("".join(n_list))
    elif num_len == 14 or num_len == 15:
        n_list.insert(-3, ",")
        n_list.insert(-6, ",")
        n_list.insert(-9, ",")
        n_list.insert(-12, ",")
        n_list.insert(-15,",")
        n_list.insert(-18,",")
        print("".join(n_list))
    elif num_len == 16 or num_len == 17:
        n_list.insert(-3, ",")
        n_list.insert(-6, ",")
        n_list.insert(-9, ",")
        n_list.insert(-12, ",")
        n_list.insert(-15,",")
        n_list.insert(-18,",")
        n_list.insert(-21,",")
        print("".join(n_list))
    else:
        exit()
