
# Start with current index = 0

# For all indices EXCEPT the last index:

    # a. Loop through elements on right-hand-side of current index and find the smallest element

    # b. Swap the element at current index with the smallest element found in above loop

# For every index in the collection from 0 to length-2:

# Compare the element at the current index, i, with everything on its right to identify the position of the smallest element

# Swap the element at i with the smallest element
# i++

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # print("i",i)
        # print("arr",arr[cur_index - 1])
        # print("curr",arr[cur_index])
        # print("small",arr[smallest_index])
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # print(i < arr[cur_index -1])
        # if i < arr[cur_index -1]:
        #         # print("curr",arr[cur_index])
        #         # print("i",i)
        #         i,arr[cur_index] = arr[cur_index], i
        #         print("curr",arr[cur_index])
        #         print("i",i)
        #         i += i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                print(j)

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr
        # while arr[cur_index - 1] > 0:
        #     smallest_index = min(arr)
        #     print(smallest_index)
        #     print(cur_index)
        #     arr[cur_index] = arr[smallest_index]
        #     cur_index += 1
        #     return





l = [4, 22, 2, 6, 3, 9, 7, 8, 30 ]
print(selection_sort(l))

# TO-DO: Complete the selection_sort() function below

def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        cur_index = i
        # print( cur_index < arr[temp - 1])

        # Iterate to the left until you find the correct index in the "sorted"
        # part of the array at which this element should be inserted
        while cur_index > 0 and temp < arr[cur_index - 1]:
            # Shift items over to the right as you iterate
            arr[cur_index] = arr[cur_index - 1]
            cur_index -= 1

        arr[cur_index] = temp

    return arr

l = [2, 6, 3, 9, 7, 8 ]
# print(insertion_sort(l))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    return
    # for i in range(len(arr)):
    #     while
# a[0:2]
# bubble_sort(l)
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr