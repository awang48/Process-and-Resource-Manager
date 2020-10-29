class rl:

    # Creates a ready list
    #   * _rl = Ready list -- Index is priority
    def __init__(self):
        self._rl = [[],[],[]]

    # Returns the highest priority process in the ready list
    def scheduler(self):
        for i in self._rl[2::-1]:
            if len(i) != 0:
                return i[0]

    # Removes a process from the ready list
    # Returns 1 on success, 0 on failure.
    def remove(self,p):
        for i in self._rl:
            if p in i:
                i.pop(i.index(p))
                return None
        raise ValueError("Process" + str(p) + "is not in readylist")
