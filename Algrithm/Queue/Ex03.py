import sys
from queue import Queue

n=int(input())     # push 1
q=Queue()

for i in range(n):
    line=sys.stdin.readline()
    cmd=line.rstrip().split()
    # print(cmd[0], cmd[1])

    if cmd[0] == 'push':
        q.put(int(cmd[1]))

    elif cmd[0] == "pop":
        if q.qsize() == 0:
            print(-1)
        else:
            print(q.get())

    elif cmd[0] == "size":
        print(q.qsize())

    elif cmd[0] == "empty":
        if q.empty():
            print(1)
        else:
            print(0)

    elif cmd[0] ==  "front":
        if q.qsize()==0:
            print(-1)
        else:
            print(q.queue[0])
            
    elif cmd[0] == "back":
        if q.qsize()==0:
            print(-1)
        else:
            print(q.queue[-1])


    