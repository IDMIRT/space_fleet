from flask import Flask
import json


app = Flask(__name__)

members = None
ships = None
missions = None

def load_data(name_file,data_variable):    
    with open(name_file,'r') as file:    
        if bool(json.load(file)):
            data_variable = json.load(file)
        else:
            print(f'Нет данных в {name_file}')


def save_file(name_file,data_variable):
    with open(name_file,'w') as file:
        json.dump(data_variable,file, ensure_ascii=False, indent=4)





# with open('members.json','r') as m:
#     # data = json.load(m)
#     if bool(json.load(m)):
#         members = json.load(m)

# with open('ships', 'r') as s:

