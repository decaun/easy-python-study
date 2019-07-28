"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def find(missing, dest):
    found_list = []
    found_mul = 1
    for i in range(2, dest):
        while dest % i == 0:
            dest /= i
            found_list.append(i)
    found_list.append(dest)

    for i in found_list:
        if missing % i != 0:
            found_mul *= i
        else:
            missing /= i
    return found_mul


def seq_gen(var):
    result = 1
    for i in reversed(range(1, var)):
        if result % i == 0:
            pass
        else:
            result *= find(result, i)
            #print("current {}, wanted {}, return {}".format(result,i,find(result,i)))
    return int(result)


if __name__ == "__main__":
    print(seq_gen(20))


# print(seq_gen(10))
