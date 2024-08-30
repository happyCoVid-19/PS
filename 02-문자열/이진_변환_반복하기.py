
def solution(s):
    result = s
    zeros = 0
    iter_n = 0
    while int(result) != 1:
        ones = ""
        for binary in result:
            if binary == "0":
                zeros += 1
            else:
                ones += "1"
        iter_n += 1
        n_len = len(ones)
        result = str(bin(int(n_len)))[2:]
    return [iter_n, zeros]