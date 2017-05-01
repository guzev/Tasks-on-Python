def answer(N):
    def init_list_of_objects(size):
        list_of_objects = list()
        for i in range(0,size):
            list_of_objects.append( list() )
        return list_of_objects

    main_array = init_list_of_objects(18)
    squares = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]

    counter_of_one = [0, 1, 1, 2]


    ref_to_counter_of_one = 1
    ref_to_squares = 2
    k = 1
    for i in range(2, 18):
        if (N >= squares[i]):
            k = k + 1
        else:
            break
    result = []
    if (N <= 3):
        for i in range(0, N):
            result.append(i)
        return result
    else:
        result = [0]
        main_array[1].append(1)
        main_array[1].append(2)
        main_array[2].append(3)
        for i in range(4, N):
            if (i == squares[ref_to_squares]):
                ref_to_counter_of_one = 1
                counter_of_one.append(1)
                main_array[1].append(i)
                ref_to_squares = ref_to_squares + 1
            else:
                counter_of_one.append(1 + counter_of_one[ref_to_counter_of_one])
                main_array[1 + counter_of_one[ref_to_counter_of_one]].append(i)
                ref_to_counter_of_one = ref_to_counter_of_one + 1


    for i in range(1, k + 1):
        for j in main_array[i]:
            result.append(j)

    return result


dataset = input()
N = int(dataset.strip())
print((answer(N)))
