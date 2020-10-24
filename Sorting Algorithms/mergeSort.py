def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) / 2
        L = arr[mid:]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[i]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1
    
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[i]
        j += 1
        k += 1


A = [52, 583, 3584, 242, 5803, 62, 53, 54, 55, 52]

print("Array before sorting :", A)
A = mergeSort(A)
print("Array after sorting :", A)
