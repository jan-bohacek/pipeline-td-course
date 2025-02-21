my_array = [1, 5, 7, 8, 10, 12, 15, 17, 21, 25, 31, 32, 33, 39, 41, 44, 46, 49, 50, 52, 55, 60]

def binary_search(array, value):
    lo = 0
    hi = len(array)

    iters = 0
    while lo < hi:
        iters += 1
        mid = lo + (hi - lo) // 2
        cur = array[mid]

        if cur == value:
            return mid, iters
        elif cur > value:
            hi = mid
        else:
            lo = mid + 1
                
    
    return False


search = binary_search(my_array, int(input("Input Number : ")))
if search:
    print(f"Number is at the index {search[0]}, it took {search[1]} iterations to find it.")
else:
    print("Number is not in the array.")