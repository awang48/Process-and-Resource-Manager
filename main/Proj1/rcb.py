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

    # Returns current state of resource
    def getState(self):
        return self._state
    
    # Allocating operation. Dedicates units and changes state to 'a'. Raises ValueError if desired # units are not available.
    def allocate(self,u):
        if (self._unit - u < 0):
            raise ValueError("Resource does not have enough units: Requested" + str(u) +  ", Available" + str(self._unit))
        self._unit -= u
        self._state = 'a'
        return None

    # Releasing operation. Releases units and changes state to 'f'. Raises ValueError if releasing too many units.
    def release(self, u):
        if (self._unit + u > self._capacity):
            raise ValueError("Releasing too many units. Theoretical total:" +  str(u) +  " Max capcacity:" + str(self._capacity))
        self._unit += u
        self._state = 'f'
        return None


    # Adds (process, units) to the waitlist
    def addWaitlist(self, p, u):
        self._waitlist.append(tuple([p,u]))
        return None