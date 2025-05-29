def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr[1:] if x < pivot]
    above = [x for x in arr[1:] if x > pivot]

    num_less = len(below)


    if k < num_less:
        return kth(below, k)
    elif k == num_less:
        return pivot
    else:
        return kth(above, k - num_less -1)
