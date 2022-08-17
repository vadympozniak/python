"""Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss.
Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss.
You're not allowed to add instances of Boss class to workers list directly via access to attribute,
use getters and setters instead!
You can refactor the existing code."""


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id_ = id_
        self.name = name
        self.company = company
        self.workers = []

    @property
    def list_workers(self):
        return self.workers

    @list_workers.setter
    def list_workers(self, worker):
        if worker[3] == self.name:
            if worker[2] == self.company:
                self.workers.append(worker)
            else:
                print(f'In company {self.company} boss {self.name}, not a {worker[4]}')
        else:
            print(f'{worker[1]} worked wit {worker[3]}, not a {self.name}')


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id_ = id_
        self.name = name
        self.company = company
        self.boss = boss


if __name__ == '__main__':
    boss_1 = Boss(1, 'Dmytro', 'Beetroot')
    boss_2 = Boss(2, 'Victor', 'Academy')
    worker_1 = (1, 'Veronika', 'Beetroot', 'Dmytro')
    worker_2 = (2, 'Oleg', 'Beetroot', 'Dmytro')
    worker_3 = (3, 'Vadym', 'Academy', 'Victor')
    worker_4 = (4, 'Vlad', 'Academy', 'Victor')
    boss_1.list_workers = worker_1
    boss_1.list_workers = worker_2
    boss_2.list_workers = worker_3
    boss_2.list_workers = worker_4
    boss_1.list_workers = worker_3
    boss_2.list_workers = worker_1
    print(boss_1.list_workers)
    print(boss_2.list_workers)