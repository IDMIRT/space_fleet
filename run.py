from flask import Flask
import json
from startsflot import Mission, Spaceship,CrewMember
import os


app = Flask(__name__)

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
                # if not member_dict == None:
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
    """по id корабля возращает класс Spaceship и возвращает его"""
    if not starships is None:
        for ship in starships:
            if ship.spaceship_id == id:
                return ship
    return None


def return_member_with_id(id):
    """по id корабля возращает класс CrewMember"""
    if not members is None:
        for member in members:
            if member.member_id == id:
                return member
    return None

def return_mission_with_id(id):
    pass


    
    




if __name__ == "__main__":
    
    members_dict = load_data('members.json')
    for value_member in members_dict:
        members.append(CrewMember(value_member['name'],value_member['role'],value_member['member_id']))

    ships_dict = load_data('starships.json')
    for valuе_ship in ships_dict:
        new_ship = Spaceship(valuе_ship['name'],valuе_ship['type'],valuе_ship['spaceship_id'],valuе_ship['status'])
        
        members_list = []
        if not valuе_ship.members is None:
            members_list = [return_member_with_id(id_member) for id_member in valuе_ship.members if return_member_with_id(id_member) !=None] 
            new_ship.members = members_list 

        starships.append(new_ship)

    missions_dict = load_data('missions.json')
    for value_mission in missions_dict:
        pass

    # missions_dict = load_data("missions.json")
    # for value in missions_dict:
    #     missions.append(Mission(value['name'],value['goal'],value['status'],))

    # ship_list = [return_ship_with_id(ship) for ship  in [1,2,13] if return_ship_with_id(ship) != None ]




    # if not member_dict == None:
    #     for value_member in member_dict:
    #         new_member = dict()

    #         for key, value in value_member.items():                
    #             new_member[key] = value

    #         members.append(new_member)
            



    # load_data('ships.json',ships)

    # if not ships == None:
    #     for ship in ships:




    app.run(debug=True)

# with open('members.json','r') as m:
#     # data = json.load(m)
#     if bool(json.load(m)):
#         members = json.load(m)

# with open('ships', 'r') as s:

