def test(*arg):
    arr = list(arg)
    # first = arr[0]
    # second = arr[1]
    if (sorted(arr[0]) == sorted(arr[1])):
        print('t')
        return True
    else:
        return False


test('listen', 'silent')
# Exemplu: task_12(2, 3, 5, 7) ➞ True
