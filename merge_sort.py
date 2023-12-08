def merge_sort(arr):
    if len(arr) == 0:
        return
    if len(arr) > 1:
        mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid//2:]
    merge_sort(left)
    merge_sort(right)

    i=0
    j=0
    k=0
    
    while i< len(left) and j < len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            k+=1
            i+=1
        else:
            arr[k]=right[j]
            k+=1
            j+=1
    while i < len(left):
        arr[k]= left[i]
        k+=1
        i+=1
    while j < len(right):
        arr[k] = right[j]
        j+=1
        k+=1
    return arr

