def sort(arr):

    if  len(arr) <= 1:
        return arr
    
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]
        else:
            return arr

    m = int(len(arr)/2)

    arr1 = sort(arr[:m])
    arr2 = sort(arr[m:])

    arr = merge(arr1, arr2)

    return arr

def merge(arr1, arr2):
    i, j, k = 0, 0, 0
    arr = []

    while i < len(arr1) and j <len(arr2):
        if arr1[i] < arr2[j]:
            arr.append (arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1 
        k += 1
    
    if i == len(arr1):
        while j < len(arr2):
            arr.append(arr2[j])
            j +=1
    
    if j == len(arr2):
        while i < len(arr1):
            arr.append(arr1[i])
            i += 1

    return arr


print(sort([9,8,7,7,6,5,9,8,5,6]))