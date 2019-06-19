def solution(d,budget):
    d.sort()                    # 내림차순해서
    while budget < sum(d):      # d(list)의 합이 budget을 초과하는경우
        d.pop()                 # 맨 마지막을 지우고 돌려줌
    return len(d)               # 남은 d(부서)의 수 리턴