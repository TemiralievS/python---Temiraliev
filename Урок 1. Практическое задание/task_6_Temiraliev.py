"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

class Tasks():
    def __init__(self):
        self.waiting_tasks = []
        self.tasks_in_progress = []
        self.completed_tasks = []

    def add_task(self, name):
        self.waiting_tasks.append(name)

    def in_progress(self, name):
        new_in_progress = self.waiting_tasks.pop(self.waiting_tasks.index(name))
        self.tasks_in_progress.append(new_in_progress)

    def completed(self, name):
        new_completed_tasks = self.tasks_in_progress.pop(self.tasks_in_progress.index(name))
        self.completed_tasks.append(new_completed_tasks)

    def __str__(self):
        return f'Задачи ожидающие решения:{self.waiting_tasks} \nВ Задачи процессе: {self.tasks_in_progress} \nВыполненные задачи: {self.completed_tasks}'

task = Tasks()
task.add_task('1 задание')
task.add_task('2 задание')
task.add_task('3 задание')
task.add_task('4 задание')
task.in_progress('1 задание')
task.in_progress('2 задание')
task.completed('1 задание')
print(task)