import json

def loadData(name):
    try:
        with open(f'{name}', 'r') as file:
            datos = json.load(file)
            return datos
    
    except FileNotFoundError:
        return {}
    
    except json.JSONDecodeError:
        return {}

def saveData(name, data):
    with open(f'{name}', 'w') as file:
        json.dump(data, file, indent=4)