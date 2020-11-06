def order_weight(string):

    def sort_by(list):
        return sum([int(x) for x in list])

    string_list = sorted(string.strip().split(' '))

    return_list = sorted(string_list, key=sort_by)

    return " ".join(return_list)
