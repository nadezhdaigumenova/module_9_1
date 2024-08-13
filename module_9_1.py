def apply_all_func(int_list, *functions):
    result: dict = {}
    for i in functions:
        res = i(int_list)
        result[i.__name__] = res
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
