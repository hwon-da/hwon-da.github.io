def two_times(numberlist):
    result = [ ]
    for number in numberlist:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)


def two_time(x):
    return x*2

list(map(two_time, [1, 2, 3, 4]))

a, b = map(int, input().strip.split(' '))
print(a + b)