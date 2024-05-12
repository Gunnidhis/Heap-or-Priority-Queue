# Author
# Gunnidhi Sharma


# question : Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.
# example : Input: s = "aabbcc", k = 3
#           Output: "abcabc"
#           Explanation: The same letters are at least distance 3 from each other.


from collections import deque, defaultdict
from heapq import *

def reorganiseString(s, distance):
    n = len(s)
    queue = deque()
    max_heap = list()
    d = defaultdict()
    for char in s:
        if char not in d:
            d[char] = 0
        d[char] += 1
    for key, value in d.items():
        heappush(max_heap, [-value, key])

    res = ""
    while max_heap:
        v, k = heappop(max_heap)
        v *= -1
        res += k
        queue.append([k, v - 1])
        if len(queue) == distance:
            char, freq = queue.popleft()
            if freq > 0:
                heappush(max_heap, [-freq, char])

    if len(res) == len(s):
        return res
    return ""


if __name__ == "__main__":
    s = "aabbcc"
    k = 3
    ans = reorganiseString(s, k)
    print(ans)

#output :abcabc
    
