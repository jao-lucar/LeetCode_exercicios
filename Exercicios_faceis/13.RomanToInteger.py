def romano(num=''):
    num = num.upper()
    arabico = 0
    numeros1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000, }

    numeros2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                'CD': 400, 'CM': 900}

    for k, v in numeros2.items():

        if k in num:
            arabico += v
            num = num.replace(k, '')

    for k, v in enumerate(num):
        if num[k] in numeros1:
            arabico += numeros1[num[k]]

    return arabico

while True:
    n = str(input("Digite o número romano: "))
    print(romano(n))

