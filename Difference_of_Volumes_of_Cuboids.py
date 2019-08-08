import numpy as np

class Difference_of_Volumes_of_Cuboids():
    a = [0] * 3

    for i in range(len(a)):
        i = str(i + 1)
        print("Input " + i)
        i = int(i)
        i = i - 1
        a[i] = int(input())
    v1 = reduce(lambda x, y: x * y, a)
    b = [0] * 3
    for i in range(len(b)):
        i = str(i + 1)
        print("Input " + i)
        i = int(i)
        i = i - 1
        b[i] = int(input())
    v2 = reduce(lambda x, y: x * y, b)

    print(np.math.fabs(v1-v2))
