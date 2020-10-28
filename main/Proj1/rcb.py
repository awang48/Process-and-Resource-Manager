class rcb:

    # Creates resource control block
    #   * _state    = Current state ('f', 'a')
    #   * _waitlist = List of (process index, # units) 
    #   * _capacity = Maximum number of units for resource
    #   * _unit     = Current number of available units
    def __init__(self, u=0):
        self._state = 'f'
        self._waitlist = []
        self._capacity = u
        self._unit = u
    
    # Returns number of units available
    def getUnit(self):
        return self._unit

    # Returns True if this resource has enough units to allocate, False otherwise.
    def canAllocate(self,u):
        return True if (self._state == 'f' and self._unit >= u) else False
    
    # Allocating operation
    def allocate(self,u):
        self._unit -= u
        self._state = 'a'
        return None

    # Adds (process, units) to the waitlist
    def addWaitlist(self,p):
        self._waitlist.append(p)
        return None