#input: crumble array 

#ouput: sort array

#algorithm : Insertion Sort 

#complexity : O(n2)
"""
the first element is considered as sorted

Ok now, you get the second element

la idea es tomar un numero y  compararlo con el anterior hasta encontrarle un lugar
"""



def insertion_sort(a):
    for step in range(1,len(a)):
        key = a[step]
        beforeKey = step -1
        while  beforeKey >= 0 and a[beforeKey] > key:
            a[beforeKey + 1] = a[beforeKey]
            beforeKey -= 1
        a[beforeKey+1]  = key
    return a


