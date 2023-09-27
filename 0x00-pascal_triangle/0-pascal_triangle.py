def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal's triangle of n."""
    if n <= 0:
        return []
    
    pascal_triangle = [[1]]

    for i in range(1, n):
        new_row = []

        new_row.append(1)

        for j in range(len(pascal_triangle[i - 1]) - 1):
            new_row.append(pascal_triangle[i - 1][j] + pascal_triangle[i - 1][j + 1])
        
        new_row.append(1)

        pascal_triangle.append(new_row)
        
    return pascal_triangle
