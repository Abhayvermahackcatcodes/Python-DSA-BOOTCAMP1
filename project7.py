import heapq


li = [5,7,9,1,3]

heapq.heapify(li)

print("the created head is", end="")
print(list(li))

heapq.heappush(li,4)

print ("The Modified heap after push is", end="")
print(list(li))


print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))
