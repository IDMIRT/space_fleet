from flask import Flask, jsonify, request
import json
from startsflot import Mission, Spaceship,CrewMember
import os


app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False

members = []
starships = []
missions = []

spaceships = list()


def load_data(name_file):  

    if os.path.exists(name_file):  
        list_data = []
        with open(name_file,'r',encoding='utf-8') as file:    
            json_data = json.load(file)

            if isinstance(json_data,list):
                
                for value_json in json_data:
                    new_data_dict = dict()
                
                    for key, value in value_json.items():                
                        new_data_dict[key] = value
                
                    list_data.append(new_data_dict)
                    
                return list_data
            else:
                return None
    else:
        print(f'Не найден файл {name_file}')
        return None        
       


def save_file(name_file,data_variable):
    with open(name_file,'w') as file:
        json.dump(data_variable,file, ensure_ascii=False, indent=4)


def return_ship_with_id(id):
    """по id корабля возращает класс Spaceship"""
    if not starships is None:
        for ship in starships:
            if ship.spaceship_id == id:
                return ship
    return None


def return_member_dict_with_id(id):
    """по id корабля возращает класс CrewMember"""
    if not members is None:
        for member in members:
            if member.member_id == id:
                return member
    return None


def save_ships():
    strarships_dict = [ship.get_dict_ships() for ship in starships]
    
    with open('starships.json','w', encoding='utf-8') as ship_file:
        json.dump(strarships_dict, ship_file, ensure_ascii=False, indent=2)

        



def return_mission_with_id(id):
    pass 

@app.route('/ship/list',methods=['GET'])
def return_ships():
    list_spaceships = [ship.get_dict_ships() for ship in starships]
    # for ship in starships:
    #     dict_ship = ship.get_dict_ships()
        # if not dict_ship['members'] is None:
        #     dict_member = []

        #     for member in dict_ship['members'] :
        #         dict_member.append(member.return_dict_member())
        
        #     dict_ship['members'] = dict_member        
        
        # list_spaceships.append(dict_ship)
    return list_spaceships
   


@app.route('/ship/add/',methods=['POST','GET'])
def ship_add():
    """процедура добавления корабля
    входящий  Content-Type - application/json 
    данные в json
    name:str - имя корабля 
    type:str - тип корабля"""
    data_ship = request.get_json(silent=True)
    name = data_ship.get('name')
    type = data_ship.get('type')

    if name is None:
        return "Нет указано имя корабля"
    
    if type is None:
        return "Не указан тип корабля"

    new_ship = Spaceship(name,type) 
    starships.append(new_ship)
    save_ships()
    return new_ship.get_dict_ships(),200 


if __name__ == "__main__":

    # загрузка уже существующих данных
    members_dict = load_data('members.json')
    for value_member in members_dict:
        members.append(CrewMember(value_member['name'],value_member['role'],value_member['member_id']))

    ships_dict = load_data('starships.json')
    for valuе_ship in ships_dict:
        new_ship = Spaceship(valuе_ship['name'],valuе_ship['type'],valuе_ship['spaceship_id'],valuе_ship['status'])
        
        members_list = []
        if not valuе_ship['members'] is None:
            # members_list = [return_member_dict_with_id(id_member) for id_member in valuе_ship['members'] if return_member_dict_with_id(id_member) !=None] 
            members_list = [id_member for id_member in valuе_ship['members']] 
            new_ship.members = members_list 

        starships.append(new_ship)

    missions_dict = load_data('missions.json')
    for value_mission in missions_dict:
        new_mission = Mission(value_mission['name'],value_mission['goal'],
                              value_mission['mission_id'],value_mission['status'])
        ship_list = []
        if not value_mission['spaceship'] is None:
            ship_list = [return_ship_with_id(id_ship) for id_ship in value_mission['spaceship'] if return_ship_with_id(id_ship) != None]
            new_mission.spaceships = ship_list

        missions.append(new_mission)



    app.run(debug=True)


