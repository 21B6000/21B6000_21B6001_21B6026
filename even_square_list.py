list = [1, 2, 3, 4, 5, 6]

def even_square_list(list):
    number = []
    for num in list:
        if num % 2 == 0:
            number.append(num ** 2)
    return number

final = even_square_list(list)

print(final)