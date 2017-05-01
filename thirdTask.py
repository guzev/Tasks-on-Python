import sys

def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0, size):
        list_of_objects.append(list())
    return list_of_objects


n = int(input())
a = input().split(" ")
root_one = 0
root_two = 0
for i in range(0, n):
    a[i] = int(a[i])
    if (a[i] == -1):
        root_one = i

b = input().split(" ")
for i in range(0, n):
    b[i] = int(b[i])
    if (b[i] == -1):
        root_two = i

if (n <= 2):
    print("YES")
    sys.exit()

list_of_first_tree = init_list_of_objects(n)
list_of_second_tree = init_list_of_objects(n)

hashes1 = [-1] * n
hashes2 = [-1] * n
counter = 1

for i in range(0, n):
    if (a[i] != -1):
        list_of_first_tree[a[i]].append(i)

for i in range(0, n):
    if (b[i] != -1):
        list_of_second_tree[b[i]].append(i)

dictinary = {(): 0}


def count_hash1(number_of_vertice):
    global counter
    global hashes1
    global list_of_first_tree
    tmp = len(list_of_first_tree[number_of_vertice])
    if (tmp == 2):
        if (hashes1[list_of_first_tree[number_of_vertice][0]] == -1):
            count_hash1(list_of_first_tree[number_of_vertice][0])
        a = hashes1[list_of_first_tree[number_of_vertice][0]]
        if (hashes1[list_of_first_tree[number_of_vertice][1]] == -1):
            count_hash1(list_of_first_tree[number_of_vertice][1])
        b = hashes1[list_of_first_tree[number_of_vertice][1]]
        s = []
        s.append(a)
        s.append(b)
        if (dictinary.get(tuple(sorted(s))) != None):
            hashes1[number_of_vertice] = dictinary.get(tuple(sorted(s)))
        else:
            dictinary[tuple(sorted(s))] = counter
            hashes1[number_of_vertice] = counter
            counter = counter + 1
    elif (tmp == 1):
        if (hashes1[list_of_first_tree[number_of_vertice][0]] == -1):
            count_hash1(list_of_first_tree[number_of_vertice][0])
        a = hashes1[list_of_first_tree[number_of_vertice][0]]
        s = []
        s.append(a)
        if (dictinary.get(tuple(sorted(s))) != None):
            hashes1[number_of_vertice] = dictinary.get(tuple(sorted(s)))
        else:
            dictinary[tuple(sorted(s))] = counter
            hashes1[number_of_vertice] = counter
            counter = counter + 1
    else:
        hashes1[number_of_vertice] = 0


counter = 1


def count_hash2(number_of_vertice):
    global counter
    global hashes2
    global list_of_second_tree
    tmp = len(list_of_second_tree[number_of_vertice])
    if (tmp == 2):
        if (hashes2[list_of_second_tree[number_of_vertice][0]] == -1):
            count_hash2(list_of_second_tree[number_of_vertice][0])
        a = hashes2[list_of_second_tree[number_of_vertice][0]]
        if (hashes2[list_of_second_tree[number_of_vertice][1]] == -1):
            count_hash2(list_of_second_tree[number_of_vertice][1])
        b = hashes2[list_of_second_tree[number_of_vertice][1]]
        s = []
        s.append(a)
        s.append(b)
        if (dictinary.get(tuple(sorted(s))) != None):
            hashes2[number_of_vertice] = dictinary.get(tuple(sorted(s)))
        else:
            dictinary[tuple(sorted(s))] = counter
            hashes2[number_of_vertice] = counter
            counter = counter + 1
    elif (tmp == 1):
        if (hashes2[list_of_second_tree[number_of_vertice][0]] == -1):
            count_hash2(list_of_second_tree[number_of_vertice][0])
        a = hashes2[list_of_second_tree[number_of_vertice][0]]
        s = []
        s.append(a)
        if (dictinary.get(tuple(sorted(s))) != None):
            hashes2[number_of_vertice] = dictinary.get(tuple(sorted(s)))
        else:
            dictinary[tuple(sorted(s))] = counter
            hashes2[number_of_vertice] = counter
            counter = counter + 1
    else:
        hashes2[number_of_vertice] = 0


count_hash1(root_one)
count_hash2(root_two)

if (hashes1[root_one] == hashes2[root_two]):
    print("YES")
else:
    print("NO")
