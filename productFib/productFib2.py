def product_lib(prod):
    solution = []
    first, second = 0, 1
    while True:
        if first * second == prod:
            solution = [first, second, True]
            break
        elif first * second > prod:
            solution = [first, second, False]
            break
        first, second = second, first + second

    return solution

if __name__ == '__main__':
    assert product_lib(4895) == [55, 89, True]
    assert product_lib(5895) == [89, 144, False]