def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                arr[i],arr[j] = arr[j],arr[i]

