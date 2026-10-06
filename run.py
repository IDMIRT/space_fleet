from flask import Flask
import json
from startsflot import Mission, Spaceship,CrewMember


app = Flask(__name__)

members = []
ships = None
missions = None

spaceships = list()


def load_data(name_file,data_variable):    
    with open(name_file,'r') as file:    
        if bool(json.load(file)):
            data_variable = json.load(file)
        else:
            print(f'Нет данных в {name_file}')


def save_file(name_file,data_variable):
    with open(name_file,'w') as file:
        json.dump(data_variable,file, ensure_ascii=False, indent=4)



if __name__ == "__main__":
    member_dict = None
    load_data('members.json',member_dict)

    # if not member_dict == None:

    #     for value_member in member_dict:
    #         members[key] = value



    # load_data('ships.json',ships)

    # if not ships == None:
    #     for ship in ships:




    app.run(debug=True)

# with open('members.json','r') as m:
#     # data = json.load(m)
#     if bool(json.load(m)):
#         members = json.load(m)

# with open('ships', 'r') as s:

