def solution(x,n):
    answer = []
    for i in range(n):
        answer.append(x + x * i)
    return answer

print(solution(2,5))


# return [i * x + x for i in range(n)]
# return list(range(x, x*n+1, x))   : 음수의 경우 에러

a = '     hi    '
print(a.rstrip)