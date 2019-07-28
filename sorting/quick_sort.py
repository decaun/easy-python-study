# https://github.com/OmkarPathak/Data-Structures-using-Python/blob/master/Sorting


def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        temp = partition(array, low, high)

        quick_sort(array, low, temp - 1)
        quick_sort(array, temp + 1, high)
