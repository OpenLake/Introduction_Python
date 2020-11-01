#Implementation of Insertion Sort using python3

#Array to be sorted
A = [52, 583, 3584, 242, 5803, 62, 53, 54, 55, 52]

#Function to do insertion sort
def insertionSort(arr):

    #Traverse through array index
    for i in range(len(arr)):
        key = arr[i]

        #Move elements of arr[0..i-1], greater than key
        #to one position ahead of current position
        j = i-1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j - 1] = key
    return 


#Printing unsorted array
print("Array before sorting :", A)

A = insertionSort(A)

#Printing sorted array
print("Array after sorting :", A)
