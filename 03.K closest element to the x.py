# Question : Given an array arr[] and a value X, find the k closest elements to X in arr[]. 

# Here's a breakdown of what's happening:

# 1. The function creates an empty max-heap `max_heap` using the `heapq` module from Python's standard library.

# 2. It iterates over the input list `nums` and calculates the absolute difference between each element and the
#    target value `x`.

# 3. For each element, it pushes a tuple `(-diff, nums[i])` onto the `max_heap`. The negative sign is used because
#    `heapq` in Python creates a min-heap by default, and using `-diff` allows us to create a max-heap based on the
#    absolute differences.

# 4. After processing all elements, the `max_heap` will contain the `k` elements with the smallest absolute differences
#    from `x` at the top (because it's a max-heap).

# 5. If the size of the `max_heap` exceeds `k`, it removes the element with the largest absolute difference (i.e., the root
#    of the max-heap) using `heappop`.

# 6. After processing all elements, the `max_heap` contains the `k` closest elements to `x`.

# 7. The code creates an empty list `result` and pops elements from the `max_heap` one by one, appending the second 
#    element of each tuple (the actual value from `nums`) to the `result` list.

# 8. Finally, the `result` list containing the `k` closest elements to `x` is returned.

# here is implementation of above approach in Python language.


from heapq import *

def closest_element(nums, k, x):
    max_heap = list()
    for i in range(len(nums)):
        if nums[i] == x:
            continue
        diff = abs(nums[i] - x)
        heappush(max_heap, [-diff, nums[i]])
        
        if len(max_heap) > k:
            heappop(max_heap)
                        
          
    result = list()
    while max_heap:
        abs_diff, element = heappop(max_heap)
        result.append(element)
    return result


if __name__ == "__main__":
    nums = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
    x = 35
    k = 4
    ans = closest_element(nums, k, x)
    print(ans)

#output : [45, 42, 30, 39]
