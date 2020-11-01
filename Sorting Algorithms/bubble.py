A = [52, 583, 3584, 242, 5803, 62, 53, 54, 55, 52]


def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return 0

print("Array before sorting :", A)
bubbleSort(A)
print("Array after sorting :", A)
