from itertools import *
def logic_table(expression):
    table = []
    cnt0 = 0
    cnt1 = 1
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):

                    iev = int(eval(expression))

                    table.append([w, x, y, z, iev])

                    if iev == 0:
                        cnt0 += 1
                    else:
                        cnt1 += 1
    res = []
    if cnt0 <= cnt1:
        for i in table:

            if i[-1] == 0:
                res.append(i)
    else:
        for i in table:
            if i[-1] == 1:
                res.append(i)
    return res

