import numpy as np

class Difference_of_Volumes_of_Cuboids():
    arr1 = [4, 6, 11, 24, 12, 1, 10]
    n = len(arr1)

    def pendulumArrangement(arr1, n):
    # sorting the elements
        arr = np.sort(arr1, axis=0)
    # the second array
        op = [0] * n
    # middle index
        mid = int((n - 1) / 2)
        j = 1
        i = 1
        op[mid] = arr[0]

        for i in range(1, mid + 1):
            op[mid + i] = arr[j]
            j += 1
            op[mid - i] = arr[j]
            j += 1
    # elements is even
        if (int(n % 2) == 0):
            op[mid + i] = arr[j]
    # Printing
        print("Pendulum list:")
        for i in range(0, n):
            print(op[i])

    pendulumArrangement(arr1, n)
