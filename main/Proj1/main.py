from manager import manager
from rl import rl
from rcb import rcb
from pcb import pcb
import sys

if (__name__ == "__main__"):
    f1 = open(sys.argv[1], 'r+')
    f2 = open('output.txt', 'w+')
    justStarted = True

    for i in f1.readlines():
        l = i.split()
        try:
            if len(l) == 0:
                pass

            elif (l[0] == 'in'):
                m = manager()
                if not justStarted:
                    f2.write('\n')
                f2.write(m.init())
                justStarted = False

            elif (l[0] == 'cr'):
                p = int(l[1])
                if p == 1 or p == 2:
                    f2.write(m.create(p))
                else:
                    f2.write('-1')

            elif (l[0] == 'de'):
                i = int(l[1])
                f2.write(m.destroy(i))

            elif (l[0] == 'rq'):
                r = int(l[1])
                n = int(l[2])
                f2.write(m.request(r,n))

            elif (l[0] == 'rl'):
                r = int(l[1])
                n = int(l[2])
                f2.write(m.release(r,n))

            elif (l[0] == 'to'):
                f2.write(m.timeout())

        except ValueError:
            f2.write('-1')

        f2.write(' ')

    f1.close()
    f2.close()