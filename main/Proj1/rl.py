class rl:
    """A three-level rl (ReadyList) for processes.
    
    Attributes:
        _rl (:obj:`list` of :obj:`list` of :obj:`int`): Three-level ready list of processes. Index indicates priority.
        _currRun (int): Currently running process.
        
    """

    def __init__(self):
        self._rl = [[],[],[]]
        self._currRun = None

    def getRun(self):
        """Obtains currently running process.
        
        Returns:
            int: Currently running process.
            
        """
        return self._currRun
        
    def scheduler(self):
        """Schedules the highest priority process. 
        
        Returns:
            None
            
        """
        for i in range(3):
            ind = 2 - i
            if len(self._rl[ind]) != 0:
                self._currRun = self._rl[ind][0]
                return None
        return None

    def remove(self,p: int) -> None:
        """Removes a process from the ready list.
        
        Args:
            p (int): Process number.
            
        Returns:
            None
        
        """
        for i in self._rl:
            if p in i:
                i.pop(i.index(p))
                return None
        return None

    def add(self, p: int, priority: int) -> None:
        """Adds a process to the ready list.
        
        Args:
            p (int): Process number.
            priority (int): Priority number.
            
        Returns:
            None
            
        """
        self._rl[priority].append(p)
        return None

    def timeout(self):
        """Times out the currently running process and runs the new highest priority.
        
        Returns:
            None
            
        """
        if len(self._rl[2]) != 0:
            self._rl[2].append(self._rl[2].pop(0))
        elif len(self._rl[1]) != 0:
            self._rl[1].append(self._rl[1].pop(0))
        else:
            self._rl[0].append(self._rl[0].pop(0))
        return None

    def __str__(self) -> str:
        return 'self._currRun: ' + str(self._currRun) + '\n' + 'self._rl[2]: ' + str(self._rl[2]) + '\n' + 'self._rl[1]: ' + str(self._rl[1]) + '\n' + 'self._rl[0]: ' + str(self._rl[0]) + '\n'

    def __repr__(self) -> str:
        return 'self._currRun: ' + str(self._currRun) + '\n' + 'self._rl[2]: ' + str(self._rl[2]) + '\n' + 'self._rl[1]: ' + str(self._rl[1]) + '\n' + 'self._rl[0]: ' + str(self._rl[0]) + '\n'