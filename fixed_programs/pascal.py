def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = []
        row.append(1)  # First element of each row is always 1
        for c in range(1, r):
            upleft = rows[r - 1][c - 1]
            upright = rows[r - 1][c]
            row.append(upleft + upright)
        row.append(1) # Last element of each row is always 1
        rows.append(row)

    return rows
