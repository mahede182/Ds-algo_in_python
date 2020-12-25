# FIFO methode.
class queue:
    def __init__(self):
        self.queues = list()
    def addtoq(self,dataval):
        if dataval not in self.queues:
            self.queues.insert(0,dataval)
            return True
        return False
    def size(self):
        return len(self.queues)
    def removfromq(self):
        if len(self.queues)>0:
            return self.queues.pop()
        return ("No element in q")
theQueue = queue()
rq = queue()
theQueue.addtoq("mahede")
theQueue.addtoq("Ashis")
theQueue.addtoq("khaled")
print(theQueue.size())


rq.addtoq("mahede")
rq.addtoq("Ashis")
rq.addtoq("khaled")
print(rq.removfromq())
print(rq.size())