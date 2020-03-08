def selection_sort(array):
    for i in range(len(array)):
        minpos = i
        for j in range(i,len(array)):
            if array[j] < array[minpos]:         
                minpos = j
        array[i],array[minpos] = array[minpos], array[i]
    return array





        

