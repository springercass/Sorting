# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        current_index = i
        smallest_element = current_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        for v in range(current_index + 1, len(arr)):
            if arr[v] < arr[smallest_element]:
                smallest_element = v

        # TO-DO: swap
        temp = arr[smallest_element]
        arr[smallest_element] = arr[current_index]
        arr[current_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    repeat = True
    while repeat == True:
        repeat = False
        for v in range(0, len(arr) - 1):
            current_index = v
            next_v = current_index + 1

            if arr[current_index] > arr[next_v]:
                print(arr[current_index], ">", arr[next_v])
                alt_v = arr[next_v]
                arr[next_v] = arr[current_index]
                arr[current_index] = alt_v
                repeat = True
            else:
                print(arr[current_index], "<", arr[next_v])

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
