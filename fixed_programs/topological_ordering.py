def topological_ordering(nodes):
    ordered_nodes = [node for node in nodes if not node.incoming_nodes]
    
    visited = set(ordered_nodes)  # Keep track of visited nodes to avoid infinite loops

    for node in ordered_nodes:
        for nextnode in node.outgoing_nodes:
            if nextnode not in visited:  # Check if nextnode has already been visited
                incoming_nodes_in_ordered = True
                for incoming in nextnode.incoming_nodes:
                    if incoming not in ordered_nodes:
                        incoming_nodes_in_ordered = False
                        break
                if incoming_nodes_in_ordered:
                    ordered_nodes.append(nextnode)
                    visited.add(nextnode) # Mark nextnode as visited

    return ordered_nodes
