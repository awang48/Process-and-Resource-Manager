class rcb:
    """A rcb (Resource Control Block)
    
    Attributes:
        _waitlist (:obj:'list' of :obj:'list' of :obj:'int'): Current waitlist for the resource. List of [Process index, # units]
        _capacity ('int'): Maximum number of units for this resource.
        _unit ('int'): Number of currently available units of this resource.
        
    """

    def __init__(self, u: int =0):
        self._waitlist = []
        self._capacity = u
        self._unit = u
    
    def getUnit(self) -> int:
        """Obtains the current number of units available for this resource.
            
        Returns:
            int: Current number of units.
        
        """
        return self._unit

    def getCapacity(self) -> int:
        """Obtains maximum capacity for this resource.
        
        Returns:
            int: Maximum number of units available.
        
        """
        return self._capacity

    def allocate(self,u: int) -> None:
        """Allocates a number of units.
        
        Args:
            u (int): Number of units to be allocated.
            
        Returns:
            None

        Raises:
            ValueError: If the resource does not have the number of units requested.
        
        """
        if (self._unit - u < 0):
            raise ValueError("Resource does not have enough units: Requested" + str(u) +  ", Available" + str(self._unit))
        self._unit -= u
        return None

    def release(self, u: int) -> None:
        """Releases a number of units.
        
        Args:
            u (int): Number of units to be released.
            
        Returns:
            None

        Raises:
            ValueError: If the number of units to be released totals over the capacity.
        
        """
        if (self._unit + u > self._capacity):
            raise ValueError("Releasing too many units. Theoretical total:" +  str(u) +  " Max capcacity:" + str(self._capacity))
        self._unit += u
        return None

    def addWaitlist(self, p: int, u: int) -> None:
        """Adds a process index and the number of units to the waitlist.
        
        Args:
            p (int): Process index
            u (int): Number of units.
            
        Returns:
            None
        
        """
        self._waitlist.append([p,u])
        return None

    def remWaitlist(self, p: int) -> list:
        """Removes a process from the current waitlist.
        
        Args:
            p (int): Process index.

        Returns:
            list(int): [process index, # units].
        
        """
        for i in range(len(self._waitlist)):
            if self._waitlist[i][0] == p:
                return self._waitlist.pop(i)

    def waitlistNext(self) -> list:
        """Obtains a list of [process index, # units] that will fit in the number of currently available units.
        
        Returns:
            list(list(int)): List of [process index, # units].
        
        """
        offWL = []
        newWL = []
        tentativeUnits = self._unit
        for i in range(len(self._waitlist)):
            if self._waitlist[i][1] <= self._unit and self._waitlist[i][1] <= tentativeUnits:
                offWL.append(self._waitlist[i])
                tentativeUnits -= self._waitlist[i][1]
            else:
                newWL.append(self._waitlist[i])
        self._waitlist = newWL
        return offWL

    def __str__(self) -> str:
        return '[wl: ' + str(self._waitlist) + ', cap: ' + str(self._capacity) + ', unit: ' + str(self._unit) + ']'
    
    def __repr__(self) -> str:
        return 'self._waitlist: ' + str(self._waitlist) + '\n' + 'self._capacity: ' + str(self._capacity) + '\n' + 'self._unit: ' + str(self._unit) + '\n'
