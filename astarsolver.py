# An Implementation of the A* algorithm for pathfinding
import math

n = int(input())
digits = int(math.pow(10, len(str(n))))

l = {}

for i in range(1, n + 1):
    s = input()
    for j in range(1, len(s.split(" ")) + 1):
        l[i * digits + j] = int(s.split(" ")[j - 1])


def print_board(l: dict):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(l[i * 10 + j], end=" ")
        print()
    print()


def astarsolve(start, end):
    heuristic = lambda a, b: abs(a // digits - b // digits) + abs(
        a % digits - b % digits
    )

    for k, v in l.items():
        if k == start:
            if (
                k + 10 in l
                and (l[k + 10] == 0 or l[k + 10] == 2)
                and heuristic(k, end) > heuristic(k + 10, end)
            ):
                l[k] = 2
                start = k + 10
                
                astarsolve(start, end)

            elif (
                k - 10 in l
                and (l[k - 10] == 0 or l[k - 10] == 2)
                and heuristic(k, end) > heuristic(k - 10, end)
            ):
                l[k] = 2
                start = k - 10
                
                astarsolve(start, end)

            elif (
                k + 1 in l
                and (l[k + 1] == 0 or l[k + 1] == 2)
                and heuristic(k, end) > heuristic(k + 1, end)
            ):
                l[k] = 2
                start = k + 1
                
                astarsolve(start, end)

            elif (
                k - 1 in l
                and (l[k - 1] == 0 or l[k - 1] == 2)
                and heuristic(k, end) > heuristic(k - 1, end)
            ):
                l[k] = 2
                start = k - 1
                
                astarsolve(start, end)

        if start == end:
            
            l[start] = 2
            return


print(l)
goals_done = []
for k, v in l.items():
    if v == n - 1:
        if k + 10 in l and l[k + 10] == 0:
            cur = k + 10
            goals_done.append(k)
            break
        elif k - 10 in l and l[k - 10] == 0:
            cur = k - 10
            goals_done.append(k)
            break
        elif k + 1 in l and l[k + 1] == 0:
            cur = k + 1
            goals_done.append(k)
            break
        elif k - 1 in l and l[k - 1] == 0:
            cur = k - 1
            goals_done.append(k)
            break
print(goals_done)
while len(goals_done) < list(l.values()).count(n - 1):
    target = 0
    for k, v in l.items():

        if int(v) == n - 1 and k not in goals_done:
            if k + 10 in l and l[k + 10] == 0:
                target = k + 10

            elif k - 10 in l and l[k - 10] == 0:
                target = k - 10

            elif k + 1 in l and l[k + 1] == 0:
                target = k + 1

            elif k - 1 in l and l[k - 1] == 0:
                target = k - 1

            print(target)
            astarsolve(cur, target)
            print(l)
            goals_done.append(target)
            print(goals_done)
            cur = target
target = goals_done[-1]
cur = goals_done[0]
astarsolve(cur, target)


print_board(l)
