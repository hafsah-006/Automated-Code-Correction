**Fixed Code:**

```python
def depth_first_search(startnode, goalnode):
    nodesvisited = set()
 
    def search_from(node):
        if node in nodesvisited:
            return False
        elif node is goalnode:
            return True
        else:
            nodesvisited.add(node) # Missing initialization
            return any(
                search_from(nextnode) for nextnode in node.successors
            )

    return search_from(startnode)
```

**Explanation of the fix:**

The original code was missing a crucial step: adding the current `node` to the `nodesvisited` set *before* exploring its successors.  Without this, the algorithm would not correctly track visited nodes, potentially leading to infinite loops in cyclic graphs or redundant exploration of paths.

The fix `nodesvisited.add(node)` ensures that the current node is marked as visited *before* the recursive calls to `search_from` are made for its successors. This prevents the algorithm from revisiting the same node along the same path, ensuring correct DFS traversal and termination.