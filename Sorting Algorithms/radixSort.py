def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(1, n):
        index = (arr[i] // exp1)
        count[index % 10] += 1

    for i in range(10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i = 0
    for i in range(1, len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    temp = max(arr)
    exp = 1
    while temp / exp > 0:
        countingSort(arr, exp)
        exp *= 10


arr = [170, 45, 75, 90, 802, 24, 2, 66]

print(arr)
radixSort(arr)
print("After sorting : ", arr)
