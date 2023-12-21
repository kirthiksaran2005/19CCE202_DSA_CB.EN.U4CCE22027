def floyd_warshall(C):
    n = len(C)
    A = [row[:] for row in C]

    print("Initial Matrix:")
    print_matrix(A)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]

        print(f"\nIntermediate Matrix after Iteration {k + 1}:")
        print_matrix(A)

    return A

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Example Usage:
inf = float('inf')

# Example adjacency matrix (C)
C = [
    [0, 3, inf, 7],
    [8, 0, 2, inf],
    [5, inf, 0, 1],
    [2, inf, inf, 0]
]

result = floyd_warshall(C)

# Output the final resulting matrix
print("\nFinal Result Matrix:")
print_matrix(result)
