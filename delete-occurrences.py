def delete_nth(order,max_e):
    index = 0
    while index < len(order):
        if order[:index].count(order[index]) == max_e:
            del order[index]
            index -= 1
        index += 1
    return order
