def binary_search(arr,tar):
    low = 0
    high = len(arr)
    while low < high:
        mid = low + ((high -low )//2)
        if arr[mid] == tar:
            return mid
        elif arr[mid]  < tar:
            low = mid+1
        elif arr[mid] > tar :
            high = mid-1
    return -1
