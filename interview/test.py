def  characterReverse( input):
    n = len(input)
    output = ''
    count_t = 0
    count_h = 0
    for i in range(n):
        a = input[i]
        if i == n-1:
            b = None
        else:
            b = input[i+1]
        if a == 't' and b == 't':
            count_t += 1
        if a == 't' and b == 'h':
            count_t += 1
        if a == 'h' and b == 'h':
            count_h += 1
        if a == 'h' and b == 't':
            count_h += 1
        if a == 't' and b != 't' and b != 'h':
            count_t += 1
        if a == 'h' and b != 't' and b != 'h':
            count_h += 1
        if a != 't' and a != 'h':
            output += 'h'*count_h + 't'*count_t + a
            count_h = 0
            count_t = 0
    return output

print characterReverse('theatre')
