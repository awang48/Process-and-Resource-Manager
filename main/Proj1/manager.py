from rl import rl
from rcb import rcb
from pcb import pcb

class manager:
    """A manager that manages processes and resources.
    
    Attributes:
        _pcb (:obj:`list` of :obj:`pcb`): List of pcb objects, each one representing a slot for processes.
        _rcb (:obj:'list' of :obj:'rcb'): List of rcb objects, each one representing a resource.
        _rl (:obj:'rl'): Three-level rl (Ready list) for processes.
        
    """

    def __init__(self):
        self._pcb = [pcb(None, 0)] + [None]*15
        self._rcb = [rcb(1),rcb(1),rcb(2),rcb(3)]
        self._rl = rl()
        self._rl.add(0, 0)
        self._rl.scheduler()
        self._pcb[self._rl.getRun()].run()

    def init(self):
        """Placeholder function for assignment's naming conventions.
   
        Returns:
            str: Currently running process.
        
        """
        return str(self._rl.getRun())
        
    def request(self,r: int,u: int) -> str:
        """Requests a certain number of units of a certain resource.
        
        Args:
            r (int): Resource number.
            u (int): Unit count.
            
        Returns:
            str: Currently running process.

        Raises:
            ValueError: If the process already has the resource, the resource does not exist, or
                The requested units exceeds the maximum capacity of units for the given resource.
        
        """
        p = self._rl.getRun()
        if self._rl.getRun() == 0 or u <= 0:
            return -1
        if self._pcb[self._rl.getRun()].hasResource(r):
            raise ValueError("Resource already requested")
        if r < 0 or r > 3:
            raise ValueError("Resource does not exist")
        if u > self._rcb[r].getCapacity():
            raise ValueError("Requested units greater than capacity")
        if self._rcb[r].getUnit() >= u:
            self._rcb[r].allocate(u)
            self._pcb[p].addResource(r,u)
            return str(self._rl.getRun())
        else:
            self._pcb[p].block()
            self._rl.remove(p)
            self._rcb[r].addWaitlist(p,u)
            self._rl.scheduler()
            self._pcb[self._rl.getRun()].run()
            return str(self._rl.getRun())

    def release(self,r: int,u: int, p:int = None) -> str:
        """Releases a certain number of units of a certain resource. Processes that have been
            re-'ready'ed are added back on to the ready list. Running process is updated.
        
        Args:
            r (int): Resource number.
            u (int): Unit count.
            p (int): Process number.
            
        Returns:
            str: Currently running process.

        Raises:
            ValueError: If the resource does not exist or if the process has not requested
                the resource before.
        
        """
        if p == None:
            p = self._rl.getRun()
        if u <= 0:
            return
        if r < 0 or r > 3:
            raise ValueError("Resource does not exist")
        if not self._pcb[p].hasResource(r):
            raise ValueError("Process has not requested resource before")
        numReleased = self._pcb[p].remResource(r,u)
        self._rcb[r].release(numReleased)
        next = self._rcb[r].waitlistNext().copy()
        self._pcb[self._rl.getRun()].ready()
        for i in next:
            self._pcb[i[0]].ready()
            self._rcb[r].allocate(i[1])
            self._pcb[i[0]].addResource(r,i[1])
            self._rl.add(i[0], self._pcb[i[0]].getPriority())
        self._rl.scheduler()
        self._pcb[self._rl.getRun()].run()
        return str(self._rl.getRun())

    def create(self, p: int) -> str:
        """Creates a process at the given priority level. The currently running process is the parent.
        
        Args:
            p (int): Priority level.
            
        Returns:
            str: Currently running process.

        Raises:
            ValueError: If there are no more slots open for processes.
        
        """
        firstFree = -1
        for i in range(len(self._pcb)):
            if self._pcb[i] == None:
                firstFree = i
                break
        if firstFree == -1:
            raise ValueError("No more slots open for processes.")
        self._pcb[firstFree] = pcb(self._rl.getRun(), p)
        self._pcb[self._rl.getRun()].ready()
        self._pcb[self._rl.getRun()].addChild(firstFree)
        self._rl.add(firstFree, p)
        self._rl.scheduler()
        self._pcb[self._rl.getRun()].run()
        return str(self._rl.getRun())

    def destroy(self, p: int) -> str:
        """Destroys a certain process and all its children. Releases all resources held by those processes.
            Processes are removed from all resource waitlists.
        
        Args:
            p (int): Process number. Must be either the currently running process or an immediate child of it.
            
        Returns:
            str: Currently running process. -1 if an attempt to delete process 0 is made.

        Raises:
            ValueError: If the process is not a child of the current process.
        
        """
        def recurDel(p: int) -> None:
            """Requests a certain number of units of a certain resource.
        
            Args:
                p (int): Process number.
            
            Returns:
                None
        
            """
            self._pcb[self._pcb[p].getParent()].remChild(p)
            children = self._pcb[p].getChildren().copy()
            res = self._pcb[p].getResources().copy()
            s = 0
            for i in self._rcb:
                i.remWaitlist(p)
            for i in res:
                self.release(i[0],i[1],p)
            for i in children:
                recurDel(i)
            self._rl.remove(p)
            self._pcb[p] = None
            return None
        if p == 0:
            return -1
        if (not self._pcb[self._rl.getRun()].isChild(p)) and p != self._rl.getRun():
            raise ValueError('Process is not a child of the current process.')
        s = recurDel(p)
        self._rl.scheduler()
        return str(self._rl.getRun())

    def timeout(self) -> None:
        """Times out the currently running process.
            
        Returns:
            str: Currently running process.
        
        """
        self._pcb[self._rl.getRun()].ready()
        self._rl.timeout()
        self._rl.scheduler()
        self._pcb[self._rl.getRun()].run()
        return str(self._rl.getRun())

    def __repr__(self) -> str:
        s = ''
        s += 'pcb\n---\n'
        for i in range(len(self._pcb)):
            if i < 10:
                s += ' '
            s += str(i) + " : "
            if self._pcb[i] == None:
                s += 'None'
            else:
                s += str(self._pcb[i])
            s += '\n'
        s += '\nrcb\n---\n'
        for i in range(len(self._rcb)):
            s += str(i) + ' : '
            if self._rcb[i] == None:
                s += 'None'
            else:
                s += str(self._rcb[i])
            s += '\n'
        s += '\nrl\n--\n' + str(self._rl) + '\n'
        return s




