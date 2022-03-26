
sort_tests = [
    {'input': ([1, 2, 5, 0, 5, 1, 10, 1],), 'result': [0, 1, 1, 1, 2, 5 ,5, 10]},
    {'input': ([1],), 'result': [1]},
    {'input': ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1],), 'result': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]},
    {'input': ([2, 4, 0, 1, 0, 3, 2, 9, 10012, 1],), 'result': [0, 0, 1, 1, 2, 2, 3, 4, 9, 10012]},
    {'input': ([-1, 1, -1, 1, 0, 5, 6, -1, 121, -10],), 'result': [-10, -1, -1, -1, 0, 1, 1, 5, 6, 121]}
    ]

def bubble_sort(arr, key=lambda x, y: x < y):
    for i in range(len(arr)-1, -1, -1):
        for j in range(1, i+1):
            if key(arr[j], arr[j-1]):
                tmp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = tmp
    return arr

def direct_choice_sort(arr, key=lambda x, y: x < y):
    for i in range(len(arr)-1, -1, -1):
        max_val = arr[0]
        max_ind = 0
        for j in range(i+1):
            if key(max_val, arr[j]):
                max_val = arr[j]
                max_ind = j
        arr[max_ind] = arr[i]
        arr[i] = max_val
    return arr

def insertion_sort(arr, key=lambda x, y: x < y):
    for i in range(1, len(arr)):
        idx = i
        val = arr[i]
        while idx > 0 and key(val, arr[idx-1]):
            arr[idx] = arr[idx-1]
            idx -= 1
        arr[idx] = val
    return arr

def test_func(func, tests):
    for test in tests:
        result = func(*test['input'])
        print ("Test number " + str(tests.index(test)+1) + ":")
        print ("Input: " + str(test["input"]))
        print ("Expected result: " + str(test["result"]) + "; Produced result: " + str(result))
        print ("Result: " + ("PASS!" if result == test["result"] else "FAIL!") + "\n")

#test_func(bubble_sort, sort_tests)
#test_func(direct_choice_sort, sort_tests)
#test_func(insertion_sort, sort_tests)