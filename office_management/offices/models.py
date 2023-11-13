from django.db import models


class Room(models.Model):
    """Модель описывает комнаты в офисе."""
    # office = models.ForeignKey(Office, on_delete=models.CASCADE)
    number = models.CharField(max_length=10, unique=True, help_text='Номер комнаты')
    capacity = models.PositiveIntegerField(help_text='Вместимость комнаты')

    def __str__(self):
        return self.number


class Employee(models.Model):
    """Модель описывает сотрудников и их привязку к комнатам."""
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room', help_text='Текущее рабочее место сотрудника')
    name = models.CharField(max_length=40, help_text='Имя сотрудника')
    start_date = models.DateField(help_text='Дата начала работы на рабочем месте')
    end_date = models.DateField(help_text='Дата окончания работы на рабочем месте')
    rooms_history = models.ManyToManyField(Room, related_name='employees_history', blank=True)

    def __str__(self):
        return self.name


class Office(models.Model):
    """Модель описывает офисы."""
    address = models.CharField(max_length=20)
    rooms = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.address
