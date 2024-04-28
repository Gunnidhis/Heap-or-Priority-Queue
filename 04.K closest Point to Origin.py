# question: Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and
#           an integer k, return the k closest points to the origin (0, 0).

#           The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

#           You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Here's a breakdown of what's happening:

# 1. The function creates an empty max-heap `max_heap` using the `heapq` module from Python's standard library.

# 2. It iterates over the input list of points `points`.

# 3. For each point `[x, y]`, it calculates the square of the Euclidean distance from the origin (0, 0) using
#    the formula `x^2 + y^2`. This squared distance value is stored in the variable `dist`.

# 4. The function pushes a tuple `(-dist, x, y)` onto the `max_heap`. The negative sign is used because `heapq`
#    in Python creates a min-heap by default, and using `-dist` allows us to create a max-heap based on the squared
#    distances.

# 5. After processing all points, the `max_heap` will contain the `k` points with the smallest squared distances
#    from the origin at the top (because it's a max-heap).

# 6. If the size of the `max_heap` exceeds `k`, it removes the point with the largest squared distance (i.e., the 
#    root of the max-heap) using `heappop`.

# 7. After processing all points, the `max_heap` contains the `k` closest points to the origin.

# 8. The code creates an empty list `ans` and pops elements from the `max_heap` one by one, appending a list 
#    containing the `x` and `y` coordinates (the second and third elements of each tuple) to the `ans` list.

# 9. Finally, the `ans` list containing the `k` closest points to the origin is returned.


# In the example usage at the bottom, the code creates a list `points` with three points `[[3, 3], [5, -1], [-2, 4]]`,
# and sets the number of closest points `k` to `2`. It calls the `k_closest_points` function with these inputs and prints
# the resulting list `res`, which should contain the two points closest to the origin from the input list `points`.

# This implementation uses the `heapq` module to efficiently find the `k` closest points to the origin by maintaining a 
# max-heap of size `k` with the smallest squared distances at the top.


from heapq import *
def k_closest_points(points,k):
    max_heap = list()
    for i in range(len(points)):
        point = points[i]
        x = point[0]
        y = point[1]
        
        dist = (x * x + y * y)
        heappush(max_heap,[-dist,x,y])
        
        if len(max_heap) > k:
            heappop(max_heap)
            
    ans = list()
    while max_heap:
        distance,x_coordinate,y_coordinate = heappop(max_heap)
        ans.append([x_coordinate,y_coordinate])
    return ans

if __name__ == "__main__":
    points =[[3,3],[5,-1],[-2,4]]
    k = 2
    res = k_closest_points(points,k)
    print(res)

#output : [[-2, 4], [3, 3]]
