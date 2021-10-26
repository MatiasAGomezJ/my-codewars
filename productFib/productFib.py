def product_lib(prod):
    solution = []
    first = 0
    second = 1
    while True:
        if first * second == prod:
            solution = [first, second, True]
            break
        elif first * second > prod:
            solution = [first, second, False]
            break
        temp = first
        first = second
        second = temp + second

    return solution

if __name__ == '__main__':
    assert product_lib(4895) == [55, 89, True]
    assert product_lib(5895) == [89, 144, False]