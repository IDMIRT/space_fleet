import uuid

class CrewMember:

    def __init__(self,name,role,member_id=None):
        if member_id == None:
            self.member_id = uuid.uuid4()
        else:
            self.member_id = member_id
        
        self.member_id = member_id
        self.name = name
        self.role = role

    def __str__(self):
        return f'{self.name} {self.role}'


class Spaceship:

    def __init__(self, name:str, type_:str, spaceship_id=None, status="доступен"):

        if spaceship_id == None:
            self.spaceship_id = uuid.uuid4()
        else:
            self.spaceship_id = spaceship_id

        self.spaceship_id = spaceship_id
        self.name = name
        self.type_ = type_
        self.status = status
        self.members = []

    def set_name(self, new_name):
        self.name = new_name if new_name != '' else self.name

    def set_status(self, new_status:str):
        while new_status != None:
            self.status = new_status

    def get_staus(self):
        return self.status

    def __str__(self):
        return f'Корабль {self.name} тип {self.type_} УИД {self.spaceship_id} имеет статус {self.status}'

# def create_new_starship():
#     type_starship = {'1':'Боевой','2':'Исследовательский'}    

#     uid_spaceship = uuid.uuid4()

#     name =''
#     while name=='':
#         name = input('Введите имя корабля: ')

#     type_ship = ''

#     while type_ship == '':
#         type_ship = type_starship.get(input('Выберите тип корабля \n1 - боевой,\n2 - исследовательский: '),'')

#     return Spaceship(name,type_ship,uid_spaceship)


# new_starship = create_new_starship()
# print(new_starship)

class Mission:
    
    def __init__(self, name, goal, mission_id=None, status="в плане"):
        if mission_id == None:
            self.mission_id = uuid.uuid4()
        else:
            self.mission_id = mission_id
        self.name = name
        self.goal = goal
        self.status = status
        self.spaceships = []

    def add_spaceship(self, spaceship:Spaceship):
        self.spaceships.append(spaceship)

    def list_spaceship(self):
        if self.spaceships == []:
            print(f'В миссии {self.name} нет кораблей')
        else:
            print(*self.spaceships,sep = '\n')

    def del_spaceship(self,spaceship:Spaceship):
        if spaceship in self.spaceships:
            self.spaceships.remove(spaceship)
        else:
            print(f'В миссии {self.name} нет корабля {spaceship.name}')

    def get_status(self):
        print(self.status)

    def set_status(self,new_status:str):
        if new_status != '':
            self.status = new_status

    def __str__(self):
        return f'Миссия {self.name} имеет статус {self.name}, в составе корабли {' '.join(ship for ship in self.spaceships )}'

# def new_mission():
#     pass




        






    
        
        
        
        