class pcb:

    # Creates process control block
    #   * _state     = Current state ('r', 'b', 'run')
    #   * _parent    = Index of parent process 
    #   * _children  = List of indexes of children processes
    #   * _resources = List of (resource index, # unit) currently allocated
    def __init__(self, parent=None):
        self._state = 'r'
        self._parent = parent
        self._children = []
        self._resources = []

    # Returns the state of the process ['r','b','ru']
    def getState(self):
        return self._state

    # Returns the index of the parent process.
    def getParent(self):
        return self._parent

    # Returns the list of children
    def getChildren(self):
        return self._children

    # Returns the list of allocated resources
    def getResources(self):
        return self._resources

    # Add a child to _children
    def addChild(self, c):
        self._children.append(c)
        return None

    # Remove a child from _children
    def remChild(self, c):
        ind = self._children.index(c)
        self._children.pop(ind)
        return None

    # Add a resource to _resources
    def addResource(self, r, u):
        self._resources.append(tuple([r,u]))
        return None

    # Remove a resource from _resource.
    # Returns the number of units released.
    def remResource(self, r):
        for i in range(len(self._resources)):
            if self._resources[i][0] == r:
                return self._resources.pop(i)[1]
        raise ValueError("Resource" + str(r) + "not in _resources")

    # Change _state to ready
    def ready(self):
        self._state = 'r'
        return None
        
    # Change _state to blocked
    def block(self):
        self._state = 'b'
        return None

    # Change _state to running
    def run(self):
        self._state = 'run'
        return None
