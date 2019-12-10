
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
        for temp in range(i + 1, len(arr)):
            # print("i         : ", i)
            # print("arr[temp] : ",arr[temp])
            # print("arr[small]: ",arr[smallest_index])
            # print("******")
            if arr[temp] < arr[smallest_index]:
                # print("if-arr[temp] : ",arr[temp])
                # print("if-arr[small]: ",arr[smallest_index])
                # print("******")
                smallest_index = temp
                # print("temp",(temp))
                # print("small",(smallest_index))
                # print("******")
                # l = [4, 22, 2, 6, 3, 9, 7, 8, 30 ]
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
# print(selection_sort(l))

# TO-DO: Complete the insertion_sort() function below

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

    # Loop through your array
        # Compare each element to its neighbor
        # If elements in wrong position (relative to each other, swap them)
    # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

# (start at the beginning and compare each element to its right hand neighbor. If the right hand neighbor is smaller, we swap the two neighbors.)
l = [2, 6, 3, 9, 7, 8 ]
def bubble_sort( arr ):
    # result = []
    for i in range(len(arr) -1):
        # index = i
        # print("arr-i",arr[i])
        # print("index+1 ",arr[index + 1])
        # print("********")
        for i in range(i + 1, len(arr) -1):
            if arr[i] > arr[i + 1]:
                # print("if-arr",arr[i])
                # print("********")
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        # for x in range(i + 1, len(arr))
    return arr
    # if arr[]
# a[0:2]
# print(bubble_sort(l))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr