import heapq

li = [5,7,8,1,6,10]

heapq.heapify(li)


print(li)
#[1, 5, 8, 7, 6, 10]


heapq.heappush(li,4) 

print(li)
#[1, 5, 4, 7, 6, 10, 8]


(heapq.heappop(li)) 

print(li)
