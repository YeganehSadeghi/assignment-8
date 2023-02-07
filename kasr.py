def div(x , y):
    result = {}
    result['s'] = x['s'] * y['m']
    result['m'] = x['m'] * y['s']
    return result

def mul(x, y):
    result = {}
    result['s'] = x['s'] * y['s']
    result['m'] = x['m'] * y['m']
    return result

def sum(x, y):
    result = {}
    result['s'] = (x['s']*y['m']) + (x['m']*y['s'])
    result['m'] = x['m']*y['m']
    return result

def dif(x , y):
    result = {}
    result['s'] = (x['s']*y['m']) - (x['m']*y['s'])
    result['m'] = x['m']*y['m']
    return result


def show(f):
    print(f['s'], '/', f['m'])
    op = input("enter * or + or - or / :")
    if op == "*":
            mul_result = mul(a , b)
            show(mul_result)

    if op == "+":
            sum_result = sum(a , b)
            show(sum_result)

    if op == "-":
            dif_result = dif(a , b)
            show(dif_result)

    if op == "/":
            div_result = div(a, b)
            show(div_result)
while True:
    f1_s = int(input("enter Sorat kasr1: "))
    f1_m = int(input("enter Makhrag kasr1 : "))
    f2_s = int(input("enter Sorat kasr2 : "))
    f2_m = int(input("enter Makhrag kasr2 : "))

    a = {'s':f1_s, 'm':f1_m}
    b = {'s':f2_s, 'm':f2_m}
    show(a)
    show(b)
    
