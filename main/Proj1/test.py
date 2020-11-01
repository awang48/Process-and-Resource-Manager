
from manager import manager
from rl import rl
from rcb import rcb
from pcb import pcb

if (__name__ == "__main__"):
    ## Testing RCB
    ## -----------
    
    ## Constructor
    #r = rcb(5)
    #print(r)

    ## allocate()
    #r.allocate(5)
    #print(r)

    ## release()
    #r.release(5)
    #print(r)

    ## addWaitlist()
    #r.addWaitlist(0,2)
    #r.addWaitlist(1,5)
    #r.addWaitlist(2,3)
    #print(r)

    ## remWaitlist()
    #r.remWaitlist(1)
    #try:
    #    r.remWaitlist(10)
    #except ValueError as e:
    #    print(e)
    #print(r)

    ## waitlistNext()
    #print(r.waitlistNext())
    #print(r)

    ## Testing PCB
    ## -----------

    ## Constructor
    #p1 = pcb(1,2)
    #p2 = pcb(2)
    #print(p1)
    #print(p2)

    ## getState(), getParent(), getPriority()
    #print(p1.getState())
    #print(p1.getParent())
    #print(p1.getPriority())

    ## getChildren(), addChild(), remChild()
    #print(p1.getChildren())
    #p1.addChild(0)
    #p1.addChild(3)
    #print(p1.getChildren())
    #p1.remChild(3)
    #print(p1.getChildren())
    #try:
    #    p1.remChild(4)
    #    print("Shouldn't have gotten here")
    #except ValueError as e:
    #    print(e)

    ## getResources(), addResource(), remResource()
    #print(p1.getResources())
    #p1.addResource(1, 5)
    #p1.addResource(2,3)
    #print(p1.getResources())
    #p1.remResource(2,1)
    #print(p1.getResources())
    #p1.remResource(2,2)
    #print(p1.getResources())
    #try:
    #    p1.remResource(1,6)
    #except ValueError as e:
    #    print(e)
    #try:
    #    p1.remResource(3,5)
    #except ValueError as e:
    #    print(e)
    #print(p1.getResources())
    
    ## block(), run(), ready()
    #p1.block()
    #print(p1)
    #p1.run()
    #print(p1)
    #p1.ready()
    #print(p1)

    ## Testing RL
    ## ----------

    ## Constructor
    #r = rl()
    #print(r)

    ## add(), scheduler()
    #r.add(0,0)
    #r.scheduler()
    #print(r)
    #r.add(1,1)
    #r.scheduler()
    #print(r)
    #r.add(2,2)
    #r.scheduler()
    #r.add(3,2)
    #r.add(4,0)
    #print(r)

    ## timeout()
    #r.timeout()
    #r.scheduler()
    #print(r)

    ## getRun()
    #print(r.getRun())

    ## remove()
    #r.remove(4)
    #r.scheduler()
    #print(r)
    #try:
    #    r.remove(10)
    #except ValueError as e:
    #    print(e)
    #r.remove(2)
    #r.remove(3)
    #r.scheduler()
    #print(r)
    #r.add(3,1)
    #r.scheduler()
    #r.timeout()
    #r.scheduler()
    #print(r)

    # Testing manager
    # ---------------

    # Testing constructor
    m = manager()
    #print(m)
    # Testing create
    m.create(1)
    m.create(2)

    # Testing request
    m.request(1,1)
    #try:
    #    m.request(3,4)
    #except ValueError as e:
    #    print(e)
    #try:
    #    m.request(1,1)
    #except ValueError as e:
    #    print(e)
    m.request(0,1)
    m.request(2,2)
    #print(m)

    # Testing release
    m.release(0,1)
    m.release(2,1)
    m.create(2)
    m.timeout()
    m.request(3,3)
    m.timeout()
    m.request(3,3)
    m.release(3,3)
    m.request(3,1)
    m.release(3,1)

    # Testing destroy
    m.timeout()
    m.create(2)
    m.timeout()
    print(m)
    m.destroy(2)
    print(m)