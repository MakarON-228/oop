from itertools import *

def solve_first_task(s, z, table_length):
    # s = 'ADEF BDF CFG DABE EADG FABC GCE'
    #d = {c:set(v) for c,*v in s.split()}

    # z = '123 2145 316 427 5267 6357 7456'
    for x in permutations(set(s)-{' '}):
      t = z
      for a,b in zip(''.join(str(i + 1) for i in range(table_length)), x):
        t = t.replace(a,b)


      #g = {c:set(v) for c,*v in t.split()}
      g = ' '.join(c+''.join(sorted(v)) for c,*v in sorted(t.split()))
      if g==s:
        return x

# print(solve_first_task('АБ БАВГД ВБД ГБДК ДБВГЕК ЕДК КГДЕ', '147 246 36 412567 5467 62345 7145', 7))