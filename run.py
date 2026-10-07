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
        
        # if bool(json.load(file)):
        #     data_variable = json.load(file)
        # else:
        #     print(f'Нет данных в {name_file}')


def save_file(name_file,data_variable):
    with open(name_file,'w') as file:
        json.dump(data_variable,file, ensure_ascii=False, indent=4)



if __name__ == "__main__":
    
    members_dict = load_data('members.json')
    for value in members_dict:
        members.append(CrewMember(value['name'],value['role'],value['member_id']))

    ships_dict = load_data('starships.json')
    for valuе in ships_dict:
        starships.append(Spaceship(value['name'],value['type'],value['spaceship_id'],value['status']))

    missions_dict = load_data("missions.json")
    for value in missions_dict:
        missions.append(Mission(value))





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

