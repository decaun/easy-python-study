def get_squares_gen(n):  # generator approach
    for x in range(n):
        yield x ** 2  # we yield, we don't return


if __name__ == "__main__":

    result = get_squares_gen(5)
    print(result)
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print(result.__next__())
