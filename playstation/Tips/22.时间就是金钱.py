'''
描述:
给你两个时间st和et(00:00:00<=st <= et<=23:59:59), 请你给出这两个时间间隔的秒数。
如：st="00:00:00", et="00:00:10", 则输出10.
'''
def shi_jian_qian(st,et):
    a = st.split(':')
    b = et.split(':')
    if b[0] != '00':
        x1 = int(b[0])*3600
    else:
        x1 = 0
    if b[1] != '00':
        x2 = int(b[1])*60
    else:
        x2 = 0
    x3 = int(b[2])
    y1 = x1+x2+x3
    if a[0] != '00':
        z1 = int(a[0])*3600
    else:
        z1 = 0
    if a[1] != '00':
        z2 = int(a[1])*60
    else:
        z2 = 0
    z3 = int(a[2])
    y2 = z1+z2+z3
    print(y1-y2)

st = input('st:')
et = input('et:')
shi_jian_qian(st,et)