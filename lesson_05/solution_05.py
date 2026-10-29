# первая функция
def step_score(steps, k, lower, upper):
    current_sum = sum(steps[:k])
    score = 0
    if current_sum < lower:
        score -= 1
    elif current_sum > upper:
        score += 1
    for i in range(k, len(steps)):
        current_sum += steps[i] - steps[i - k]
        if current_sum < lower:
            score -= 1
        elif current_sum > upper:
            score += 1
    return score

# вторая функция
def decrypt(code, k):
    n = len(code)
    result = [0] * n
    if k == 0:
        return result
    if k > 0:
        left = 1
        right = k
    else:
        left = n + k
        right = n - 1
    current_sum = 0
    for i in range(left, right + 1):
        current_sum += code[i % n]
    result[0] = current_sum
    for i in range(1, n):
        current_sum -= code[(left + i - 1) % n]
        current_sum += code[(right + i) % n]
        result[i] = current_sum
    return result
