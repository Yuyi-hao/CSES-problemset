from collections import deque
if __name__=="__main__":
    n = int(input())
    queue = deque(range(1, n+1))
    flag = False
    while queue:
        curr = queue.popleft()
        if flag:
            print(curr, end=" ")
        else:
            queue.append(curr)
        flag = not flag
    exit(0)