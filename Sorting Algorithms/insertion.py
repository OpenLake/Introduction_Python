A = [52, 583, 3584, 242, 5803, 62, 53, 54, 55, 52]

def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    return

print("Array before sorting :", A)
A = insertionSort(A)
print("Array after sorting :", A)
