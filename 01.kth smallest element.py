# This code is an implementation of finding the kth smallest element in an unsorted list
# of numbers using a heap data structure.

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




# 1. The `kth_smallest_number` function takes two arguments: `nums` (the list of numbers)
#    and `k` (the value of k for finding the kth smallest element).

# 2. An empty list `max_heap` is created to store the max heap.

# 3. A loop iterates through each number `curr` in the `nums` list.

# 4. For each `curr`, `-curr` (negated value) is pushed into the `max_heap` using 
#   `heappush(max_heap, -curr)`. This is because the `heapq` module in Python implements
#    a min heap by default, and negating the values allows us to treat it as a max heap.

# 5. After pushing an element, if the length of `max_heap` exceeds `k`, the largest element
#    (the root of the max heap) is removed using `heappop(max_heap)`. This ensures that the 
#    max heap contains only the `k` smallest elements.

# 6. After the loop, the max heap contains the `k` smallest elements, with the smallest element
#    at the root (index 0).

# 7. The function returns `-max_heap[0]`, which is the negated value of the root (the kth smallest element).

# 8. In the `__main__` block, an example list `arr` and the value of `k` are provided.

# 9. The `kth_smallest_number` function is called with `arr` and `k`, and the result is stored in `ans`.

# 10. Finally, the value of `ans` (the kth smallest element) is printed.


from heapq import *

def kth_smallest_number(nums, k):
    max_heap = list()
    for i in range(len(nums)):
        curr = nums[i]
        heappush(max_heap, -curr)
        if len(max_heap) > k:
            heappop(max_heap)
    return -max_heap[0]


if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    ans = kth_smallest_number(arr, k)
    print(ans)
