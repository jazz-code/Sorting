# TO-DO: Complete the selection_sort() function below
l = [2, 6, 3, 9, 7, 8 ]

def selection_sort(arr):
    # loop through n-1 elements
    for i in range(1, len(arr)):
        temp = arr[i]
        smallest_index = i
        # print( smallest_index < arr[temp - 1])

        # Iterate to the left until you find the correct index in the "sorted" part of the array,
        # at which this element should be inserted
        while smallest_index > 0 and temp < arr[smallest_index - 1]:
            # Shift items over to the right as you iterate
            arr[smallest_index] = arr[smallest_index - 1]
            smallest_index -= 1
        #TO-DO: swap
        arr[smallest_index] = temp

    return arr

print(selection_sort(l))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr