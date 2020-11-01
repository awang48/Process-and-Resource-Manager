
from manager import manager
from rl import rl
from rcb import rcb
from pcb import pcb
import sys

if (__name__ == "__main__"):
    while (True):
        i = input()
        l = i.split()
        try:
            if len(l) == 0:
                pass

            if (l[0] == 'e'):
                break

            elif (l[0] == 'in'):
                m = manager()

            elif (l[0] == 'cr'):
                p = int(l[1])
                if p == 1 or p == 2:
                    m.create(p)

            elif (l[0] == 'de'):
                i = int(l[1])
                m.destroy(i)

            elif (l[0] == 'rq'):
                r = int(l[1])
                n = int(l[2])
                m.request(r,n)

            elif (l[0] == 'rl'):
                r = int(l[1])
                n = int(l[2])
                m.release(r,n)

            elif (l[0] == 'to'):
                m.timeout()

        except ValueError:
            pass

        print(m)