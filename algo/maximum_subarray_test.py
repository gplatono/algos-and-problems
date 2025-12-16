import maximum_subarray

maximum_subarray_tests = [
    {'input': [-2, -1, -3], 'result': -1},
    {'input': [-2, -1, 4, 5, -3], 'result': 9},
    {'input': [3, -2, -1, 4, -3], 'result': 4},
    {'input': [4, -2, -1, 4, -3], 'result': 5},
    {'input': [-3], 'result': -3},
    {'input': [], 'result': 0}
]

def test_func(func, tests):
    print ("Begin testing " + str(func) + "\n==============================================================")
    for test in tests:
        print ("Test #" + str(tests.index(test)+1) + ":")
        print ("Input: " + str(test["input"]))
        try:
            result = func(*test['input'])
        except Exception as ex:
            result = type(ex)
        finally:
            print ("Expected result: " + str(test["result"]) + "; Produced result: " + str(result) + "\n")
    print("End of tests for " + str(func) + "\n==============================================================")

test_func(maximum_subarray.kadanesAlgorithm, maximum_subarray_tests)
test_func(maximum_subarray.minMaxDiffAlgorithm, maximum_subarray_tests)