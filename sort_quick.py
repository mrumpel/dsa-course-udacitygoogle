def sort(arr):
    quick_sort_step(arr, 0, len(arr)-1)

def quick_sort_step(arr, start, end):
    if start == -1 or end == len(arr) or start >= end:
        return
    
    if end - start == 1:
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
            return
        else:
            return

    p = end
    i = start

    while i < p:
        if arr[i] > arr[p]:
            arr[p], arr[i], arr[p-1] = arr[i], arr[p-1], arr[p]
            p -= 1
        else:
            i += 1
    
    quick_sort_step(arr, start, p-1)
    quick_sort_step(arr, p+1, end)

arr = [9,8,7,7,6,5,9,8,5,6]
sort(arr)
print(arr)