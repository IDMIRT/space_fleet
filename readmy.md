Вы капитан звездного флота и перед вами стоит задача организовать управление космическими кораблями, миссиями и экипажем. Вам нужно спроектировать три ключевых класса: Spaceship, Mission и CrewMember. Каждый из этих классов будет представлять отдельную сущность вашего флота.

##Шаг 1. Создайте класс Spaceship

Космический корабль (Spaceship) должен обладать следующими характеристиками:

spaceship_id (уникальный идентификатор корабля).
name (название корабля).
type_ (тип корабля: исследовательский или боевой).
status (текущий статус корабля: «доступен», «в миссии», «на ремонте»).
Также добавьте метод для изменения статуса корабля.

Пример кода:

```python
class Spaceship:
    def __init__(self, spaceship_id, name, type_, status="available"):
        self.spaceship_id = spaceship_id
        self.name = name
        self.type_ = type_
        self.status = status

    def update_status(self, new_status):
        self.status = new_status
```

##Шаг 2. Создайте класс Mission

Миссия (Mission) должна включать:

mission_id (уникальный идентификатор миссии).
name (название миссии).
goal (цель миссии: исследование или защита).
status (текущий статус миссии: «запланирована», «в процессе», «завершена»).
Список кораблей, участвующих в миссии (spaceships).
Добавьте метод для добавления корабля в миссию.

Пример кода:

```python
class Mission:
    def __init__(self, mission_id, name, goal, status="planned"):
        self.mission_id = mission_id
        self.name = name
        self.goal = goal
        self.status = status
        self.spaceships = []

    def add_spaceship(self, spaceship):
        self.spaceships.append(spaceship)
```

##Шаг 3. Создайте класс CrewMember

Член экипажа (CrewMember) должен обладать следующими характеристиками:

member_id (уникальный идентификатор члена экипажа).
name (имя члена экипажа).
role (роль в экипаже: капитан, инженер или пилот).
Пример кода:

class CrewMember:
    def __init__(self, member_id, name, role):
        self.member_id = member_id
        self.name = name
        self.role = role

##Шаг 4. Проверка работы классов

Создайте несколько объектов каждого класса и убедитесь в их корректной работе.

