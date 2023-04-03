from collections import deque
queue = deque([])
queue.append(1)
queue.append(3)
queue.append(4)
queue.append(9)

print(queue)
print(queue.popleft())
if not queue:
    print("Empty Queue")
