def mod(a, b):  # 1.19
    if a < b:
        return a
    return a - int(a / b) * b


def gcd_mr(num1, num2):  # 1.20
    if num1 < num2:
        return gcd_mr(num2, num1)
    elif num2 == 0:
        return num1
    else:
        return gcd_mr(num1 - num2, num2)


def gcd_m(num1, num2):  # 1.21????????what????????
    if num1 > num2:
        num = int(num2 / 2)
    else:
        num = int(num1 / 2)
    while num1 % num != 0 or num2 % num != 0:
        num -= 1
    return num


def gcd_er(num1, num2):  # 1.22
    if num2 == 0:
        return num1
    else:
        return gcd_er(num2, mod(num1, num2))


def gcd_e(num1, num2):  # 1.23
    while num2 != 0:
        num1, num2 = num2, mod(num1, num2)
    return num1


def gcd_c(num1, num2):  # 1.24
    if num2 == 0:
        return num1
    num = 0
    while num1 % 2 == 0 and num2 % 2 == 0:
        num1 /= 2
        num2 /= 2
        num += 1
    while num1 % 2 == 0:
        num1 /= 2
    while num2 % 2 == 0:
        num2 /= 2
    numt = 1
    while numt != 0:
        numt = (num1 - num2) / 2
        while numt % 2 == 0 and numt != 0:
            numt /= 2
        if numt > 0:
            num1 = numt
        else:
            num2 = -numt
    return (2 ** num) * num1


def is_compire_pairs(pairs_list):   # 1.25
    for i in range(1, len(pairs_list) - 1):
        for j in range(i + 1, len(pairs_list)):
            if gcd_er(pairs_list[i], pairs_list[j]) != 1:
                return False
    return True


if __name__ == '__main__':
    print(gcd_e(40, 24))
    print(gcd_er(40, 24))
    print(gcd_mr(40, 24))
    print(gcd_m(40, 24))
    print(gcd_c(40, 24))
    listok = [1, 3, 6, 7]
    print(is_compire_pairs(listok))
