import math

def binary_search(target,arr):
    min = 0
    max = len(arr)-1

    while min <= max:
        mid = math.floor((min+max)/2)
        print(arr[min:max])
        if arr[mid]==target:
            return mid
        elif arr[mid] < target:
            min = mid+1
        else:
            max = mid -1
    return -1

lista = [1,2,3,4,5,6,7,8,9,10]

target = 4

print(binary_search(target,lista))
