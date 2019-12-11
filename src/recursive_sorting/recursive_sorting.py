# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for x in arrA:
        if arrA[0] <= arrB[1]:
            # merged_arr.insert(0, x)
            merged_arr.append(x)
        # else:

    return merged_arr
    # for x in merged_arr:
    #     merged_arr.append(x + 1)
    #     return merged_arr
a = [1,2,3]
b = [4,5]
c = [1,2,3,4,5,6]
# print([len(c) // 2])
# print(merge(a, b))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # base case
    if len(arr) > 1:
    # divide arr by half until len = 1
        mid = (len(arr) // 2)
        left = arr[:mid]
        right = arr[mid:]
        # Recursive calls
        merge_sort(left)
        merge_sort(right)
        # print(left)
        # print(right)
        # 2 iterators for traversing left / right
        l = 0
        r = 0

        # main counter iterator for arr
        a = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                # Left half used
                arr[a] = left[l]
                l += 1
            else:
                arr[a] = right[r]
                r += 1
            # Move to next slot
            a += 1
        # All remaining values
        while l < len(left):
            arr[a] = left[l]
            l += 1
            a += 1

        while r < len(right):
            arr[a] = right[r]
            r += 1
            a += 1

    return arr
        # for x in arr:
        #     if x < mid:
        #         left.append(x)
        #     else:
        #         right.append(x)

        # print(left)
        # print(right)
        # # merge_sort(left)
        # # merge_sort(right)

        # merge = left + right
        # print("len",[len(arr) // 2])
        # print("arr", arr)
        # return merge_sort([len(arr) // 2])
        # return merge_sort( arr + [len(arr) // 2])

    # return merge_sort([len(arr) // 2])

# print(merge_sort([]))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
