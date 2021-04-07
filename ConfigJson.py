import json
from os.path import isfile

def getJsonData():
    # If there is a config.json file, it reads it and returns its data.
    if isfile('config.json'):
        with open("config.json",'r') as f:
            data=json.loads(f.read())
            return data
    else:
        print("NOT EXISTS")

def createJsonFile(Filters:list):
    # If the config.json file does not exist, it creates it
    # and writes the desired information in it.
    if not isfile('config.json'):
        # Create a dictionary from datas.
        x={"filters":Filters}
        # Convert the dictionary data to json data.
        jsonData=json.dumps(x)
        # Write the json data to json file
        with open("config.json",'w') as f:
            f.write(jsonData)
    # If the config.json exists :
    else:
        # Read the config.json file.
        data=getJsonData()
        t=0
        # Get filters key values
        x=data['filters']
        # Create a copy from datas.
        jsonList=x
        # Checking loop :
        while t <= len(Filters) - 1:
            # If there are the same filters in the file,
            # do not add them again.
            if Filters[t] in x:
                pass
            # Else if they were not repeated again 
            elif Filters[t] not in jsonList:
                # Then add them to the values
                jsonList.append(Filters[t])
            t+=1
        # At the end, create the new dictionary from datas.
        y={"filters":jsonList}
        # And write them to file.
        with open('config.json','w') as f:
            f.write(json.dumps(y))
