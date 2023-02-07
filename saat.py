
def dif(time1 , time2):
    result = {}
    result['h'] = time2['h'] - time1['h']
    result['m'] = time2['m'] - time1['m']
    result['s'] = time2['s'] - time1['s']
    if result['s'] < 0:
        result['m'] -= 1
        result['s'] += 60
    if result['m'] < 0 :
        result['h'] -= 1
        result['m'] += 60
    if result['h'] >= 24:
        result['h'] -= 24
    return result
def sum(time1 , time2):
    result = {}
    result['h'] = time2['h'] - time1['h']
    result['m'] = time2['m'] - time1['m']
    result['s'] = time2['s'] - time1['s']
    if result['s'] >= 60:
       result['s'] -= 60
       result['m'] +=1
    if result['m'] >= 60:
       result['m'] -= 60 
       result['h'] += 1
    if result['h'] >= 24:
       result['h'] -= 24
    return result

def show(time):
    print(time['h'], ':', time['m'], ':', time['s'])
while True:
    time1_h = int(input("enter h1 : "))
    time1_m = int(input("enter m1: "))
    time1_s = int(input("enter s1 : "))
    time2_h = int(input("enter h2: "))
    time2_m = int(input("enter m2: "))
    time2_s = int(input("enter s2: "))
    time1 = {'h':time1_h, 'm':time1_m, 's':time1_s}
    time2 = {'h':time2_h, 'm':time2_m, 's':time2_s}
    show(time1)
    show(time2)
    
    op = input("+ or - ? :")
    if op == "+":
            sum_result = sum(time1, time2)
            show(sum_result)
    if op == "-":
            dif_result = dif(time1, time2)
            show(dif_result)       
        