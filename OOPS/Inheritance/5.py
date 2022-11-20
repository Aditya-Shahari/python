class Salon:
    tv = 1
    chair = 5

    def __init__(self, salon_name, no_workers):
        self.salon_name = salon_name
        self.no_workers = no_workers

    def info_salon(self):
        print(self.salon_name)
        print(self.no_workers)

    @classmethod
    def cls_meth(cls):
        print(cls.tv)
        print(cls.chair)


class Worker(Salon):
    def __init__(self, worker_name, worker_shift, salon_name, no_workers):
        super().__init__(salon_name, no_workers)
        self.worker_name = worker_name
        self.worker_shift = worker_shift

    def info_worker(self):
        print(self.worker_name)
        print(self.worker_shift)




worker1 = Worker("Raju", "Morning", "Pablo", 7)
worker1.info_salon()
worker1.info_worker()
print(worker1.tv)
print(worker1.chair)
Worker.tv = 2

worker2 = Worker("Ram", "Night", "Pablo", 7)
print(worker2.tv)