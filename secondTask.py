import sys

def main_function():
    a = int(sys.stdin.readline())
    if a == 0:
        return 0
    used = [False] * a
    s = sys.stdin.readline()
    s = s.split()
    for i in range(0, a):
        s[i] = int(s[i])
        if s[i] == -1:
            s[i] = i
            v = i

    def init_list_of_objects(size):
        list_of_objects = list()
        for i in range(0,size):
            list_of_objects.append( list() ) #different object reference each time
        return list_of_objects

    graph = init_list_of_objects(a)

    for i in range(0, a):
        graph[s[i]].append(i)


    d = [0] * a

    queue = [v]
    used[v] = True
    while (len(queue) != 0):
        s = queue[0]
        queue = queue[1:]
        for i in graph[s]:
            if (used[i] == False):
                used[i] = True
                queue.append(i)
                d[i] = d[s] + 1

    maximum = 0
    for i in d:
        if i > maximum:
            maximum = i

    return maximum + 1

print(main_function())
