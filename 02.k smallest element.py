# This code is a Python implementation of an algorithm to find the k smallest number in a given list of numbers 
# (`nums`). 



# NOTE : VERY IMPORTANY : Python always creates the MIN_HEAP by default However, we can create
#  a MAX_HEAP in Python by negating the values before pushing them into the heap, and negating
# the popped values after removing them from the heap

# example : let us understand with an example. consider two numbers i.e. 3 and 7
#                       1:) 3,7 which is minimum element answer is 3 < 7(MIN_HEAP SEQUENCE)
   
#                       2:)But if we give negation to each number number will become
#                         -3 and -7 then same question which number is minimum
#                         ans will be -7 < -3 (MAX_HEAP SEQUENCE) in the same manner python forms the MIN_HEAP
#                         but by providing negation we can get MAX_HEAP.


# SYNTAX FOR PYTHON :

# heappush(max_heap, -curr)  # Negate the value before pushing
.....
.....
.....
.....
# curr = heappop(max_heap)
# curr = -curr               # Negate the root value when returning




# IMPLEMENTATION:

# 1. The `heapq` module is imported, which provides functions to work with heaps (priority queues).

# 2. The `kth_smallest_number` function takes two arguments: `nums` (the list of numbers) and `k` 
#    (the value of `k` for which we want to find the `k`th smallest number).

# 3. An empty list `max_heap` is created, which will be used as a max-heap data structure.

# 4. The function iterates over the list `nums` using a `for` loop.

# 5. For each number `curr` in `nums`, `-curr` is pushed onto the `max_heap` using `heappush(max_heap, -curr)`.
#    This is because the `heapq` module in Python provides a min-heap implementation by default, so we negate
#    the numbers to turn it into a max-heap.

# 6. If the length of `max_heap` becomes greater than `k`, the largest element (which is the root of the max-heap)
#    is removed using `heappop(max_heap)`. This ensures that the max-heap only contains the `k` smallest elements
#    at any given time.

# 7. After the loop, `max_heap` contains the `k` smallest numbers from `nums`.

# 8. An empty list `res` is created to store the `k` smallest numbers in ascending order.

# 9. The function then repeatedly removes the root (largest element) from `max_heap` using `heappop(max_heap)`, 
#    negates it (`-node`), and appends it to `res`. This effectively reverses the negation done earlier and puts
#    the numbers back in their original order.

# 10. Finally, `res` is returned, which contains the `k` smallest numbers from `nums` in ascending order.



from heapq import *

def kth_smallest_number(nums, k):
    max_heap = list()
    for i in range(len(nums)):
        curr = nums[i]
        heappush(max_heap, -curr)
        if len(max_heap) > k:
            heappop(max_heap)
            
    res = list()    
    while max_heap:
        node = heappop(max_heap)
        res.append(-node)
    return res
        


if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    ans = kth_smallest_number(arr, k)
    print(ans)
