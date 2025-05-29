**Fixed Code:**

```python
def reverse_linked_list(node):
    prevnode = None
    currentnode = node  # Initialize currentnode to node
    while currentnode:
        nextnode = currentnode.successor
        currentnode.successor = prevnode
        prevnode = currentnode
        currentnode = nextnode
    return prevnode
```

**Explanation of the fix:**

The original code was missing the update of `prevnode`. Also, the original code was missing the initialization of `currentnode`. The `while` loop condition `node` was using the original `node` which was never updated, causing an infinite loop if the list was not empty. I have added `currentnode = node` to initialize `currentnode` to the head of the list. Also, I have replaced `node` with `currentnode` in the while loop and inside the loop. This ensures that the loop iterates through the list correctly, updating the `successor` pointers and moving to the next node until the end of the list is reached. Finally, `prevnode` is returned, which will be the new head of the reversed list.