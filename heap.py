# a heap is created by using python inbuilt library named "heapq
# heapify= convert regular list to a heap.smallest element push in the index position 0
# heappush,heappop,heapreplace. various operation.
import heapq

H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)
# inserting
heapq.heappush(H,9)
print(H)
# removing
heapq.heappop(H)

print(H)