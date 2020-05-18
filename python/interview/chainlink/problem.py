def solution(prices):
    if len(prices) == 0:
        return 0
    # We are always paying the first price.
    total = prices[0]
    min_price = prices[0]
    for i in range(1, len(prices)):
        if prices[i] > min_price:
            total += prices[i] - min_price
        if prices[i] < min_price:
            min_price = prices[i]
    return total

def num_divisors(number, keys):
    count = 0
    for key in keys:
        if number % key == 0:
            count += 1
    return count

def encryptionValidity(instructionCount, validityPeriod, keys):
    max_num_divisors = float('-inf')
    for key in keys:
        num = num_divisors(key, keys)
        if num > max_num_divisors:
            max_num_divisors = num
    encryption_strength = max_num_divisors * pow(10, 5)
    is_crackable = 1
    if encryption_strength / instructionCount > validityPeriod:
        is_crackable = 0
    return is_crackable, encryption_strength
