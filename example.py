#считаем оазисы в пустыне
def print_array(input_array):
    for i in range(0, len(input_array)):
            for j in range(0, len(input_array[i])):
                print(input_array[i][j], end=' ')
            print()

def seach_water(x, i, j):
    if (i + 1) < len(x) and x[i+1][j] == 1:
        x[i+1][j] = 2
        seach_water(x, i + 1, j)
    if (i - 1) >= 0 and x[i - 1][j] == 1:
        x[i - 1][j] = 2
        seach_water(x, i - 1, j)
    if (j + 1) < len(x[i]) and x[i][j + 1] == 1:
        x[i][j + 1] = 2
        seach_water(x, i, j + 1)
    if (j - 1) >= 0 and x[i][j - 1] == 1:
        x[i][j - 1] = 2
        seach_water(x, i, j - 1)
    return

def func_down_right(x):
    count = 0
    for i in range(0, len(x) - 1):
        for j in range(0, len(x) - 1):
            if x[i][j] == 1:
                x[i][j] = 2
                count += 1
                seach_water(x, i, j)
    return count

# матрица для подсчета оазисов в пустыне
arr1 = [[0,0,1,0,0,1,0,0],
        [0,1,1,1,0,1,1,0],
        [0,0,1,1,0,0,1,0],
        [0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0],
        [0,1,1,0,0,1,1,0],
        [0,0,0,0,1,1,0,0],
        [0,1,0,0,1,1,0,0],
        [0,1,0,0,0,1,0,0]
        ]

print_array(arr1)
print("Количество оазисов: ", func_down_right(arr1))
print_array(arr1)