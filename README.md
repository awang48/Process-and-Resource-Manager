# Process and Resource Manager
A Python application for managing processes and resources.  
Processes are managed by a triple-layered ready list.  
Runs on either <strong> automated mode </strong> or <strong> debug mode </strong>.  
Program assumes only valid opcodes.  

## Installation
Move all .py files, except test.py, to any desired directory.  

## Usage
### Automated mode
Provide an input file with valid line-separated input commands.  
Valid example provided with input.txt.  

```bash
python main.py <input file>
```

### Debug mode
To either debug or see a step-by-step simulation, run debug.py. Shows the status of the list of process  
control blocks (pcb), the list of resource control blocks (rcb), and the ready list (rl) after each command.  
'e' to exit.  

```bash
python debug.py
```

# Output
### Automated mode
Output is output.txt, with currently running process number printed after each command. New instantiations of the  
manager start on new lines. -1 is printed when the argument is invalid.  
```bash
0 1 2 -1

```
Four commands were used, with process 0, 1, and 2 being the running processes after each command. Invalid opcode/arg  
combination for the fourth command, resulting in -1.  

### Debug mode
Console output is shown through three blocks.  
```bash
> in  
pcb  
---  
 0 : [st: run, par: None, child: [], res: [], prio: 0]  
 1 : None  
 2 : None  
 3 : None  
 4 : None  
 5 : None  
 6 : None  
 7 : None  
 8 : None  
 9 : None  
10 : None  
11 : None  
12 : None  
13 : None  
14 : None  
15 : None  

rcb
---
0 : [wl: [], cap: 1, unit: 1]
1 : [wl: [], cap: 1, unit: 1]
2 : [wl: [], cap: 2, unit: 2]
3 : [wl: [], cap: 3, unit: 3]

rl
--
self._currRun: 0
self._rl[2]: []
self._rl[1]: []
self._rl[0]: [0]

```
After 'in', the pcb, rcb, and rl are shown.  
  
For pcb, st = state (ready, running, blocked), par = parent index, child = list of child indices,  
res = list of currently allocated \[resource, units\], and prio = priority ( 0-2, inclusive ).  
  
For rcb, wl = waitlist of \[process, units\], cap = maximum capacity of units, unit = current # of units available.  
  
For rl, self._currRun = currently running process, self._rl\[0-2\] are levels of the ready list, with self._rl\[2\] being  
the highest priority.  

## Opcodes + Arg(s)
```
in         -    Initiates a new instance of the manager. Maximum of 16 processes,  
				including process 0. Maximum of 4 resources, zero-indexed.  
cr <p>     -    Creates a new process at priority level <p>. <p> must be either 0, 1, or 2.  
de <i>     -    Destroys process <i>. <i> can not be 0. Recursively destroys <i> and all of  
				its children, deallocating resources as necessary.  
rq <r> <n> -    Requests <n> units of resource <r> and allocates, if possible.  
rl <r> <n> -    Releases <n> units of resource <r> and allocates to the next process on the  
				waiting list that is requesting an equal or less amount of units.  
to         -    Times out currently running process and runs next process on same priority level.  

```