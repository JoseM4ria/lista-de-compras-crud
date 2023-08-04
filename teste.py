def lu_decomposition(matrix):

    m = len(matrix)

    n = len(matrix[0])

    L = [[0.0] * n for _ in range(m)]

    U = [[0.0] * n for _ in range(m)]


    for i in range(m):

        L[i][i] = 1.0


        for j in range(i+1):

            s1 = sum(U[k][i] * L[j][k] for k in range(j))

            U[j][i] = matrix[j][i] - s1


        for j in range(i, m):

            s2 = sum(U[k][i] * L[j][k] for k in range(i))

            L[j][i] = (matrix[j][i] - s2) / U[i][i]


    return L, U


def lu_solve(L, U, b):

    m = len(b)

    n = len(U[0])

    y = [0.0] * n

    x = [0.0] * n


    # Solving Ly = b

    for i in range(n):

        y[i] = b[i]

        for j in range(i):

            y[i] -= L[i][j] * y[j]

        y[i] /= L[i][i]


    # Solving Ux = y

    for i in range(n-1, -1, -1):

        x[i] = y[i]

        for j in range(i+1, n):

            x[i] -= U[i][j] * x[j]

        x[i] /= U[i][i]


    return x


# Solicitar a matriz de entrada do usuário

m = int(input("Digite o número de linhas da matriz: "))

n = int(input("Digite o número de colunas da matriz: "))


matrix = []

for i in range(m):

    row = list(map(float, input(f"Digite os elementos da linha {i+1}: ").split()))

    matrix.append(row)


# Solicitar o vetor de termos independentes do usuário

b = list(map(float, input("Digite os elementos do vetor de termos independentes: ").split()))


L, U = lu_decomposition(matrix)

x = lu_solve(L, U, b)


print("Matriz L:")

for row in L:
    formatedList = [f"{item:.2f}" for item in row]
    print(formatedList)


print("Matriz U:")

for row in U:
    formatedList = [f"{item:.2f}" for item in row]
    print(formatedList)

print("Solução:")
formated_x = [f"{item:.2f}" for item in x]
print(formated_x)
