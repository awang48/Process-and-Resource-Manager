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

    # Returns the parent process.
    def getParent(self):
        return self._parent

    # Returns the list of children
    def getChildren(self):
        return self._children

    # Returns the list of allocated resources
    def getResources(self):
        return self._resources

    # Adds (resource, units) to the list of allocated resources
    def addResource(self, r):
        self._resources.append(r)
        return None

    # Add a child to the list of children
    def addChild(self, c):
        self._children.append(c)
        return None

    # Change state to ready
    def ready(self):
        self._state = 'r'
        return None
        
    # Change state to blocked
    def block(self):
        self._state = 'b'
        return None

    # Change state to running
    def run(self):
        self._state = 'run'
        return None

    
