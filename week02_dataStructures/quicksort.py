my_array = [1, 9, 3, 6, 8, 2, 5, 4, 7]

def dfs(array, lo, hi):
    if lo > hi:
        return
    pivot = partition(array, lo, hi)
    print(f"--- next iteration ---")
    print(f"--- Array size : {hi - lo} ---")
    print(f"--- Iter array : {my_array} ---")
    print(f"--- Pivot idx : {pivot} | Pivot value : {array[pivot]} ---")
    dfs(array, lo, pivot-1)
    dfs(array, pivot+1, hi)

def partition(array, lo, hi):
    pivot = array[hi]
    idx = lo - 1
    i = lo

    while i < hi:
        if array[i] <= pivot:
            idx += 1
            tmp = array[i]
            array[i] = array[idx]
            array[idx] = tmp
        i += 1
    idx += 1
    array[hi] = array[idx]
    array[idx] = pivot
    return idx

def quicksort(array):
    dfs(array, 0, len(array)-1)



print(f"Original array : {my_array}")
quicksort(my_array)
print(f"Result array : {my_array}")