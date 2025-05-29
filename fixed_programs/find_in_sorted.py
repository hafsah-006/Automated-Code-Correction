**Fixed Code:**

```python
def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(mid + 1, end)
        else:
            return mid

    return binsearch(0, len(arr))
```

**Explanation of the fix:**

The original code had a potential issue in the `binsearch` function when recursively searching the right half of the array. The line `return binsearch(mid, end)` would cause an infinite loop if `x` was greater than `arr[mid]` but also the first element in the right sub-array. The fix is to change this line to `return binsearch(mid + 1, end)`. This ensures that the `mid` element is excluded from the next search, preventing the infinite loop and ensuring the search progresses correctly.