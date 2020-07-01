# Recursive merge sort

#Aux array to do the merge

def merge_sort(array):
    global temp
    temp = [None] * len(array)
    merge_sort_recursive(array, 0, len(array)-1)

def merge_sort_recursive(array, l, r):
    if (l < r):
        mid = l + (r-l)//2
        merge_sort_recursive(array, l, mid)
        merge_sort_recursive(array, mid+1, r)
        # if the half is sorted dont call merge()
        if (array[mid] <= array[mid+1]):
            return
        merge(array, l, r, mid)

def merge(array, l, r, mid):
    i = l
    j = mid+1 
    x = l
    # fill aux array
    while (x <= r):
        temp[x] = array[x]
        x += 1
    k = l
    while (k <= r):
        if (i > mid):
            array[k] = temp[j]
            j += 1
        elif (j > r):
            array[k] = temp[i]
            i += 1
        elif (temp[i] < temp[j]):
            array[k] = temp[i]
            i += 1
        elif (temp[i] > temp[j]):
            array[k] = temp[j]
            j += 1
        else:
            array[k] = temp[i]
            i += 1
        k += 1

example_list = [4, 2, 10, 300, 200, 40, 55, 21, 23, 56, 85, 51]
# sorted: 2 4 10 21 23 40 51 55 56 85 200 300
merge_sort(example_list) 
print(example_list)


