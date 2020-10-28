from rl import rl
from rcb import rcb
from pcb import pcb

class manager:

    # Creates a resource manager
    #   * _pcb = List of PCBs -- index is process number
    #   * _rcb = List of RCBs -- index is resource number
    #   * _rl  = Ready list
    def __init__(self):
        self._pcb = [pcb()] + [None]*15
        self._rcb = [rcb(1),rcb(1),rcb(2),pcb(3)]
        self._rl = rl()

    # Request a resource
    # If it can be allocated, allocate the resource to the process.
    # If it can not be allocated, block the process, remove it from
    #   the ready list, and waitlist it. Call scheduler for the next 
    #   running process.
    def request(self,r,u,p):
        if self._rcb[r].canAllocate(u):
            self._rcb[r].allocate(u)
            self._pcb[p].addResource(r)
            print('Resource', r, 'allocated')
        else:
            self._pcb[p].block()
            self._rl.remove(p)
            self._rcb[r].waitlist(tuple([p,u]))
            self._rl.scheduler()


