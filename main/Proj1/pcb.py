class pcb:
    """A pcb (Process Control Block)
    
    Attributes:
        _state ('str'): Current state of the process. 'r' = 'ready', 'b' = 'blocked', 'run' = 'running'
        _parent ('int'): Index of parent process.
        _children (:obj:'list' of :obj:'int'): List of integer indexes of children processes.
        _resources (:obj:'list' of :obj:'list' of :obj:'int'): List of [resource index, # units].
        _priority ('int'): Current priority of the process. [0,2]
        
    """

    def __init__(self, parent: int =-1, priority: int =0):
        self._state = 'r'
        self._parent = parent
        self._children = []
        self._resources = []
        self._priority = priority

    def getState(self) -> str:
        """Obtains the current state of the pcb.
        
        Returns:
            str: Current state
        
        """
        return self._state

    def getParent(self) -> int:
        """Obtains the index of the parent process.
        
        Returns:
            int: Index of the parent process.
        
        """
        return self._parent

    def getChildren(self) -> list:
        """Obtains the list of the indexes of children processes.
        
        Returns:
            list(int): List of children processes.
        
        """
        return self._children

    def getResources(self) -> list:
        """Obtains the list of currently held resources, as well as how many units of each resource.
        
        Returns:
            list(list(int)): List of [resource index, # unit].
        
        """
        return self._resources

    def getPriority(self) -> int:
        """Obtains priority level.
        
        Returns:
            int: Priority level.
        
        """
        return self._priority

    def isChild(self, c: int) -> bool:
        """Checks if the parameter variable is an immedaite child of the current process.
        
        Args:
            c (int): Child process index.
            
        Returns:
            bool: True if c is an immediate child of the current process. False otherwise.

        """
        return c in self._children

    def hasResource(self, r: int) -> bool:
        """Checks if the resource indicated by the parameter variable is being held by the current process.
        
        Args:
            r (int): Resource index.
            
        Returns:
            bool: True if r is being held by the current process. False otherwise.
        
        """
        for i in self._resources:
            if i[0] == r:
                return True
        return False

    def addChild(self, c: int) -> None:
        """Adds a child process to the current process.
        
        Args:
            c (int): Child process index.
            
        Returns:
            None
        
        """
        self._children.append(c)
        return None

    def remChild(self, c: int) -> int:
        """Removes a child from the current process.
        
        Args:
            c (int): Child process index.
            
        Returns:
            str: Currently running process.

        Raises:
            ValueError: If c is not a child process index.
        
        """
        for i in range(len(self._children)):
            if self._children[i] == c:
                return self._children.pop(i)
        raise ValueError("Child " + str(c) + " not in _children")

    def addResource(self, r: int, u: int) -> None:
        """Holds a resource.
        
        Args:
            r (int): Resource index.
            u (int): Unit count.
            
        Returns:
            None
        
        """
        for i in self._resources:
            if i[0] == r:
                i[1] += u
        else:
            self._resources.append([r,u])
        return None

    def remResource(self, r: int, u: int) -> int:
        """Removes a certain amount of units from a resource.
        
        Args:
            r (int): Resource index.
            u (int): Unit count.
            
        Returns:
            int: Number of units removed.

        Raises:
            ValueError: If the process is not holding that many units or if the resource is not being held.
        
        """
        for i in range(len(self._resources)):
            if self._resources[i][0] == r:
                if (self._resources[i][1] == u):
                    return self._resources.pop(i)[1]
                elif (self._resources[i][1] > u):
                    self._resources[i][1] -= u
                    return u
                else:
                    raise ValueError("Releasing too many resources")
        raise ValueError("Resource " + str(r) + " not in _resources")

    def ready(self) -> None:
        """Changes the process' state to 'ready'.
            
        Returns:
            None
        
        """
        self._state = 'r'
        return None
        
    def block(self) -> None:
        """Changes the process' state to 'blocked'.
        
        Returns:
            None
        
        """
        self._state = 'b'
        return None

    def run(self) -> None:
        """Changes the process' state to 'running'.
        
        Returns:
            None
        
        """
        self._state = 'run'
        return None

    def __str__(self) -> str:
        return '[st: ' + str(self._state) + ', par: ' + str(self._parent) + ', child: ' + str(self._children) + ', res: ' + str(self._resources) + ', prio: ' + str(self._priority) + ']'
    
    def __repr__(self) -> str:
        return 'self._state: ' + str(self._state) + '\n' + 'self._parent: ' + str(self._parent) + '\n' + 'self._children: ' + str(self._children) + '\n' + 'self._resources: ' + str(self._resources) + '\n' + 'self._priority: ' + str(self._priority) + '\n'
