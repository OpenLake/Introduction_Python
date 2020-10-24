def heapSort(arr):
    n = len(arr)
    for i in range(n / 2 - 1, -1, -1):
        heapify(arr, i, n)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[i], arr[0]
        heapify(arr, 0, i)

def heapify(arr, n, i):
    largest = i
    l = 2 * i 
    r = 2 * i + 1

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[r] < arr[largest]:
        largest = r

    if largest == i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

A = [52, 583, 3584, 242, 5803, 62, 53, 54, 55, 52]

print("Array before sorting :", A)
A = heapSort(A)
print("Array after sorting :", A)
